# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
            
        # prefix sums in the current path
        sumFreq = {0:1}
        self.count = 0

        def dfs(root, prefixSum):
            if not root: return
            
            currentSum = prefixSum + root.val
            checkVal = currentSum - targetSum

            if checkVal in sumFreq:
                self.count += sumFreq[checkVal]
            if currentSum in sumFreq:
                sumFreq[currentSum] += 1
            else:
                sumFreq[currentSum] = 1
            
            dfs(root.left, currentSum)
            dfs(root.right, currentSum)

            sumFreq[currentSum] -= 1
        
        dfs(root, 0)
        return self.count