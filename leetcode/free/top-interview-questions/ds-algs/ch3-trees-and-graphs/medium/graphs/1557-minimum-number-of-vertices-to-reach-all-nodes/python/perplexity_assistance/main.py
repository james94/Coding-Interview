# Perplexity AI reference: https://www.perplexity.ai/search/can-you-solve-the-following-le-DuJjSC.9R5OMPlYJeVkC_g#22


##
# Before Coding:
##
# Data Structures & Algorithms
#
# - Directed Acyclic Graph (DAG): Understanding the properties of DAGs
# - Graph Traversal: Concepts of reachability in a graph
# - Set Operations: To keep track of nodes with incoming edges
#
##
# Clarifying Questions:
##
#
# 1. Can there be isolated nodes (nodes with no incoming or outgoing edges)?
#   - Yes, isolated nodes would be part of the solution set.
#
# 2. Is the graph guaranteed to be connected?
#   - Not necessarily; the graph could have multiple disconnected components.
#
# 3. Can there be self-loops or parallel edges?
#   - No, the problem states that all pairs (from_i, to_i) are distinct.
#
# Potential Solutions:
#
# 1. DFS/BFS Approach: Start from each node and mark all reachable nodes. (Less efficient, O(n^2) times complexity)
#
# 2. Indegree Counting: Nodes with zero indegree (no incoming edges) must be in the solution set. (Efficient, O(n) time complexity)
#
##
# Explanation of Indegree Counting Approach:
##
#
# 1. We create a seet of all nodes (0 to n-1)
#
# 2. We create a set of nodes that have incoming edges by extracting the "to" nodes from the edges list.
#
# 3. The solution set is the difference between all nodes and nodes with incoming edges. These
#   are the nodes with no incoming edges (zero indegree)
#
##
# After Coding:
##
#
# Time Complexity: O(n + e), where n is the number of nodes and e is the number of edges.
#
# Space Complexity: O(n) to store the sets of nodes
#
#
# Potential Improvements:
#
#   - Memory Optimization: If memory is a concern, we could use a bit vector instead of sets to omark nodes with incoming edges.
#   - Early Termination: If we find that the solution set size is becoming larger than half of n, we could switch to finding
#       nodes with incoming edges instead.
#
# Edge Cases:
#
#   - Graph with no edges: All nodes would be in the solution set
#   - Fully connected graph: Only the root node (if exists) would be in the solution set
#   - Graph with multiple disconnected components: Each component's "root" would be in the solution set
#

##
# Summary
##
#
# This solution efficiently finds the smallest set of vertices from which all nodes are reachable by identifying nodes with zero indegree,
#   which must be part of the solution set in a DAG
#
#

# We'll use Indegree Counting Approach
from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create a set of all nodes
        all_nodes = set(range(n))

        # Create a set of nodes with incoming edges
        nodes_with_incoming = set(to_node for _, to_node in edges)

        # The solution is the set difference: all nodes minus nodes with incoming edges
        return list(all_nodes - nodes_with_incoming)

def main():
    sol = Solution()

    # Test case 1
    n1 = 6
    edges1 = [[0,1],[0,2],[2,5],[3,4],[4,2]]

    print(sol.findSmallestSetOfVertices(n1, edges1)) # Output: [0, 3]

    # Test case 2
    n2 = 5
    edges2 = [[0,1],[2,1],[3,1],[1,4],[2,4]]

    print(sol.findSmallestSetOfVertices(n2, edges2)) # Output: [0, 2, 3]

if __name__ == "__main__":
    main()
