'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]


Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(preorder, inorder):
            if not preorder or not inorder:
                return None
            item = preorder[0]
            idx = inorder.index(item)
            left_subtree = construct(preorder[1:idx+1], inorder[:idx])
            right_subtree = construct(preorder[idx+1:], inorder[idx+1:])
            return TreeNode(item, left_subtree, right_subtree)


        return construct(preorder, inorder)