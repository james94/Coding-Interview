####
#   Clarifying Questions (Before Coding)
####
#
#   1. Understand the Problem: the task is to generate all possible letter combinations
#       for a given string of digits, where each digit maps to a set of letters as seen on a
#       telephone keypad
#
#   2. Input and Output Format: input is a string of digits from 2 to 9. Output should
#       be a list of all possible letter combinations.
#
#   3. Input string can be empty or contain up to 4 digits
#
####
#   Potential Solutions
####
#
#   1. Backtracking Algorithm: suitable for generating all combinations by exploring each possible letter
#   for each digit.
#
#   2. Iterative Approach: similar to backtracking, but uses iteration instead of recursion
#
####
#   Solution Explanation
####
#
#   Step 1: Define Digit to Letter Mapping
#       - Create a dictionary that maps each digit to its corresponding letters
#
#   Step 2: Implement Backtracking
#       - Use a recursive function to generate combinations by appending each possible
#       letter for each digit to the current path
#       - Once all digits have been processed, add the current combination to the result list
#
#   Step 3: Handle Edge Cases
#       - If the input string is empty, return an empty list
#
####
#   Explanation of Data Structures & Algorithms (While Coding)
####
#
#   Backtracking Algorithm: used to systematically generate all combinations by exploring
#       each possible letter for each digit
#
#   Time Complexity: O(4^N): where N is the number of digits. This is because the maximum
#       number of letters per digit is 4.
#
#   Space Complexity: O(4^N): for storing the result list
#
####
#   Potential Improvements (After Coding)
####
#
#   1. Iterative Solution: instead of using recursion, implement an iterative solution using
#       a queue or list to sotre intermediate combinations
#
#   2. Early Exit Conditions: Check for invalid (ex: digits outside the range 2-9) and handle them appropriately
#


def letterCombinations(digits: str) -> list[str]:
    map_digits_to_letter = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    
    def backtrack(combination: str, next_digits: str) -> None:
        # If there are no more digits to check, add the current combination to the result
        if len(next_digits) == 0:
            if combination:
                result.append(combination)
            return
        
        # For each letter that the next digit can represent
        for letter in map_digits_to_letter[next_digits[0]]:
            # Append the current letter to the combination and proceed to the next digit
            backtrack(combination + letter, next_digits[1:])
    
    result = []
    if digits:
        backtrack("", digits)
    
    return result

def main():
    digits = "23"
    result = letterCombinations(digits)

    print(result)

if __name__ == "__main__":
    main()