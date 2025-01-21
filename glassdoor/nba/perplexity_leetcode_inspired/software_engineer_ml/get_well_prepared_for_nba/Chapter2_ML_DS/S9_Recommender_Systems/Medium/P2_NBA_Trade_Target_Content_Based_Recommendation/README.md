# NBA Trade Target Recommender System

## Problem Statement

Design a content-based recommender system using Scikit-learn to suggest potential trade targets
for an NBA team based on their specific needs and player characteristics.
The system should analyze player statistics, team requirements, and salary constraints
to provide relevant trade recommendations.

## Examples

### Example 1

**Input:**

~~~yml
Team Needs: [3-point shooting, rim protection]
Player Characteristics: [Age: <28, Contract: <$20M/year]
~~~

**Output:**

~~~yml
Recommended Targets: [Cam Johnson, Myles Turner, Robert Covington]
~~~

**Explanation:**

The system suggests players who excel in 3-point shooting and rim protection, fitting the age and contract criteria.


### Example 2

**Input:**

~~~yml
Team Needs: [Playmaking, perimeter defense]
Player Characteristics: [Age: <30, All-Star potential]
~~~

**Output:**

~~~yml
Recommended Targets: [Dejounte Murray, Tyrese Haliburton, Marcus Smart]
~~~

**Explanation:**

The recommendations focus on young guards with strong playmaking and defensive skills.

### Example 3

**Input:**

~~~yml
Team Needs: [Scoring, veteran leadership]
Player Characteristics: [Age: 30+, Playoff experience]
~~~

**Output:**

~~~yml
Recommended Targets: [DeMar DeRozan, Kyle Lowry, Mike Conley]
~~~

**Explanation:**

The system suggests experienced scorers with leadership qualities and playoff experience.


## Constraints


- Number of NBA Players: 300-450
- Team Needs Categories: 5-10 (e.g., scoring, defense, rebounding)
- Player Characteristics: 10-15 features (e.g., age, contract, experience)
- Salary Cap Considerations: Must be within 10% of team's available cap space
- Trade Feasibility: Consider contract length and team's long-term plans

## Follow-Up

1. How would you incorporate player chemistry and team fit into the recommendation system?

2. Can you modify the model to suggest multi-player trade packages that balance team needs?

3. What techniques would you use to keep the system updated with real-time player performance data?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A