"""
Part 2: Data Cleaning and Preparation
Handles missing data, prepares columns, and adds new features.
"""
import pandas as pd

df = pd.read_csv('../metadata_first_1000.csv')

# Identify columns with many missing values
missing = df.isnull().sum()
print('Columns with missing values:')
print(missing[missing > 0])

# Drop columns with >50% missing values
threshold = len(df) * 0.5
drop_cols = missing[missing > threshold].index.tolist()
df_clean = df.drop(columns=drop_cols)

# Fill missing values in important columns (example: fillna for 'journal')
if 'journal' in df_clean.columns:
    df_clean['journal'] = df_clean['journal'].fillna('Unknown')

# Convert date columns to datetime
if 'publish_time' in df_clean.columns:
    df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
    df_clean['year'] = df_clean['publish_time'].dt.year

# Add abstract word count
if 'abstract' in df_clean.columns:
    df_clean['abstract_word_count'] = df_clean['abstract'].fillna('').apply(lambda x: len(x.split()))

# Save cleaned data
df_clean.to_csv('metadata_first_1000_cleaned.csv', index=False)
print('Cleaned data saved to metadata_first_1000_cleaned.csv')
