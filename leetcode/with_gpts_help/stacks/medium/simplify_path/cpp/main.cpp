#include <iostream>
#include <vector>
#include <stack>
#include <sstream>
#include <gtest/gtest.h>

using namespace std;


/**
**Leetcode Stack Questions (Top Interview 150):**

- https://leetcode.com/studyplan/top-interview-150/

**Leetcode Problem (71. Simplify Path):**

- https://leetcode.com/problems/simplify-path/description/?envType=problem-list-v2&envId=stack

**ChatGPT solution:**

- https://chatgpt.com/share/66e7c1c7-adec-8005-b2ae-3cc974d1f280

*/

/**
Approach: Simplify Unix-style Path in C++ using Stack
    - Traverse the path, process each directory or filename,
    - Handle special cases like ".." and ".", and simplify the path

Step 1: Split the Path
    - Split the path by the delimiter "/" to get individual directories and filenames
    - Empty strings and "." are ignored, while ".." pops the last directory from the stack

Step 2: Simplify the Path
    - After processing all segments of the path, join the stack elements with a single "/"
    between them to get the simplified path

Step 3: Handle Edge Cases
    - Multiple "/" characters are treated as a single "/" character
    - A path that only contains slashes should return a single "/"
    - The root directory (/) does not change even if .. is applied to it

Time Complexity: O(n)
    - where n is the length of the input path
    - we process each character in the path once and manipulate the stack

Space Complexity: O(n)
    - we use a stack to store the directories, which can grow up to the size of the path
*/
class Solution {
public:
    string simplifyPath(string path) {
        stack<string> directories;
        stringstream ss(path);
        string directory;

        // Split the path by "/" and process each directory part
        while (getline(ss, directory, '/')) {
            if (directory == "" || directory == ".") {
                // Ignore empty and current directory segments
                continue;
            } else if (directory == "..") {
                if (!directories.empty()) {
                    // Go to parent directory if not empty
                    directories.pop();
                }
            } else {
                // Add valid directory names to the stack
                directories.push(directory);
            }
        }

        // Construct the conanical path by joining the directories in the stack
        string simplifiedPath = "";
        while (!directories.empty()) {
            simplifiedPath = "/" + directories.top() + simplifiedPath;
            directories.pop();
        }

        // If stack is empty, return root directory
        // Otherwise, return the simplified path
        return simplifiedPath.empty() ? "/" : simplifiedPath;
    }
};

TEST(SimplifyPathTest, BasicTests) {
    Solution solution;

    EXPECT_EQ(solution.simplifyPath("/home/"), "/home");
    EXPECT_EQ(solution.simplifyPath("/../"), "/");
    EXPECT_EQ(solution.simplifyPath("/home//foo/"), "/home/foo");
    EXPECT_EQ(solution.simplifyPath("/.../a/../b/c/../d/./"), "/.../b/d");
    EXPECT_EQ(solution.simplifyPath("/home/user/Documents/../Pictures"), "/home/user/Pictures");
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
