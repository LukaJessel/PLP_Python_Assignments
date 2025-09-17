# Iris Dataset Analysis and Visualization

## Overview
This project demonstrates how to load, analyze, and visualize the classic Iris dataset using Python. The script uses the `pandas`, `matplotlib`, `seaborn`, and `ucimlrepo` libraries to perform data exploration, basic statistical analysis, and create a variety of plots.

## Features
- Loads the Iris dataset directly from the UCI Machine Learning Repository using `ucimlrepo`.
- Explores the dataset: displays the first few rows, data types, and checks for missing values.
- Cleans missing data if present.
- Performs basic statistical analysis (mean, median, standard deviation, group means).
- Visualizes the data with:
  - Line chart (sepal length trends by species)
  - Bar chart (average petal length per species)
  - Histogram (distribution of sepal width)
  - Scatter plot (sepal length vs. petal length, colored by species)
- All plots are customized with titles, axis labels, and legends.
- Includes error handling for data loading.

## Requirements
- Python 3.x
- pandas
- matplotlib
- seaborn
- ucimlrepo

Install dependencies with:
```
pip install pandas matplotlib seaborn ucimlrepo
```

## Usage
1. Run the script:
   ```
   python iris_analysis_ucimlrepo.py
   ```
2. The script will print data exploration and analysis results to the console and display the visualizations.

## File Structure
- `iris_analysis_ucimlrepo.py` — Main script for data analysis and visualization
- `README.md` — Project documentation

## Notes
- The script is self-contained and does not require downloading the dataset manually.
- You can convert this script to a Jupyter notebook for interactive exploration if desired.

## License
This project is for educational purposes.
