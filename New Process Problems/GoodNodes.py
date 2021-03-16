#GoodNodes.py
def goodNodes(self, root):
        
        return len(self.helper(root))
        
    def helper(self, root):
        if root:
            res = [root.val]
            l = self.helper(root.left)
            r = self.helper(root.right)
            for x in l + r:
                if x >= root.val:
                    res.append(x) 
            return res
        return []


#idea was to have a counter variable
count = 0
dfs(node, maxi):
	if not node:
		return
	if node.val >= maxi:
		count += 1
	maxi = max(maxi, node.val)
	dfs(node.left, maxi)
	dfs(node.right, maxi)

dfs(root, -float('inf'))
return count
