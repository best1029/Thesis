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
The main project logic can be found in cluster/src/. splitCompoundWordsApi works as a separate API for splitting compound words since the required package was not compatible with the Python version of the main logic.

In cluster/src/
- `preProcessing`: Involves data cleaning and preparation for clustering. 
- `dataRepresentation`: Implements different approaches to representing documents as vectors.
- `similarity`: Contains implementations of different similarity measures.
- `algorithm`: Implements various clustering algorithms, including K-Means, Hierarchical Clustering, and DBSCAN.
- `evaluation`: Provides tools for evaluating the quality of the clustering results.

## Usage

1. Begin by collecting text data from the companies' websites. [Apache Nutch](https://nutch.apache.org/) has been used for this process step.
2. Preprocess the acquired data to ensure consistency and quality (see `preProcessing`).
3. Select a 'dataRepresentation' (SVD, MDS, BOW, TfIdf, ...).
4. Select a 'similarity' measure for the data (Jaccard, Cosinus, ...).
5. Apply different clustering algorithms from the `algorithm` directory.
6. Evaluate the clustering results using the tools in the `evaluation` directory.

All those steps and the results can modified with a simple webpage contained in the 'templates' directory after starting the server.

## Data Acquisition

Data was collected solely from company websites. This involved extracting the text from the main page of each company.

## Data Preprocessing

Data preprocessing ensured that the extracted text data was cleaned and transformed into a suitable format for clustering. This step was essential for obtaining accurate clustering results.

## Clustering Algorithms

Various clustering algorithms were implemented, allowing flexibility in the choice of method and parameters. The effectiveness of these algorithms was evaluated based on the quality of the clusters generated.

## Evaluation

A gold standard dataset was created to serve as a benchmark for evaluating the quality of the clustering results. Among others, the adjusted rand index was used as a metric to assess the consistency of the clustering with the gold standard.

## Conclusion

This study demonstrated the high feasibility of clustering companies into their respective economic sectors based on text data extracted from websites, as evidenced by the highest adjusted rand index of 0.88. However, some economic sectors may be challenging to cluster, particularly when companies from different sectors share similar themes.

## Contributing

Contributions to this project are welcome. Please feel free to open issues, fork the repository, and submit pull requests to enhance functionality, add new features, or improve documentation.
