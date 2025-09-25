# CORD-19 Data Analysis Project

Analyze COVID-19 research papers using a subset of the CORD-19 metadata (first 1000 entries). This project demonstrates a full data science workflow: loading, cleaning, analysis, visualization, and interactive exploration with Streamlit.

---

## 📁 Project Structure

```
cord19_analysis/
│
├── part1_data_loading_exploration.py      # Load and explore the data
├── part2_data_cleaning_preparation.py     # Clean and prepare the data
├── part3_data_analysis_visualization.py   # Analyze and visualize the data
├── part4_streamlit_app.py                 # Interactive Streamlit app
├── part5_documentation_reflection.py      # Project summary and reflection
├── requirements.txt                       # Python dependencies
├── README.md                              # Project documentation
├── images/                                # All generated visualization images
│   ├── publications_by_year.png
│   ├── top_journals.png
│   ├── title_wordcloud.png
│   └── source_distribution.png
└── metadata_first_1000_cleaned.csv        # Cleaned data (generated)
```

---

## 🚀 Quick Start

1. **Clone or download this repository.**
2. Place `metadata_first_1000.csv` in the project root or parent directory.
3. *(Optional but recommended)* Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. Install all dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

---

## 🛠️ How to Run Each Part

**1. Data Loading and Exploration**
```powershell
python part1_data_loading_exploration.py
```
*Loads the data and prints basic info to the terminal.*

**2. Data Cleaning and Preparation**
```powershell
python part2_data_cleaning_preparation.py
```
*Cleans the data and saves `metadata_first_1000_cleaned.csv`.*

**3. Data Analysis and Visualization**
```powershell
python part3_data_analysis_visualization.py
```
*Generates all plots and saves them in the `images/` folder.*

**4. Streamlit Interactive App**
```powershell
streamlit run part4_streamlit_app.py
```
*Launches an interactive dashboard in your browser.*

**5. Documentation and Reflection**
```powershell
python part5_documentation_reflection.py
```
*Prints a summary of findings, challenges, and learnings.*

---

## ✨ Features

- Loads and explores a subset of the CORD-19 metadata
- Cleans and prepares data for analysis
- Analyzes publication trends, top journals, and word frequencies
- Generates and saves visualizations (bar charts, word cloud, etc.)
- Interactive Streamlit app for data exploration
- Well-commented scripts and a summary report

---

## 📦 Requirements

- Python 3.7 or higher
- pandas
- matplotlib
- wordcloud
- streamlit
- pillow

Install all requirements with:
```powershell
pip install -r requirements.txt
```

---

## 📝 Reflection & Learnings

See `part5_documentation_reflection.py` for a summary of findings, challenges, and learnings from this project. Each script is commented for clarity and educational value.

---

## 💡 Tips & Troubleshooting

- If you encounter issues with Streamlit not being recognized, ensure your Python Scripts directory is in your PATH or use:
  ```powershell
  python -m streamlit run part4_streamlit_app.py
  ```
- All generated images are in the `images/` folder for easy access and sharing.
- For best results, run each script in order.

---

**Author:** Kira_Black 
**Date:** September 2025
