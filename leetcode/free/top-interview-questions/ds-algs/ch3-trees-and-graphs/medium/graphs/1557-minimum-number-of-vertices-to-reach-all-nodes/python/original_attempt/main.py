
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        min_num_vertices_to_nodes = {}

        from_elm = 0
        to_elm = 0

        row, col = len(edges), len(edges[0])



def main():
    sol = Solution()
    n1 = 6
    edges1 = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    
    res1 = sol.findSmallestSetOfVertices(n1, edges1)

