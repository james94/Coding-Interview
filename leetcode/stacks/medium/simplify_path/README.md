# Hash Table: 71. Simplify Path

**Leetcode Stack Questions (Top Interview 150):**

- https://leetcode.com/studyplan/top-interview-150/

**Leetcode Problem:**

- https://leetcode.com/problems/simplify-path/description/?envType=problem-list-v2&envId=stack

**ChatGPT solution:**

- https://chatgpt.com/share/66e7c1c7-adec-8005-b2ae-3cc974d1f280

**OBJECTIVE:**

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

- A single period '.' represents the current directory.
- A double period '..' represents the previous/parent directory.
- Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
- Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:

- The path must start with a single slash '/'.
- Directories within the path must be separated by exactly one slash '/'.
- The path must not end with a slash '/', unless it is the root directory.
- The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.

Return the **simplified canonical path**.

**CONSTRAINTS:**

1 <= path.length <= 3000

path consists of English letters, digits, period '.', slash '/' or '_'.

path is a valid absolute Unix path.

**EXAMPLES:**

Example 1:

~~~bash
Input: path = "/home/"

Output: "/home"


Explanation:

The trailing slash should be removed.
~~~

Example 2:

~~~bash
Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.
~~~

Example 3:

~~~bash
Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level (the parent directory).
~~~

Example 4:

~~~bash
Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.
~~~


Example 5:

~~~bash
Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.
~~~

## Solution

~~~bash
pushd cpp
mkdir build
pushd build

cmake ..
make -j $(nproc)

popd # exit build/
popd # exit cpp
~~~

Output:

~~~bash
# pushd cpp/build
# ctest --verbose
 
UpdateCTestConfiguration  from :/home/ubuntu/src/james/Coding-Interview/leetcode/top_interview_150/stacks/medium/simplify_path/cpp/build/DartConfiguration.tcl
UpdateCTestConfiguration  from :/home/ubuntu/src/james/Coding-Interview/leetcode/top_interview_150/stacks/medium/simplify_path/cpp/build/DartConfiguration.tcl
Test project /home/ubuntu/src/james/Coding-Interview/leetcode/top_interview_150/stacks/medium/simplify_path/cpp/build
Constructing a list of tests
Done constructing a list of tests
Updating test list for fixtures
Added 0 tests to meet fixture requirements
Checking test dependency graph...
Checking test dependency graph end
test 1
    Start 1: simplify_path_tests

1: Test command: /home/ubuntu/src/james/Coding-Interview/leetcode/top_interview_150/stacks/medium/simplify_path/cpp/build/simplify_path_tests
1: Working Directory: /home/ubuntu/src/james/Coding-Interview/leetcode/top_interview_150/stacks/medium/simplify_path/cpp/build
1: Test timeout computed to be: 10000000
1: [==========] Running 1 test from 1 test suite.
1: [----------] Global test environment set-up.
1: [----------] 1 test from SimplifyPathTest
1: [ RUN      ] SimplifyPathTest.BasicTests
1: [       OK ] SimplifyPathTest.BasicTests (0 ms)
1: [----------] 1 test from SimplifyPathTest (0 ms total)
1: 
1: [----------] Global test environment tear-down
1: [==========] 1 test from 1 test suite ran. (0 ms total)
1: [  PASSED  ] 1 test.
1/1 Test #1: simplify_path_tests ..............   Passed    0.00 sec

100% tests passed, 0 tests failed out of 1

Total Test time (real) =   0.00 sec
~~~
