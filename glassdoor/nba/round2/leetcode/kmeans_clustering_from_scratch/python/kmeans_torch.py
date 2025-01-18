from kmeans_abstract import KMeansAbstract
import torch

# Time Complexity: O(n_clusters * n_samples * n_features * n_iterations)
    # where "n_clusters" is the number of clusters
    # "n_samples" is the number of points
    # "n_features" is the number of dimensions
    # "n_iterations" is the number of iterations

# Space Complexity: O(n_samples * n_features)
    # storing data points and centroids

class KMeansTorch(KMeansAbstract):
    def __init__(self, n_clusters=8, max_iterations=300, tol=1e-4):
        super(KMeansAbstract, self).__init__()

        self.n_clusters = n_clusters
        self.max_iters = max_iterations
        self.tol = tol
        self.centroids = None

    def fit(self, X):
        """
        we randomly initialize centroids and iteratively assign points to clusters
        and update centroids.
        """
        self.X = X
        self.n_samples, self.n_features = self.X.shape

        # Initialize centroids randomly
        rand_idx = torch.randperm(self.n_samples)[:self.n_clusters]
        self.centroids = self.X[rand_idx].clone()

        for _ in range(self.max_iters):
            # Assigns points to nearest centroids
            labels = self._assign_labels()

            # Update centroids
            new_centroids = self._update_centroids(labels)
    
            # Check for convergence: compare the change in centroids to a tol value
            if torch.all(torch.abs(new_centroids - self.centroids) < self.tol):
                break

            self.centroids = new_centroids

        return self

    def _assign_labels(self):
        """
        torch.cdist efficiently calculates distances between points and centroids, 
        torch.argmin find the nearest centroid for each point
        """
        distances = torch.cdist(self.X, self.centroids)
        labels = torch.argmin(distances, dim=1)
        return labels

    def _update_centroids(self, labels):
        """
        Update centroids by calculating the mean of points in each cluster
        """
        new_centroids = torch.stack([
            self.X[labels == k].mean(dim=0) for k in range(self.n_clusters)
        ])
        return new_centroids
    
    def predict(self, X):
        """
        assigns new points to the nearest centroid
        """
        distances = torch.cdist(X, self.centroids)
        return torch.argmin(distances, dim=1)
