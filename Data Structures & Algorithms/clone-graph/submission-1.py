"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}
        def dfs(node):
            #base case, visited node:
            if node in old_to_new:
                return old_to_new[node] #if node existed, return clone
            
            #case: new node:
            #create a new Node object 'clone'
            clone = Node(node.val) #assign node value to clone
            #add it to dict as node's key
            old_to_new[node] = clone

            # explore current node's neighbors:
            for neighbor in node.neighbors:
                #assign node's neighbor relationship to clone.
                clone.neighbors.append(dfs(neighbor))
            
            return clone
    
        return dfs(node)
        