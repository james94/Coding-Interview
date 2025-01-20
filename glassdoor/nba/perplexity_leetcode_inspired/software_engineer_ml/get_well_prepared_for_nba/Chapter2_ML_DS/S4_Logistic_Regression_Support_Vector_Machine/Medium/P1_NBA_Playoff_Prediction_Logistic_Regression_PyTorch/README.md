# NBA Playoff Prediction: Logistic Regression Model

## Problem Statement

Implement a logistic regression model using PyTorch to classify whether an NBA team will
make the playoffs based on their mid-season statistics.

## Examples

### Example 1

**Input:**

~~~yml
Team Statistics: [Win Rate: 0.58, Points Per Game: 112, Margin of Victory: 6.5, Road Win %: 0.52]
~~~

**Output:**

~~~yml
Playoff Probability: 0.85 (85% chance of making playoffs)
~~~

**Explanation:**

Strong mid-season performance indicates high likelihood of playoff qualification.

### Example 2

**Input:**

~~~yml
Team Statistics: [Win Rate: 0.42, Points Per Game: 105, Margin of Victory: 2.3, Road Win %: 0.38]
~~~

**Output:**

~~~yml
Playoff Probability: 0.25 (25% chance of making playoffs)
~~~

**Explanation:**

Weak performance suggests low probability of playoff qualification.

### Example 3

**Input:**

~~~yml
Team Statistics: [Win Rate: 0.50, Points Per Game: 108, Margin of Victory: 4.1, Road Win %: 0.45]
~~~

**Output:**

~~~yml
Playoff Probability: 0.55 (55% chance of making playoffs)
~~~

**Explanation:**

Borderline performance indicates uncertain playoff chances


## Constraints


- Input Features: 4-6 mid-season performance metrics
- Training Data Size: 200-500 team records
- Playoff Classification: Binary (Make/Miss Playoffs)
- Model Complexity: Single linear layer with sigmoid activation

## Follow-Up

1. How would you incorporate additional features like player injuries or recent performance trends?

2. Can you modify the model to handle multi-class playoff seeding prediction?

3. What techniques would you use to improve model generalization and prevent overfitting?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A