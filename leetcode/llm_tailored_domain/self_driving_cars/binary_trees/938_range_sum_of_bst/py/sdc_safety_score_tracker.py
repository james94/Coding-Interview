import sdc_safety_score_tracker as sdcsst

def create_decision_tree():
    root = sdcsst.DecisionNode(10)
    root.left = sdcsst.DecisionNode(5)
    root.right = sdcsst.DecisionNode(15)
    root.left.left = sdcsst.DecisionNode(3)
    root.left.right = sdcsst.DecisionNode(7)
    root.right.right = sdcsst.DecisionNode(18)
    return root

def main():
    root = create_decision_tree()
    min_threshold = 7
    max_threshold = 15

    sdc_safety_calculator = sdcsst.SelfDrivingCarSafetyScoreTracker()
    result = sdc_safety_calculator.calculate_safety_score(root, min_threshold, max_threshold)

    print("Self-Driving Car Safety Score Calculator")
    print("========================================")
    print(f"Total SDC Safety Score for Actions within the range [{min_threshold}, {max_threshold}]: {result}")
    print("Explanation: Nodes with safety scores 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32")

if __name__ == "__main__":
    main()