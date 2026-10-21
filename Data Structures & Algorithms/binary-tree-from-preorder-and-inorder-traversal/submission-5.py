# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        pre = 0
        def build(l, r):
            nonlocal pre
            if l > r:
                return None
            root = TreeNode(preorder[pre])
            pre += 1
            mid = idx[root.val]#中间的root返回，然后mid-1/mid+1去左边和右边；
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root
        return build(0, len(inorder) - 1)
        #最左边和最右边的l和r分别一直都是0和(len(inorder)-1)