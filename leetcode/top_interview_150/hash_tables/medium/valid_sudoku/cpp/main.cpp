#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;


/**
**Leetcode Hash Table Questions:**

- https://leetcode.com/problem-list/hash-table/

**Leetcode Problem "36. Valid Sudoku":**

- https://leetcode.com/problems/valid-sudoku/description/?envType=problem-list-v2&envId=hash-table

**ChatGPT solution:**

- https://chatgpt.com/share/66e7a8c3-4de8-8005-a0cb-6fc07bc21ae8

*/

/**
Approach: Valid Sudoku in C++ using Hash Set

We use 3 vectors of hash sets to keep track of the digits we have
seen in each row, column, and 3x3 sub-boxes.

Index Calculation:

- Row Check: we use rows[i].count(digit) to check if the digit is already in the row
- Column Check: we use cols[j].count(digit) to check if the digit is already in the column
- Sub-box Check: we calculate the box index as (i / 3) * 3 + j / 3
    - we use boxes[boxIndex].count(digit) to check if the digit is already in the 3x3 sub-box

Insertion:

- We insert the digit into the respective hash sets for each row, column, and sub-box after 

// Time Complexity: O(1)
    - Iterating through the 9x9 Sudoku board: O(n^2), where n = 9 is dimension of the board
        - Since we iterate over a fixed size board, we get O(81) = O(1)
    - Checking for duplicates: O(1) for each cell because each hash operation on those 
        - cells takes O(1) on average and since we perform a constant number of operations
        - for each cell, the overall time complexity is O(1)
// Space Complexity: O(1)
    - We use 3 hash sets for each of the 9 rows, 9 columns, and 9 sub-boxes
    - This results in a total of 27 hash sets, resulting in constant space usage
    - , which is O(1) space complexity
*/

class Solution {
public:
    bool isValidSudoku(const std::vector<std::vector<char>>& board) {
        // Hash sets to keep track of seen digits
        std::unordered_set<char> rows[9];
        std::unordered_set<char> cols[9];
        std::unordered_set<char> boxes[9];

        // Traverse the board
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char digit = board[i][j];
                if (digit == '.') {
                    continue;
                }

                // Validation #1: Check if the digit is already in the row
                if (rows[i].count(digit) > 0) {
                    return false;
                }
                rows[i].insert(digit);

                // Validation #2: Check if the digit is already in the column
                if (cols[j].count(digit) > 0) {
                    return false;
                }
                cols[j].insert(digit);

                // Validation #3: Check if the digit is already in the 3x3 sub-box
                int boxIndex = (i / 3) * 3 + j / 3;
                if (boxes[boxIndex].count(digit) > 0) {
                    return false;
                }
                boxes[boxIndex].insert(digit);
            }
        }

        return true;
    }
};

int main() {
    Solution solution;

    // Example 1
    std::vector<std::vector<char>> board1 = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
    };

    // Example 2
    std::vector<std::vector<char>> board2 = {
        {'8', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
    };

    std::cout << "Sudoku Board 1 is " << (solution.isValidSudoku(board1) ? "valid." : "invalid.") << std::endl;
    std::cout << "Sudoku Board 2 is " << (solution.isValidSudoku(board2) ? "valid." : "invalid.") << std::endl;

    return 0;
}
