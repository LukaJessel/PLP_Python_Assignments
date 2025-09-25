"""
Part 1: Data Loading and Basic Exploration
Loads metadata_first_1000.csv and performs basic exploration.
"""
import pandas as pd

# Load the data
df = pd.read_csv('../metadata_first_1000.csv')

# Examine first few rows
print(df.head())

# DataFrame dimensions
print('Shape:', df.shape)

# Data types
print('Data types:')
print(df.dtypes)

# Missing values
print('Missing values:')
print(df.isnull().sum())

# Basic statistics
print('Basic statistics:')
print(df.describe())
