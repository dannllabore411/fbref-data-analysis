# fbref-data-analysis
This football data analysis project is one of my major projects of the year, and thus has a wide range, from scraping FBRef data to creating metrics and player statistical profiles.<br>
The main output of this project is a football player stats dashboard web app using FBRef data.<br>
This repository also includes other side projects using the same FBRef data.<br>
> [!NOTE]  
> Some advanced FBRef data for certain leagues have been unavailable since ~28 January 2025.<br>
> Keep this in mind when running the 2324_fbref_data_scraper.ipynb, which was coded with the Big 8 Leagues (Big 5 ENG, ESP, FRA, GER, ITA + POR, NED, BEL) in mind.<br>
> For men's football, only the Big 5 European Leagues, MLS, Brazilian Serie A, English Championship and Italian Serie B have full data coverage.
## Contents:
* Scraping Module - 2324_fbref_data_scraper.ipynb, covers <b>data scraping</b> as well as <b>data cleaning</b>, <b>feature selection</b>, and some parts of <b>metric creation</b>, with the goal of exporting a large dataset (in csv format) for use in other applications.
* Data Visualization - 2324_big8_ui.py, UI implementation of code, to be run with <b>streamlit</b> ($ streamlit run 2324_big8_ui.py on terminal). Needs output from scraping module (2324_top_8_raw.csv) on the same folder.
* Position Clustering - 2324_big8_clusters_touch.ipynb - exploratory project where I <b>classify players by position</b> using derived %Touches metrics (proportion of touches by specific pitch zone)
* Player Similarity/Comparison - 2324_big8_compare.ipynb - exploratory project on a <b>similar player recommender</b> tool, using the concept of <b>cosine similarity</b> on FBRef data
* Feature Selection Tests - 2324_big8_selection_feature.ipynb (documentation pending)
* Women's Football Applications - essentially the same as above, but for women's leagues
## Phases:
* Data Scraping
* Data Cleaning
* Feature Selection
* Metric Creation
* Data Visualization
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

