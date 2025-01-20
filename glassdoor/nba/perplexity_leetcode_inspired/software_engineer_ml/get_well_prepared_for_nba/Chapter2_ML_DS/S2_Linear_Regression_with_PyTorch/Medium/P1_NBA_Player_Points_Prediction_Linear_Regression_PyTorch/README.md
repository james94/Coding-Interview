# NBA Player Points Prediction: Linear Regression with PyTorch

## Problem Statement

Implement a linear regression model using PyTorch to predict a player's points
per game based on their minutes played and previous season's performance.

## Examples

### Example 1

**Input:**

~~~yml
Minutes Played: 28.5

Previous Season Points: 16.3
~~~

**Output:**

~~~yml
Predicted Points Per Game: 19.7
~~~

**Explanation:**

Model predicts increased scoring based on increased playing time and previous performance

### Example 2

**Input:**

~~~yml
Minutes Played: 22.0

Previous Season Points: 12.5
~~~

**Output:**

~~~yml
Predicted Points Per Game: 15.2
~~~

**Explanation:**

Model estimates modest scoring potential with limited minutes

### Example 3

**Input:**

~~~yml
Minutes Played: 35.6

Previous Season Points: 22.8
~~~

**Output:**

~~~yml
Predicted Points Per Game: 25.4
~~~

**Explanation:**

Model predicts high scoring potential with significant playing time


## Constraints


- Input Features: 2 (Minutes Played, Previous Season Points)
- Training Data Size: 50-500 player records
- Minutes Played Range: 10-40 minutes
- Previous Season Points Range: 5-35 points
- Model Complexity: Single linear layer

## Follow-Up

1. How would you incorporate additional features like shooting percentage?

2. Can you modify the model to handle non-linear relationships?

3. What techniques would you use to prevent overfitting?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A