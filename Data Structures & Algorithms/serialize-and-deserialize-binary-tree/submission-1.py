import json

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # This is a copy of the question before which was 
        # convert a binary tree using inorder nad post order.
        # the only trick is that you need to convert it into a string which honestly
        # dould prob do it as an array

        nums = []

        def preorder(root):
            if(not root):
                nums.append("N")
                return None

            nums.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

            return None

        preorder(root)


        return ", ".join(nums)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split the string back into an iterator of values
        vals = iter(data.split(", "))
        
        def reconstruct():
            val = next(vals)
            
            if val == "N":
                return None
                
            # Pre-order reconstruction: Root, then Left, then Right
            node = TreeNode(int(val))
            node.left = reconstruct()
            node.right = reconstruct()
            
            return node
            
        return reconstruct()

