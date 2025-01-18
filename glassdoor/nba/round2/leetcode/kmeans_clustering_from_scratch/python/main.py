import os
import sys
import torch
import numpy as np

# from kmeans_np import KMeansNp
from kmeans_torch import KMeansTorch

import matplotlib.pyplot as plt

def main():
    # NBA player data: [ponits_per_game, assists_per_game, rebounds_per_game]
    
    # Numpy Approach
    # nba_data = np.array([
    #     [30.1, 8.5, 6.2],  # Player 1
    #     [25.7, 10.3, 7.9], # Player 2
    #     [22.3, 3.2, 11.5], # Player 3
    #     [18.6, 9.8, 4.1],  # Player 4
    #     [15.2, 1.8, 12.7], # Player 5
    #     [28.4, 6.7, 8.3],  # Player 6
    #     [21.9, 7.2, 5.8],  # Player 7
    #     [17.5, 2.3, 10.1], # Player 8
    #     [24.6, 5.1, 6.9],  # Player 9
    #     [19.8, 8.9, 3.7]   # Player 10
    # ])

    # Initialize and fit KMeans
    # kmeans = KMeansNp(k=3)
    # kmeans.fit(nba_data)

    # PyTorch Approach
    nba_data = torch.tensor([
        [30.1, 8.5, 6.2],  # Player 1
        [25.7, 10.3, 7.9], # Player 2
        [22.3, 3.2, 11.5], # Player 3
        [18.6, 9.8, 4.1],  # Player 4
        [15.2, 1.8, 12.7], # Player 5
        [28.4, 6.7, 8.3],  # Player 6
        [21.9, 7.2, 5.8],  # Player 7
        [17.5, 2.3, 10.1], # Player 8
        [24.6, 5.1, 6.9],  # Player 9
        [19.8, 8.9, 3.7]   # Player 10
    ], dtype = torch.float32)

    # Initialize and fit KMeans
    kmeans = KMeansTorch(n_clusters=3)
    kmeans.fit(nba_data)

    # Predict clusters
    labels = kmeans.predict(nba_data)

    # Visualize results
    plt.figure(figsize=(10,0))
    scatter = plt.scatter(nba_data[:, 0], nba_data[:, 1], c=labels, cmap="viridis")
    plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], marker="x", s=200, linewidths=3, color="r")
    plt.title("NBA Player Clustering")
    plt.xlabel("Points per Game")
    plt.ylabel("Assists per Game")
    plt.colorbar(scatter)
    plt.show()

    # Print cluster assignments
    for i, label in enumerate(labels):
        print(f"Player {i+1}: Cluster {label}")

if __name__ == "__main__":
    main()
