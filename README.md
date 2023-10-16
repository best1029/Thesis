# Company Clustering Based on Online Presence

## Overview

This project was developed in response to the needs of EBID Service AG to dynamically cluster a database of companies into different economic sectors using only data extracted from their websites. The primary objective was to assess the feasibility of clustering companies into sectors based on their online presence and to determine the most effective clustering algorithm. The study involved data acquisition, data preprocessing, similarity measurement, and clustering. A gold standard dataset was created to evaluate the clustering results. 

## Table of Contents

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Challenges](#challenges)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Data Acquisition](#data-acquisition)
- [Data Preprocessing](#data-preprocessing)
- [Clustering Algorithms](#clustering-algorithms)
- [Evaluation](#evaluation)
- [Results](#results)
- [Conclusion](#conclusion)
- [Contributing](#contributing)

## Introduction

This project was initiated to investigate the possibility of clustering companies into their respective economic sectors solely based on the content extracted from their websites. It aims to utilize pattern learning techniques to create meaningful clusters while avoiding reliance on third-party data sources.

## Objectives

- Assess the feasibility of clustering companies into economic sectors based on their online presence.
- Select and implement the most effective clustering algorithm.
- Develop a gold standard dataset for evaluating clustering results.

## Challenges

The challenging aspects of this study include the acquisition and extraction of data from websites, particularly information regarding the economic sector. Some companies, especially those from different sectors but with similar themes, proved difficult to assign to clusters.

## Project Structure

- `data_acquisition`: Contains scripts and tools for collecting text data from company websites.
- `data_preprocessing`: Involves data cleaning and preparation for clustering.
- `clustering_algorithms`: Implements various clustering algorithms, including K-Means, Hierarchical Clustering, and DBSCAN.
- `evaluation`: Provides tools for evaluating the quality of the clustering results.
- `results`: Stores the clustering outcomes and insights.

## Usage

1. Begin by collecting text data from the companies' websites. Scripts in the `data_acquisition` directory can be used for this purpose.
2. Preprocess the acquired data to ensure consistency and quality (see `data_preprocessing`).
3. Apply different clustering algorithms from the `clustering_algorithms` directory.
4. Evaluate the clustering results using the tools in the `evaluation` directory.
5. Review and analyze the results in the `results` directory.

## Data Acquisition

Data was collected solely from company websites. This involved extracting text content relevant to the economic sector of the company. Specialized web scraping and data retrieval techniques were employed.

## Data Preprocessing

Data preprocessing ensured that the extracted text data was cleaned and transformed into a suitable format for clustering. This step was essential for obtaining accurate clustering results.

## Clustering Algorithms

Various clustering algorithms were implemented, allowing flexibility in the choice of method and parameters. The effectiveness of these algorithms was evaluated based on the quality of the clusters generated.

## Evaluation

A gold standard dataset was created to serve as a benchmark for evaluating the quality of the clustering results. The adjusted rand index was used as a metric to assess the consistency of the clustering with the gold standard.

## Results

The project's results and insights can be found in the `results` directory. Visualizations and summary reports help interpret the clustered economic sectors.

## Conclusion

This study demonstrated the high feasibility of clustering companies into their respective economic sectors based on text data extracted from websites, as evidenced by the highest adjusted rand index of 0.88. However, some economic sectors may be challenging to cluster, particularly when companies from different sectors share similar themes.

## Contributing

Contributions to this project are welcome. Please feel free to open issues, fork the repository, and submit pull requests to enhance functionality, add new features, or improve documentation.
