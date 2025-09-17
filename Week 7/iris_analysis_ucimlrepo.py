
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo

def load_iris_dataset_ucimlrepo():
    try:
        # Fetch Iris dataset by ID from UCI repository
        iris = fetch_ucirepo(id=53)

        # Extract features and target as DataFrames/Series
        X = iris.data.features       # DataFrame of features
        y = iris.data.targets        # Series of targets

        # Combine features and target into one DataFrame
        df = X.copy()
        df['target'] = y

        # Print metadata and variables information
        print("Dataset metadata:\n", iris.metadata)
        print("\nVariable information:\n", iris.variables)

        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def explore_data(df):
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nData Types:")
    print(df.dtypes)
    
    print("\nChecking for missing values:")
    print(df.isnull().sum())
    
    # Cleaning missing data (if any)
    if df.isnull().values.any():
        print("\nMissing values found. Filling missing values with column mean.")
        df.fillna(df.mean(), inplace=True)
    else:
        print("\nNo missing values found.")
        
def basic_analysis(df):
    print("\nBasic statistics of numerical columns:")
    print(df.describe())
    
    print("\nMean of numerical columns grouped by target (species):")
    grouped = df.groupby('target').mean()
    print(grouped)
    
    # Findings:
    print("\nObservations:")
    print("- The mean sepal length and petal length vary significantly between species.")
    print("- Setosa (target=0) tends to have smaller petal lengths compared to Versicolor (1) and Virginica (2).")

def create_visualizations(df):
    sns.set(style="whitegrid")
    
    # Map target to species names for clarity
    species_map = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    df['species'] = df['target'].map(species_map)
    
    # 1. Line Chart: Show sepal length trends by sample index for each species
    plt.figure(figsize=(10,6))
    for species in df['species'].unique():
        subset = df[df['species'] == species]
        plt.plot(subset.index, subset['sepal length (cm)'], label=species)
    plt.title("Sepal Length Trends by Species")
    plt.xlabel("Sample Index")
    plt.ylabel("Sepal Length (cm)")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # 2. Bar Chart: Average petal length per species
    avg_petal_length = df.groupby('species')['petal length (cm)'].mean().sort_values()
    plt.figure(figsize=(8,5))
    sns.barplot(x=avg_petal_length.index, y=avg_petal_length.values, palette="viridis")
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Average Petal Length (cm)")
    plt.tight_layout()
    plt.show()
    
    # 3. Histogram: Distribution of sepal width
    plt.figure(figsize=(8,5))
    sns.histplot(df['sepal width (cm)'], bins=15, kde=True, color='skyblue')
    plt.title("Distribution of Sepal Width")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
    
    # 4. Scatter Plot: Sepal length vs Petal length colored by species
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette="deep", s=80)
    plt.title("Sepal Length vs Petal Length by Species")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title='Species')
    plt.tight_layout()
    plt.show()

def main():
    df = load_iris_dataset_ucimlrepo()
    if df is None:
        print("Failed to load dataset. Exiting.")
        return
    
    explore_data(df)
    basic_analysis(df)
    create_visualizations(df)

if __name__ == "__main__":
    main()
# iris_analysis_ucimlrepo.py