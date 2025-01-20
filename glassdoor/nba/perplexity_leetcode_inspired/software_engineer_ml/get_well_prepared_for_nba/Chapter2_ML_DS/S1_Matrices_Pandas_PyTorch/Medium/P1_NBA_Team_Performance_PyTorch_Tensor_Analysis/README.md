# NBA Team Performance PyTorch Tensor Analysis

## Problem Statement

Create a PyTorch tensor to represent team performance over a season and implement basic
statistical operations that provide insights into team performance metrics.

## Examples

### Example 1

**Input:**

~~~yml
Team: Golden State Warriors

Season: 2024

Performance Metrics: [Points, Rebounds, Assists, Steals, Turnovers]

Data: [[112, 45, 28, 7, 14], [105, 42, 25, 6, 16], ...]
~~~

**Output:**

~~~python
{
  'mean_performance': tensor([108.5, 43.5, 26.5, 6.5, 15.0]),
  'max_performance': tensor([112, 45, 28, 7, 16]),
  'variance': tensor([12.25, 4.5, 4.5, 0.25, 1.0])
}
~~~

**Explanation:**

Calculates key statistical measures for team performance across multiple games.

### Example 2

**Input:**

~~~yml
Team: Los Angeles Lakers

Season: 2024

Performance Metrics: [Points Scored, Field Goal %, 3-Point %, Free Throw %]

Data: [[98, 0.45, 0.36, 0.78], [105, 0.48, 0.40, 0.82], ...]
~~~

**Output:**

~~~python
{
  'performance_trend': tensor([Increasing]),
  'consistency_score': tensor(0.85),
  'statistical_summary': {
    'mean': tensor([101.5, 0.465, 0.38, 0.80]),
    'standard_deviation': tensor([4.95, 0.02, 0.03, 0.03])
  }
}
~~~

**Explanation:**

Provides comprehensive statistical analysis of team shooting performance.

## Constraints


- Tensor dimensions: (Number of Games, Number of Metrics)
- Number of games: 1 <= x <= 82
- Number of metrics: 3 <= x <= 10
- Metric values must be float or integer types
- All input data must be non-negative

## Follow-Up

1. How would you modify the function to handle missing game data?

2. Can you implement a method to compare performance across different teams?

3. How would you extend the analysis to predict future performance?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A