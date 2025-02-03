# fbref-data-analysis
This football data analysis project is one of my major projects of the year, and thus has a wide range, from scraping FBRef data to creating metrics and player statistical profiles.<br>
The main output of this project is a football player stats dashboard web app using FBRef data.<br>
This repository also includes other side projects using the same FBRef data.<br>
## Phases:
* Data Scraping
* Data Cleaning
* Feature Selection
* Metric Creation
* Data Visualization
## Contents:
* Scraping Module - 2324_fbref_data_scraper.ipynb (as the name implies) covers <b>Data Scraping</b> as well as <b>data cleaning</b>, <b>feature selection</b>, and some parts of <b>metric creation</b>, with the goal of exporting a large dataset (in csv format) for use in other applications.
## Libraries:
* <b>numpy, pandas</b> - for data processing
* <b>requests, StringIO</b> - for data scraping
* <b>time</b> - delay/sleep between requests
* <b>timeit</b> - measuring speed/performance
* <b>warnings</b> - suppressing warnings
* <b>matplotlib</b> - for data visualization (in graphs)
* <b>umap</b> - dimension reduction technique used for visualization 
* <b>StandardScaler</b> from sklearn.preprocessing - scaling data to mean 0 and variance 1 (common practice for machine learning projects)
* <b>scipy.stats, distance</b> - for measuring cosine similarity (for finding similar players)
* <b>streamlit</b> - for data visualization (as a web app)

