from typing import List
from collections import deque

# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#15


##
# Before Coding:
##
# Data Structures & Algorithms
#
# - Graph Representation: Adjacency list (given in the problem)
#
# - Breadth-First Search (BFS): To explore all paths level by level
#
# - Queue: to manage the BFS traversal
#
# - Path Finding: Tracking and storing paths in a graph during traversal
#
##
# Clarifying Questions:
##
#
# 1. Are cycles allowed in the graph?
#   - No, the input is a Directed Acyclic Graph (DAG).
#
# 2. How to handle multiple paths to the same node?
#   - Each path is considered unique and must be tracked separately.
#
# 3. Are there any constraints on the number of nodes or edges?
#   - Yes, 2 <= n <= 15, where n is the number of nodes.
#
# 4. Can there be disconnected components in the graph?
#   - No, we're guaranteed a path from 0 to n-1
#
# Potential Solutions:
#
#  1. Depth First Search (DFS) with backtracking
#  2. Breadth-First Search (BFS) with path tracking
#  3. Dynamic Programming approach
#  4. A* Search algorithm (though not typically used for all-paths problems)
##
# Explanation of BFS Approach:
##
#
# 1. Initialization:
#   - Create a queue and add the initial path.
#   - Initialize an empty result list to store complete paths.
# 2. BFS Loop:
#   - While the queue is not empty.
#       a. Dequeue a path from the queue.
#       b. Get the last node in this path
# 3. Path Checking:
#   - If the last node is the target (n-1):
#       - Add the current path to the result list.
#   - Else:
#       - Create a new path by appending the neighbor
#       - Eenqueue this new path.
# 4. Return Result:
#   - After the queue is empty, return all found paths.
#
##
# After Coding
##
#
# Time Complexity: O(2^n*n), where n is the number of nodes. In the worst case, we might
#   have 2^n paths, each of length n
#
# Space Complexity: O(2^n*n) to store all paths in the worst case
#
##
# Potential Improvements:
##
#
# Early Termination: If we only need to find one path, we can return as soon as we reach
#   the target.
#
# Pruning: if we know certain nodes can't lead to the target, we can avoid exploring them.
#
# Parallelization: For very large graphs, we could potentally parallelize BFS process.
#
# Edge Cases:
#
# - Empty graph: Return an empty list
#
# - Graph with only one node: Return [] if n = 1
# 
# - No path to target: The current implementation handles this correctly (returns empty list)

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1

        # Initialize queue with starting path
        queue = deque([[0]])
        result = []

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == target:
                result.append(path)
            else:
                for neighbor in graph[node]:
                    new_path = path + [neighbor]
                    queue.append(new_path)
        return result

def main():
    graph1 = [[1,2], [3], [3], []]
    sol = Solution()
    print(sol.allPathsSourceTarget(graph1)) # Output: [[0,1,3], [0,2,3]]

    graph2 = [[4,3,1],[3,2,4],[3],[4],[]]
    print(sol.allPathsSourceTarget(graph2)) # Output: [[0,4], [0,3,4], [0,1,3,4], [0,1,2,3,4], [0,1,4]]

if __name__ == "__main__":
    main()

