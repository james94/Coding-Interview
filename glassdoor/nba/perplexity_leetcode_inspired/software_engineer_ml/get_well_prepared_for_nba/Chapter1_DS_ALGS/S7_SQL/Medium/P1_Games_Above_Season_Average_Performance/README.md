# Games Above Season Average Performance

## Problem Statement

Design a SQL function to retrieve all games where a specific player scored
above their season average, providing insights into their high-performance 
matches.

## Examples

### Example 1

**Input:**

~~~yml
Player: "LeBron James"

Season: 2024
~~~

**Output:**

| Game_Date | Opponent | Points_Scored | Season_Average |
|-----------|----------|--------------|---------------|
| 2024-01-15| Celtics  | 35           | 27.5          |
| 2024-02-03| Bucks    | 42           | 27.5          |

**Explanation:**

LeBron scored above his season average of 27.5 points in two games.

### Example 2

**Input:**

~~~yml
Player: "Stephen Curry"

Season: 2024
~~~

**Output:**

| Game_Date | Opponent | Points_Scored | Season_Average |
|-----------|----------|--------------|---------------|
| 2024-01-22| Lakers   | 45           | 32.3          |
| 2024-02-10| Suns     | 38           | 32.3          |

**Explanation:**

Curry exceeded his season average in multiple games.


### Example 3

**Input:**

~~~yml
Player: "Nikola Jokic"

Season: 2024
~~~

**Output:**

| Game_Date | Opponent | Points_Scored | Season_Average |
|-----------|----------|--------------|---------------|
| 2024-01-05| Rockets  | 33           | 24.6          |

**Explanation:**

Jokic had one standout game above his season average.

## Constraints


- Player must have played at least 10 games in the season
- Season year must be between 2020 and 2025
- Points scored must be between 0 and 60
- Database must have tables: `Games`, `PlayerStats`, `Players`

## Follow-Up

1. How would you modify the function to handle players with fewer than 10 games?

2. Can you optimize the query for performance with large datasets?

3. How would you extend this to include multiple statistical categories beyond points?

## References

- Perplexity AI assistance: https://www.perplexity.ai/search/i-am-interviewing-for-software-G9IVrQnbRRaYWT5TL29h3A