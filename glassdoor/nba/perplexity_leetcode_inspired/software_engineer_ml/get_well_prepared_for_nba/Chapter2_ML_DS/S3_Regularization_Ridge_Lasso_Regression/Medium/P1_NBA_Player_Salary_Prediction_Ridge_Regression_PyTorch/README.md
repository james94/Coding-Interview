# NBA Player Salary Prediction: Ridge Regression with PyTorch

## Problem Statement

Implement a Ridge regression model using PyTorch to predict an NBA player's
salary based on their performance metrics, incorporating L2 regularization
to prevent overfitting.

## Examples

### Example 1

**Input:**

~~~yml
Performance Metrics: [Points per Game, Rebounds, Assists, Field Goal %]

Values: [22.5, 7.2, 5.8, 0.48]
~~~

**Output:**

~~~yml
Predicted Annual Salary: $15,750,000
~~~

**Explanation:**

Model predicts salary based on comprehensive performance metrics

### Example 2

**Input:**

~~~yml
Performance Metrics: [15.3, 4.5, 3.2, 0.42]
~~~

**Output:**

~~~yml
Predicted Annual Salary: $8,250,000
~~~

**Explanation:**

Lower performance metrics result in a more modest salary prediction

### Example 3

**Input:**

~~~yml
Performance Metrics: [28.7, 9.1, 8.3, 0.52]
~~~

**Output:**

~~~yml
Predicted Annual Salary: $35,500,000
~~~

**Explanation:**

Elite performance metrics translate to a high salary prediction


## Constraints


- Input Features: 4-6 performance metrics
- Salary Range: $1,000,000 - $50,000,000
- Training Data Size: 100-500 player records
- Regularization Parameter (λ): 0.001 - 0.1
- Model Complexity: Single linear layer with Ridge regression

## Follow-Up

1. How would you incorporate additional features like player age or position?

2. Can you modify the model to handle non-linear salary relationships?

3. What techniques would you use to improve model generalization?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A