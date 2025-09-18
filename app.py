import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st

# URL for the dataset
DATA_URL = "https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-07-16/metadata.csv"

# Function to load data from the URL and cache it
@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

# Data Loading and Pre-processing
data = load_data()

# Converting 'publish_time' to datetime objects. Invalid dates become NaT.
data['publish_time'] = pd.to_datetime(data['publish_time'], errors='coerce')

# Removing rows where the date could not be parsed
data.dropna(subset=['publish_time'], inplace=True)

# Sorting the entire DataFrame by publication time in ascending order
data.sort_values(by='publish_time', ascending=True, inplace=True)

# --- Streamlit App Layout ---
st.title("COVID-19 Data Analysis")

st.header("Dataset Preview")
st.write("Here is a preview of the 100 earliest papers in the dataset:")
st.dataframe(data.head(100))

st.header("Unique Values Analysis")
st.write("This chart shows the number of unique values for different identifier columns in the dataset.")

# i have created a dictionary with unique value counts
unique_counts = {
    'cord_uid': data['cord_uid'].nunique(),
    'title': data['title'].nunique(),
    'doi': data['doi'].nunique(),
    'pmcid': data['pmcid'].nunique(),
    'pubmed_id': data['pubmed_id'].nunique(),
    'arxiv_id': data['arxiv_id'].nunique()
}

# Converting to a pandas Series for better charting
unique_counts_series = pd.Series(unique_counts)
st.bar_chart(unique_counts_series)

st.header("Publication Sources")
st.write("This chart shows the distribution of articles from different sources.")
# counting the number of papers from each source
source_counts = data['source_x'].value_counts()
st.bar_chart(source_counts)

st.header("Publications Over Time")
st.write("This line chart shows the number of papers published over time.")

# This data will be be grouped by month, so let's group the data by month to see the trend more clearly.
#  i have created a new column for the year-month.
data['publish_month'] = data['publish_time'].dt.to_period('M')

# Counting the number of papers per month
monthly_counts = data['publish_month'].value_counts().sort_index()

# Streamlit's line_chart works best with a DataFrame where the index is the date.
st.line_chart(monthly_counts)
