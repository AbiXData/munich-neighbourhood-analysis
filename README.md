# Analysis of Munich Neighbourhoods for New Immigrants Using Machine Learning

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abi_Tijani-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/abitijani/)
[![GitHub](https://img.shields.io/badge/GitHub-AbiXData-black?style=flat&logo=github)](https://github.com/AbiXData)

This is a repository for the Analysis of Munich Neighbourhoods for New Immigrants Using Machine Learning. All analysis was done by **Abi Tijani**.

The datasets and Google Colab notebooks used in the project are included in this repository. A GeoJSON file with geographic coordinates for all 25 Munich districts is also included as a supplementary reference file.

See link to **blog post** for a more concise report - *[Towards Data Science](#) - [Medium](#)* *(links to be added after publication)*

---

## Introduction

In January 2026, I moved to Munich, Germany as a new immigrant. One of my first questions was: *"Which neighbourhood should I settle in?"* Munich has 25 Stadtbezirke (districts), so as a new immigrant, a vital question to answer is **"What district do I settle in?"**

The aim of this project is to group Munich's 25 districts in order of desirability for new immigrants using Machine Learning and Data Visualisation techniques. I performed my analysis using the following criteria:

- **Primary Benchmarks:** Unemployment rate and Crime rate per district
- **Secondary Benchmark:** Average monthly rent for a 1-bedroom apartment per district (EUR/month)

---

## Methodology

### Python Libraries

- **Pandas** - Used for storing, cleaning and manipulating the district data. All three datasets were loaded into Pandas dataframes and merged into one final dataframe for analysis
- **NumPy** - Used for numerical operations and array handling throughout the analysis
- **GeoPandas** - Used to create a GeoDataFrame with point coordinates (latitude and longitude) for all 25 Munich districts using gpd.points_from_xy()
- **Scikit-learn** - Used for two key Machine Learning tasks: StandardScaler to normalise the data before clustering, and KMeans to apply K-Means clustering with k=4
- **Plotly Express** - Used to build all interactive charts and the district map. Charts were saved as HTML files and hosted on GitHub Pages
- **Matplotlib** - Used for early exploratory bar charts during the data analysis phase

### Project Flowchart

![Flowchart](Flowchart.png)

---

## Interactive Charts

All charts are fully interactive - hosted on GitHub Pages:

| Chart | Link |
|---|---|
| Unemployment Rate by District | [View](https://abixdata.github.io/munich-neighbourhood-analysis/Interactive_Charts/chart1_unemployment.html) |
| Average Rent by District | [View](https://abixdata.github.io/munich-neighbourhood-analysis/Interactive_Charts/chart2_rent.html) |
| Crime vs Unemployment Bubble Chart | [View](https://abixdata.github.io/munich-neighbourhood-analysis/Interactive_Charts/chart3_bubble.html) |
| Elbow Method | [View](https://abixdata.github.io/munich-neighbourhood-analysis/Interactive_Charts/chart4_elbow.html) |
| Desirability Index | [View](https://abixdata.github.io/munich-neighbourhood-analysis/Interactive_Charts/chart5_desirability.html) |
| Munich District Map | [View](https://abixdata.github.io/munich-neighbourhood-analysis/Interactive_Charts/chart6_map.html) |

---

## View Full Notebook

👉 [Open notebook on GitHub](https://github.com/AbiXData/munich-neighbourhood-analysis/blob/main/Munich_Neighbourhood_Analysis_Full.ipynb)

---

## Final Results

K-Means clustering (k=4) was used to group all 25 Munich districts to produce a final **Munich District Desirability Index.**

### Desirability Index Chart

![Munich District Desirability Index](https://abixdata.github.io/munich-neighbourhood-analysis/Interactive_Charts/chart5_desirability.html)

> For the fully interactive version: [Click here](https://abixdata.github.io/munich-neighbourhood-analysis/Interactive_Charts/chart5_desirability.html)

### Interactive District Map

> [View Interactive Munich District Map](https://abixdata.github.io/munich-neighbourhood-analysis/Interactive_Charts/chart6_map.html)

---

## About

Analysis of Munich Neighbourhoods for New Immigrants Using Machine Learning - by Abi Tijani, 2026

[LinkedIn](https://www.linkedin.com/in/abitijani/) | [GitHub](https://github.com/AbiXData)

### Topics
`python` `data-analytics` `machine-learning` `k-means` `munich` `germany` `plotly-express` `data-visualisation` `geopandas` `scikit-learn` `new-immigrants` `kmeans-clustering` `pandas` `numpy`

