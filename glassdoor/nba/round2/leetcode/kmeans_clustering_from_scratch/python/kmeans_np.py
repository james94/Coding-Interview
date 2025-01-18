from kmeans_abstract import KMeansAbstract

import numpy as np

# Time Complexity: O(k * n * d * i)
    # where "k" is the number of clusters
    # "n" is the number of points
    # "d" is the number of dimensions
    # "i" is the number of iterations

# Space Complexity: O(n + k * d)
    # storing data points and centroids

class KMeansNp(KMeansAbstract):
    def __init__(self, k=3, max_iterations=100):
        super(KMeansAbstract, self).__init__()

        self.k = k
        self.max_iterations = max_iterations

    def fit(self, X):
        """
        we randomly initialize centroids and iteratively assign points to clusters
        and update centroids.
        """
        self.X = X
        self.n_samples, self.n_features = X.shape

        # Randomly initialize centroids
        self.centroids = self.X[np.random.choice(self.n_samples, self.k, replace=False)]

        for _ in range(self.max_iterations):
            # Assign points to closest centroids
            labels = self._assign_labels()

            # Update centroids
            new_centroids = self._update_centroids(labels)

            # Check for convergence: compare new and old centroids
            if np.all(self.centroids == new_centroids):
                break

            self.centroids = new_centroids
        
        return self

    def _assign_labels(self):
        """
        calculates distances between points and centroids, assigning each point 
        to the nearest centroid.
        """
        distances = np.sqrt(((self.X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)

    def _update_centroids(self, labels):
        """
        calculates new centroids as the mean of points in each cluster
        """
        new_centroids = np.array([
            self.X[labels == i].mean(axis=0) if np.sum(labels==i) > 0 else self.centroids[i] for i in range(self.k)
        ])
        return new_centroids

    def predict(self, X):
        """
        assigns new points to the nearest centroid
        """
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)
