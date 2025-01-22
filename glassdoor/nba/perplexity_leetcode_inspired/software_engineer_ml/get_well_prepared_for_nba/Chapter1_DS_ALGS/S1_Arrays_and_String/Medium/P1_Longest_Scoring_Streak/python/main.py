

class ScoringStreakAnalyzer:
    def longest_scoring_streak(self, scores, threshold):
        # Use a linear scan through scores, maintaining two variables
        longest_streak = 0
        current_streak = 0

        for score in scores:
            # Increment 'current_streak' when a score is above or equal to threshold
            if score >= threshold:
                current_streak += 1
                # Update 'longest_streak' whenever 'current_streak' exceeds it
                longest_streak = max(longest_streak, current_streak)
            else:
                # when score is below threshold, reset 'current_streak' to 0
                current_streak = 0

        return longest_streak

def main():
    # NBA example: LeBron James' scoring in the 2020 NBA Finals
    lebron_scores = [25, 33, 25, 28, 40, 32]
    threshold = 30

    analyzer = ScoringStreakAnalyzer()
    longest_streak = analyzer.longest_scoring_streak(lebron_scores, threshold)

    print(f"LeBron's longest scoring streak above {threshold} points: {longest_streak} games")

if __name__ == "__main__":
    main()
