import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sc


def main():
    state_data = pd.read_csv("./data.csv")
    state_data.shape
    data = state_data.iloc[:, 1:].values
    # print(state_data.head(), data)

    # state_name = []
    state_name = state_data.iloc[:, 0].values
    plt.figure(1, figsize=(10, 7))
    plt.title("Using Ward's Distance")
    dend = sc.dendrogram(sc.linkage(data, method='ward'),
                         labels=state_name)

    plt.figure(2, figsize=(10, 7))
    plt.title("Using Single Link")
    dend1 = sc.dendrogram(sc.linkage(data, method='single'), labels=state_name)

    plt.figure(3, figsize=(10, 7))
    plt.title("Using Complete Link")
    dend1 = sc.dendrogram(sc.linkage(
        data, method='complete'), labels=state_name)

    plt.figure(4, figsize=(10, 7))
    plt.title("Using Group Average")
    dend2 = sc.dendrogram(sc.linkage(
        data, method='average'), labels=state_name)

    plt.figure(5, figsize=(10, 7))
    plt.title("Using Centroid method")
    dend3 = sc.dendrogram(sc.linkage(
        data, method='centroid'), labels=state_name)

    plt.figure(6, figsize=(10, 7))
    plt.title("Using Weighted method")
    dend4 = sc.dendrogram(sc.linkage(
        data, method='weighted'), labels=state_name)

    plt.figure(7, figsize=(10, 7))
    plt.title("Using Median method")
    dend4 = sc.dendrogram(sc.linkage(data, method='median'), labels=state_name)

    # print(state_name)

    plt.show()


if __name__ == "__main__":
    main()
