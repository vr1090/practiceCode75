class Codec:

    def serialize(self, root):
        res = []

        def dfs(node):
           if not node:
               res.append("N")
               return
           else:
               res.append( str(node.val) )
               dfs(node.left)
               dfs(node.right)
        
        dfs(root)
        return ",".join(res)


    def deserialize(self, data):
        values = data.s