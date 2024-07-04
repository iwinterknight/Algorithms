'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
 

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true


Example 2:

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def recursive(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if isSameTree(root, subRoot):
                return True
            return recursive(root.left, subRoot) or recursive(root.right, subRoot)


        return recursive(root, subRoot)