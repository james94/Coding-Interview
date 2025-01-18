# K-Means Clustering Algorithm from Scratch (Solution)

We'll approach the k-means algorithm implementation for NBA using Meta's guidelines "How to Approach Coding Problems During Your Interview".

## Before Coding

### Clarifying questions:

1. What input format should we expect for the data points?

2. Should we implement the k-means++ initialization or use random initialization?

3. Do we need to handle edge cases like empty input or k=0?

4. Should we implement a specific stopping criterion or use a fixed number of iterations?

### Potential solutions:

1. Basic k-means with random initialization

2. K-means++ with improved initialization

3. Mini-batch k-means for larger datasets

## Basic K-Means Implementation for Clarity

Python Numpy Approach: [kmeans_np.py](./python/kmeans_np.py)

Python PyTorch Approach: [kmeans_torch.py](./python/kmeans_torch.py)

Main Deployment: [main.py](./python/main.py)


<!-- C++ Python binding code. -->

### Main Function NBA Players Performance Stats

This example demonstrates how to use the KMeans class to cluster NBA players based
on their performance statistics. Heres what happens in the main() function:

1. Defines a dataset of 10 NBA players, each with three features: points per game,
assists per game, and rebounds per game.

2. The KMeans class is initialized with 3 clusters (k=3) and then fit to the NBA data.

3. The algorithm predicts cluster assignments for each player.

4. A scatter plot is created to visualize the clustering results, showing points
per game vs assists per game. Each player is colored according to their cluster,
and the centroids are marked with red X's.

5. Finally, it prints the cluster assignment for each player.

This example showcases how k-means clustering can be applied to group NBA players
based on their statistical performance, potentially identifying different
player roles or styles. The visualization helps in understanding how the
algorithm has separated the players into distinct groups based on their scoring
and assist-making abilities.

## After Coding

### Numpy Approach: Potential Improvements

1. Implement k-means++ initialization for better initial centroids

2. Add error handling for edge cases (empty input, k=0, etc).

3. Implement early stopping based on centroid movement threshold

4. Optimize distance calculations using vectorization or GPU acceleration for large datasets.

### PyTorch Approach: Advantages of Implementation

1. Uses PyTorch tensors, allowing for easy GPU acceleration if available.

2. Vectorized operations for efficient computation.

3. Works with any number of dimensions.

### PyTorch Approach: Potential Improvements

1. Implement k-means++ initialization for better initial centroids.

2. Add error handling for edge cases (empty input, k=0, etc.).

3. Implement early stopping based on a convergence threshold.

4. Use mini-batches for handling larger datasets.

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-KEMQRh8.Q6.iA7GPeIXiUw
