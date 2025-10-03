"""
Module for loading the Wine Quality Dataset.

This module provides functionality to download and load the Wine Quality Dataset from the 
UCI Machine Learning Repository. The dataset includes information about physicochemical 
tests (e.g., pH, alcohol content) and quality scores for red and white wines.

The module contains the following functionality:
- Automatically downloads the datasets if not found locally.
- Loads the red and white wine datasets into pandas DataFrames.
- Rescales the 'quality' column to start from 0 and ensures it is of integer type.

Functions
---------
load_wine_quality():
    Loads the wine quality dataset. Automatically downloads the datasets 
    if they are not found locally and returns them as pandas DataFrames.

_download_wine_quality_datasets(destination: str):
    Downloads the wine quality datasets (red and white) from the UCI repository 
    to the specified destination folder.

Examples
--------
>>> from mymodule import load_wine_quality
>>> red_wine, white_wine = load_wine_quality()
>>> print(red_wine.head())
>>> print(white_wine.head())
"""
import os
import urllib.request
import pandas as pd

def load_wine_quality():
    """
    Loads the wine quality dataset from the UCI repository. 
    If the datasets are not already downloaded,
    they will be downloaded automatically.

    Returns
    -------
    tuple of pandas.DataFrame
        A tuple containing two DataFrames:
        - The first for red wine data.
        - The second for white wine data.
    """
    # Define the local paths for the datasets
    dataset_folder = os.path.join(os.path.dirname(__file__), "data")
    red_wine_path = os.path.join(dataset_folder, "winequality-red.csv")
    white_wine_path = os.path.join(dataset_folder, "winequality-white.csv")

    # Check if the datasets exist locally; if not, download them
    if not os.path.exists(red_wine_path) or not os.path.exists(white_wine_path):
        print("Datasets not found locally. Downloading from UCI repository...")
        os.makedirs(dataset_folder, exist_ok=True)
        _download_wine_quality_datasets(dataset_folder)

    # Load the datasets into pandas DataFrames
    red_wine_df = pd.read_csv(red_wine_path, sep=";")
    white_wine_df = pd.read_csv(white_wine_path, sep=";")

    # rescale quality to start from 0
    red_wine_df["quality"] -= red_wine_df["quality"].min()
    white_wine_df["quality"] -= white_wine_df["quality"].min()

    # ensure data type for response is integer
    red_wine_df["quality"] = red_wine_df["quality"].astype(int)
    white_wine_df["quality"] = white_wine_df["quality"].astype(int)

    return red_wine_df, white_wine_df


def _download_wine_quality_datasets(destination: str):
    """
    Downloads the wine quality datasets from the UCI repository.

    Parameters
    ----------
    destination : str
        Directory where the datasets will be saved.
    """
    # UCI repository URLs
    red_wine_url = (
        "https://archive.ics.uci.edu/ml/machine-learning-databases/"
        "wine-quality/winequality-red.csv"
    )
    white_wine_url = (
        "https://archive.ics.uci.edu/ml/machine-learning-databases/"
        "wine-quality/winequality-white.csv"
    )

    # Define file paths
    red_wine_path = os.path.join(destination, "winequality-red.csv")
    white_wine_path = os.path.join(destination, "winequality-white.csv")

    # Download the datasets
    print(f"Downloading red wine dataset to {red_wine_path}...")
    urllib.request.urlretrieve(red_wine_url, red_wine_path)
    print("Red wine dataset downloaded.")

    print(f"Downloading white wine dataset to {white_wine_path}...")
    urllib.request.urlretrieve(white_wine_url, white_wine_path)
    print("White wine dataset downloaded.")
