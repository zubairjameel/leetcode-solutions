# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        path = [root]          
        sumPath = [root.val]    

        while path:
            temp = path.pop()
            tempVal = sumPath.pop()

           
            if temp.left is None and temp.right is None and tempVal == targetSum:
                return True

           
            if temp.right:
                path.append(temp.right)
                sumPath.append(tempVal + temp.right.val)

           
            if temp.left:
                path.append(temp.left)
                sumPath.append(tempVal + temp.left.val)

        return False
