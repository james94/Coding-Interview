# NBA All-Star Prediction: Support Vector Machine Classifier

## Problem Statement

Design an SVM classifier using Scikit-learn to predict whether an NBA player will be
selected for the All-Star game based on their performance metrics, considering the
complex selection process involving fan, player, and coach voting.

## Examples

### Example 1

**Input:**

~~~yml
Performance Metrics: [Points per Game: 26.5, Rebounds: 7.2, Assists: 6.3, Field Goal %: 0.52, Player Efficiency Rating: 24.1]
~~~

**Output:**

~~~yml
All-Star Probability: 0.85 (85% chance of All-Star selection)
~~~

**Explanation:**

High-performance metrics across multiple categories suggest strong All-Star candidacy.

### Example 2

**Input:**

~~~yml
Performance Metrics: [Points per Game: 18.7, Rebounds: 4.5, Assists: 3.2, Field Goal %: 0.45, Player Efficiency Rating: 16.8]
~~~

**Output:**

~~~yml
All-Star Probability: 0.15 (15% chance of All-Star selection)
~~~

**Explanation:**

Lower performance metrics indicate minimal likelihood of All-Star selection.

### Example 3

**Input:**

~~~yml
Performance Metrics: [Points per Game: 22.3, Rebounds: 5.8, Assists: 4.7, Field Goal %: 0.48, Player Efficiency Rating: 20.5]
~~~

**Output:**

~~~yml
All-Star Probability: 0.45 (45% chance of All-Star selection)
~~~

**Explanation:**

Borderline performance suggests uncertain All-Star prospects


## Constraints


- Input Features: 5-7 performance metrics
- Training Data Size: 200-500 player records
- All-Star Classification: Binary (Selected/Not Selected)
- Kernel: Radial Basis Function (RBF)
- Model Complexity: SVM with probability estimation

## Follow-Up

1. How would you incorporate additional features like team performance or media popularity?

2. Can you modify the model to handle the nuanced All-Star selection process involving fan, player, and coach voting?

3. What techniques would you use to address potential class imbalance in All-Star selection?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A