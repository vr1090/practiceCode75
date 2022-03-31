class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        rank = [1] * len(isConnected)
        result = len(isConnected)
        
        def findParent(n):
            currP = n
            
            while currP != parent[currP]:
                parent[currP] = parent[parent[currP]]
                currP = parent[currP]
            
            return currP
        
        
        def union(i,j):
            pi, pj = findParent(i), findParent(j)
            
            if pi == pj:
                return 0
            
            if rank[pi] > rank[pj]:
                rank[pi]= rank[pi] + rank[pj]
                parent[pj] = pi
            else:
                rank[pj] = rank[pj] + rank[pi]
                parent[pi] = pj
                
            return 1
        
        
        for i in range(len(isConnected) ):
            for j in range( len(isConnected)):
                if isConnected[i][j] == 1:
                    unionRes = union(i,j)
                    print("hasil",i,j, unionRes, parent, rank)
                    result = result - unionRes
        
        
        return result
        