# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/submissions/

import math

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        logn = math.ceil(math.log(n, 2))
        
        self.squareparents = []
        parent = parent + [-1]
        self.squareparents.append(parent)
        
        for _ in range(1, logn+1):
            prev_parent = self.squareparents[-1]
            curr_parent = [None]*len(prev_parent)
            for i, pp in enumerate(prev_parent):
                curr_parent[i] = prev_parent[pp] if pp != -1 else -1
            self.squareparents.append(curr_parent)
            
    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0:
            kexp2 = math.floor(math.log(k, 2))
            # advance node, advance k
            k -= 2**kexp2
            node = self.squareparents[kexp2][node]
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
