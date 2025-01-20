# NBA Player Market Value Prediction: XGBoost Comparative Pipeline

## Problem Statement

Create a machine learning pipeline that compares XGBoost with other boosting
algorithms to predict an NBA player's market value, leveraging multiple
performance metrics and historical contract data.

## Examples

### Example 1

**Input:**

~~~yml
Player Statistics: [Points per Game: 22.5, Rebounds: 7.2, Assists: 5.8, Player Efficiency Rating: 24.1]

Seasons Played: 5
~~~

**Output:**

~~~yml
Predicted Market Value: $28,500,000

Algorithm Performance:
    XGBoost RMSE: 2.3
    Gradient Boosting RMSE: 2.7
    LightGBM RMSE: 2.5
~~~

**Explanation:**

XGBoost demonstrates superior predictive accuracy for player market value

### Example 2

**Input:**

~~~yml
Player Statistics: [Points per Game: 15.3, Rebounds: 4.5, Assists: 3.2, Player Efficiency Rating: 16.8]

Seasons Played: 3
~~~

**Output:**

~~~yml
Predicted Market Value: $12,750,000

Algorithm Performance:
    XGBoost RMSE: 1.9
    Gradient Boosting RMSE: 2.4
    LightGBM RMSE: 2.2
~~~

**Explanation:**

Modest performance metrics result in lower predicted market value

### Example 3

**Input:**

~~~yml
Player Statistics: [Points per Game: 28.7, Rebounds: 9.1, Assists: 8.3, Player Efficiency Rating: 28.5]

Seasons Played: 7
~~~

**Output:**

~~~yml
Predicted Market Value: $45,250,000

Algorithm Performance:
    XGBoost RMSE: 2.1
    Gradient Boosting RMSE: 2.6
    LightGBM RMSE: 2.4
~~~

**Explanation:**

Elite performance metrics translate to high predicted market value


## Constraints


- Input Features: 4-6 performance metrics
- Training Data Size: 200-500 player records
- Prediction Target: Player market value
- Evaluation Metric: Root Mean Squared Error (RMSE)
- Model Complexity: Default hyperparameters

## Follow-Up

1. How would you incorporate additional features like team performance or player age?

2. Can you modify the pipeline to provide confidence intervals for market value predictions?

3. What techniques would you use to handle potential bias in the training data?

The implementation draws insights from the search results, particularly the research showing:

- XGBoost has proven effective in predicting NBA player-related metrics
- Machine learning can uncover complex relationships in player valuation
- Multiple boosting algorithms can provide comparative insights into player market value

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A