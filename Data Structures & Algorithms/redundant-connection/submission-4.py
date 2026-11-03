class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        size = [1]*(n+1)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j: return False
            if size[root_i] < size[root_j]:
                parent[root_i] = root_j
                size[root_j] += size[root_i]
            else:
                parent[root_j] = root_i
                size[root_i] += root_j
            return True
        for i, j in edges:
            if not union(i, j): return [i, j]

