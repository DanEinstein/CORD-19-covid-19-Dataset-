# COVID-19 Research Paper Analysis Dashboard

This project is a Streamlit web application designed to analyze and visualize the CORD-19 (COVID-19 Open Research Dataset). It provides insights into the trends, sources, and metadata of scientific literature related to COVID-19.

The application dynamically downloads the dataset, processes it, and presents several interactive visualizations to help users explore the data.

## Table of Contents
- [COVID-19 Research Paper Analysis Dashboard](#covid-19-research-paper-analysis-dashboard)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Data Source](#data-source)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation \& Setup](#installation--setup)
  - [Code Explanation](#code-explanation)
    - [Data Loading and Caching](#data-loading-and-caching)
    - [Data Pre-processing](#data-pre-processing)
    - [Visualizations](#visualizations)
  - [How to Contribute](#how-to-contribute)
- [feel free to reach out across all social platforms](#feel-free-to-reach-out-across-all-social-platforms)

## Features

*   **Dynamic Data Loading**: The application fetches the large CORD-19 dataset directly from a URL, avoiding the need to store it in the repository.
*   **Efficient Caching**: Streamlit's caching mechanism is used to prevent re-downloading the data on every app reload, ensuring a fast user experience.
*   **Dataset Preview**: Displays the 100 earliest published papers from the dataset.
*   **Unique Identifier Analysis**: A bar chart showing the count of unique values for key identifier columns like `doi`, `pmcid`, etc.
*   **Publication Source Distribution**: Visualizes the number of articles originating from different sources (e.g., PMC, Medline, WHO).
*   **Publications Over Time**: A line chart illustrating the trend of paper publications on a monthly basis.

## Data Source

The application uses the **COVID-19 Open Research Dataset (CORD-19)**. This dataset is a resource of over 1,000,000 scholarly articles, including over 400,000 with full text, about COVID-19, SARS-CoV-2, and related coronaviruses. It is curated and maintained by the Allen Institute for AI in partnership with leading research groups.

The specific file used is `metadata.csv` from the July 16, 2020 release, which is hosted on an AWS S3 bucket. The app downloads this file directly from the following URL:

`https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-07-16/metadata.csv`

## Getting Started

Follow these instructions to get a local copy of the project up and running.

### Prerequisites

You need to have Python 3.7+ and `pip` installed on your system.

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/DanEinstein/CORD-19-covid-19-Dataset-.git
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required Python packages:**
    A `requirements.txt` file should be created to list the project dependencies.
    ```
    pip install -r requirements.txt
    ```
    *(Note: If you don't have a `requirements.txt` file, you can create one with the command `pip freeze > requirements.txt` after installing the packages below manually)*
    ```sh
    pip install streamlit pandas numpy matplotlib seaborn
    ```

4.  **Run the Streamlit application:**
    ```sh
    streamlit run app.py
    ```
    Your web browser should open a new tab with the running application. The first time you run it, it will take a moment to download the dataset.

## Code Explanation

The main logic is contained within `app.py`.

### Data Loading and Caching
The `load_data()` function is responsible for fetching the `metadata.csv` file from the `DATA_URL`. It uses the `@st.cache_data` decorator, which tells Streamlit to cache the output (the DataFrame). This means the large dataset is downloaded only once, and subsequent runs of the app will use the cached data, making it significantly faster.

### Data Pre-processing
After loading, the data undergoes several cleaning steps:
1.  The `publish_time` column is converted to datetime objects. Any rows with invalid dates are discarded.
2.  The entire dataset is sorted by `publish_time` to ensure chronological order.
3.  A `publish_month` column is created to facilitate grouping the data for the time-series analysis.

### Visualizations
The app is divided into several sections, each presenting a different analysis:
- **Dataset Preview**: Uses `st.dataframe()` to show the first 100 rows of the sorted data.
- **Unique Values Analysis**: Calculates unique counts for identifier columns and displays them using `st.bar_chart()`.
- **Publication Sources**: Uses `value_counts()` on the `source_x` column and plots the result with `st.bar_chart()`.
- **Publications Over Time**: Groups the data by `publish_month`, counts the publications in each month, and visualizes the trend using `st.line_chart()`.

## How to Contribute

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss proposed changes.
# feel free to reach out across all social platforms

Author: Danson Githuka
Email: githukadanson23@gmail.com