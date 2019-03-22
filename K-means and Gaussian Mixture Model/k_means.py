# @MayankPathela
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture


def main():
    num = int(input("How many input you want to generate: "))
    gauss_num = int(input("How many Gaussians you want to generate in RxR : "))
    print("Enter weightage of each Gaussain(space seperated)")
    weightages = list(map(float, input().split()))
    m = []
    for i in range(gauss_num):
        print("Enter the x-coordinate of Gaussian", i+1, "mean")
        num1 = int(input())
        print("Enter the y-coordinate of Gaussian", i+1, "mean")
        num2 = int(input())
        m.append([num1, num2])

    for j in range(len(weightages)):
        weightages[j] = math.floor(weightages[j]*num)
    # print(m, weightages)

    x_main = []
    y_main = []
    for i in range(gauss_num):
        mean = m[i]
        cov = []
        print("Enter the Covariance of Gaussian(Space seperated)", i+1)
        cov1 = list(map(float, input().split()))
        cov.append([cov1[0], cov1[1]])
        cov.append([cov1[2], cov1[3]])
        x, y = np.random.multivariate_normal(mean, cov, weightages[i]).T
        x_main.extend(x)
        y_main.extend(y)
        # print(x, y)
    # print(x_main, y_main)
    df = pd.DataFrame({
        'x': x_main, 'y': y_main
    })
    num3 = int(input("For how many values of k you want to plot: "))
    for i in range(num3):
        k = int(input("Please Enter the value of k: "))
        colmap = {1: 'r', 2: 'g', 3: 'b', 4: 'c', 5: 'm', 6: 'y'}
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(df)
        labels = kmeans.predict(df)
        centroids = kmeans.cluster_centers_
        fig = plt.figure(1, figsize=(5, 5))
        fig.suptitle("K-Means Clustering")
        # plt.subplot(1.1)
        colors = list(map(lambda x: colmap[x+1], labels))
        # print(colors)
        plt.scatter(df['x'], df['y'], color=colors, alpha=0.5, edgecolor='c')
        for idx, centroid in enumerate(centroids):
            plt.scatter(*centroid, color=colmap[idx+1])
        plt.xlim(-4, 8)
        plt.ylim(-4, 8)
        # plt.show()

        fig = plt.figure(2, figsize=(5, 5))
        fig.suptitle("Gaussian Mixture Model")
        # plt.subplot(1.2)
        gmm = GaussianMixture(n_components=k)
        gmm.fit(df)
        labels1 = gmm.predict(df)
        df['labels1'] = labels1
        plt.scatter(df['x'], df['y'], c=labels1, cmap='viridis')
        plt.xlim(-4, 8)
        plt.ylim(-4, 8)
        plt.show()


if __name__ == "__main__":
    main()
