"""
Part 3: Data Analysis and Visualization
Analyzes publication year, top journals, word frequency, and visualizes results.
"""
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv('metadata_first_1000_cleaned.csv')

# Publications by year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(year_counts.index, year_counts.values)
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.tight_layout()
plt.savefig('images/publications_by_year.png')
plt.close()

# Top journals
if 'journal' in df.columns:
    top_journals = df['journal'].value_counts().head(10)
    plt.figure(figsize=(10,6))
    top_journals.plot(kind='bar')
    plt.title('Top 10 Journals Publishing COVID-19 Research')
    plt.xlabel('Journal')
    plt.ylabel('Number of Publications')
    plt.tight_layout()
    plt.savefig('images/top_journals.png')
    plt.close()

# Word frequency in titles
if 'title' in df.columns:
    titles = df['title'].dropna().str.lower().str.cat(sep=' ')
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
    wordcloud.to_file('images/title_wordcloud.png')

# Distribution by source
if 'source_x' in df.columns:
    source_counts = df['source_x'].value_counts()
    plt.figure(figsize=(8,5))
    source_counts.plot(kind='bar')
    plt.title('Distribution of Paper Counts by Source')
    plt.xlabel('Source')
    plt.ylabel('Number of Papers')
    plt.tight_layout()
    plt.savefig('images/source_distribution.png')
    plt.close()

print('Analysis and visualizations complete. Images saved.')
