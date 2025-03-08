from typing import List

# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#15


##
# Before Coding:
##
# Data Structures & Algorithms
#
# - Graph Traversal: DFS, BFS, or other graph search algorithms.
#
# - Path Finding: Tracking and storing paths in a graph.
#
# - Directed Acyclic Graph (DAG): Understanding the properties of DAGs.
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
# Explanation of DFS Approach:
##
#
# - DFS: Explore all paths from the source node (0) to the target node (n-1)
#
# - Backtracking: Track the current path and backtrack after exploring all neighbors to avoid
#   revisiting nodes.
#
# 1. DFS Traversal:
#   - Start at node 0 with the initial path ``.
#   - For each neighbor of the current node, add the neighbor to the path and recursively explore further
#   - If the current node is the target(n-1), add the path to the result.
#   - After exploring all neighbors, backtrack by removing the last node from the path
#
# Time Complexity: O(2^n*n) in the worst case (exponential due to all possible paths)
#
# Space Complexity: O(n) for the recursion stack and path storage
#
# Edge Cases:
#   - Single-Node Graph (graph = [[]]): Returns []
#   - Direct path from source to target (ex: graph = [, []])
#

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph) - 1 # Last node (n-1)

        def dfs(node: int, path: List[int]):
            if node == target:
                result.append(list(path)) # Add a copy of the current path
                return
            
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop() # Backtrack after exploring the neighbor

        # Start DFS from node 0 with the initial path [0]
        dfs(0, [0])
        return result

def main():
    graph1 = [[1,2], [3], [3], []]
    sol = Solution()
    print(sol.allPathsSourceTarget(graph1)) # Output: [[0,1,3], [0,2,3]]

    graph2 = [[4,3,1],[3,2,4],[3],[4],[]]
    print(sol.allPathsSourceTarget(graph2)) # Output: [[0,4], [0,3,4], [0,1,3,4], [0,1,2,3,4], [0,1,4]]

if __name__ == "__main__":
    main()

