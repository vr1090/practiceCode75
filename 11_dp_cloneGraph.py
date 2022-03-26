class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapper = {}
        
        if not node:
            return node

        def dfs(n):
            if n in mapper:
                return mapper[n]
            
            newNode = Node(n.val)
            mapper[n] = newNode
            for ne in n.neighbors:
                newNe = dfs(ne)
                newNode.neighbors.append(newNe)
            
        
            
            return newNode
        
        dfs(node)
        
        return mapper[node]