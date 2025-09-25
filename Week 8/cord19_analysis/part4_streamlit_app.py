"""
Part 4: Streamlit Application
Displays interactive widgets, visualizations, and sample data.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

df = pd.read_csv('metadata_first_1000_cleaned.csv')

# Interactive year range slider
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (min_year, max_year))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write(f"Showing data for years: {year_range[0]} - {year_range[1]}")
st.dataframe(filtered_df.head(20))

# Show visualizations
st.subheader("Publications by Year")
st.image('publications_by_year.png')

st.subheader("Top Journals")
st.image('top_journals.png')

st.subheader("Word Cloud of Titles")
st.image('title_wordcloud.png')

st.subheader("Distribution by Source")
st.image('source_distribution.png')
