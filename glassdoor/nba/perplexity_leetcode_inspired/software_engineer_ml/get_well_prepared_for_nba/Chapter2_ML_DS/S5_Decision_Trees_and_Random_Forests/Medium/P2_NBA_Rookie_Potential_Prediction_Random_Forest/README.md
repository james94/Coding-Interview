# NBA Rookie Potential Prediction: Random Forest Model

## Problem Statement

Design a random forest model using Scikit-learn to estimate the potential of NBA
rookie players based on their college basketball statistics, predicting their likely
long-term value in the league.

## Examples

### Example 1

**Input:**

~~~yml
College Statistics: [Points per Game: 22.5, Rebounds: 7.2, Assists: 5.8, True Shooting %: 0.58, Free Throws/Minute: 0.45]
~~~

**Output:**

~~~yml
Predicted Rookie Potential Score: 0.85 (High Potential)
~~~

**Explanation:**

Strong college performance across multiple statistical categories suggests high NBA rookie potential

### Example 2

**Input:**

~~~yml
College Statistics: [Points per Game: 15.3, Rebounds: 4.5, Assists: 3.2, True Shooting %: 0.48, Free Throws/Minute: 0.30]
~~~

**Output:**

~~~yml
Predicted Rookie Potential Score: 0.35 (Low Potential)
~~~

**Explanation:**

Modest college statistics indicate limited NBA rookie success probability

### Example 3

**Input:**

~~~yml
College Statistics: [Points per Game: 18.7, Rebounds: 5.8, Assists: 4.5, True Shooting %: 0.52, Free Throws/Minute: 0.38]
~~~

**Output:**

~~~yml
Predicted Rookie Potential Score: 0.62 (Moderate Potential)
~~~

**Explanation:**

Balanced but not exceptional college performance suggests moderate NBA rookie potential


## Constraints


- Input Features: 5-7 college performance metrics
- Training Data Size: 200-500 historical player records
- Prediction Target: Rookie potential score (0-1)
- Model Complexity: 100 trees in the random forest
- Predictive Variables: Similar to those used in 1:
    - Physical attributes (height, weight)
    - College performance metrics
    - School conference performance

## Follow-Up

1. How would you incorporate non-statistical factors like team fit or player intangibles?

2. Can you modify the model to provide confidence intervals for rookie potential predictions?

3. What techniques would you use to handle potential bias in the training data?

The implementation draws insights from the search results, particularly the research showing:

- Machine learning can predict NBA draft success with moderate accuracy
- College statistics are crucial for estimating rookie potential
- Random forest models offer flexibility in handling complex predictive tasks

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A