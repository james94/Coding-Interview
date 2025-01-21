# NBA Player Play Style Clustering: KNN Classifier

## Problem Statement

Implement a K-Nearest Neighbors (KNN) classifier using PyTorch to group NBA players
into similar play styles based on their comprehensive performance metrics, addressing
the evolving nature of player roles in modern basketball.

## Examples

### Example 1

**Input:**

~~~yml
Player Metrics: [Points: 22.5, Assists: 5.8, Rebounds: 7.2, 3P%: 0.38, Blocks: 1.5]
~~~

**Output:**

~~~yml
Cluster: "Versatile Forward"

Nearest Neighbors: LeBron James, Jayson Tatum
~~~

**Explanation:**

Player demonstrates well-rounded skills across multiple statistical categories

### Example 2

**Input:**

~~~yml
Player Metrics: [Points: 28.7, 3P%: 0.42, Assists: 4.5, Rebounds: 3.2, Blocks: 0.3]
~~~

**Output:**

~~~yml
Cluster: "Scoring Guard"

Nearest Neighbors: Stephen Curry, Damian Lillard
~~~

**Explanation:**

Player shows high scoring ability with perimeter shooting skills

### Example 3

**Input:**

~~~yml
Player Metrics: [Points: 12.3, Rebounds: 10.5, Blocks: 2.3, Assists: 1.2, 3P%: 0.22]
~~~

**Output:**

~~~yml
Cluster: "Defensive Center"

Nearest Neighbors: Rudy Gobert, Clint Capela
~~~

**Explanation:**

Player demonstrates strong defensive and rebounding capabilities


## Constraints


- Input Features: 5-7 performance metrics
- Number of Neighbors (k): 3-7
- Training Data Size: 200-500 player records
- Feature Types: Offensive and defensive statistics
- Normalization: Z-score standardization

## Follow-Up

1. How would you incorporate additional features like player age or physical attributes?

2. Can you modify the model to provide confidence scores for play style classification?

3. What techniques would you use to handle potential bias in player categorization?

The implementation draws insights from the search results, particularly the research showing:

- NBA players can be effectively clustered using performance metrics
- Modern basketball positions are becoming increasingly fluid
- K-Means and KNN can provide meaningful player groupings

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A