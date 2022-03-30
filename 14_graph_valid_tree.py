from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here

        edgeMap = { i:set() for i in range(n)}
        visit = set()

        for a,b in edges:
            edgeMap[a].add(b)
            edgeMap[b].add(a)

        def dfs(i, j):
            if i in visit:
                return False
            
            visit.add(i)

            for n in edgeMap[i]:
                if n == j:
                    continue
                if not dfs(n, i):
                    return False
            
            return True
            
        result = dfs(0, -1)
        print(edgeMap)
        print(visit)

        return result and len(visit)== n 
