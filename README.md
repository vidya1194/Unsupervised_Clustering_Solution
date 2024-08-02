# Unsupervised Clustering Solution

## Project Overview

This project implements an unsupervised clustering solution using the k-means algorithm to group customers based on their purchasing behavior. The primary objective is to analyze and segment customers to gain insights that can drive marketing strategies.

## Project Structure

- **main.py**: The entry point of the application. It orchestrates the entire workflow of loading data, training the clustering model, and evaluating the results.
- **data/**: Contains the dataset used for clustering (`mall_customers.csv`).
- **logs/**: Stores logs generated during the execution of the application.
- **src/**: Contains the core modules:
  - **data_loading.py**: Module responsible for loading and preprocessing the dataset.
  - **train_evaluate_model.py**: Module that handles the training and evaluation of the k-means clustering model.
  - **utils.py**: Contains utility functions used across the project.

## Dependencies
Plese see the requirement.txt file

## How to Run
To execute the project, navigate to your project directory and run the main.py script. Ensure that Python is installed and accessible via your command line:

python main.py
