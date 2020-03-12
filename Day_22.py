

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    def getHeight(self,root):
        countl=0
        countr=0
        current=root
        while current:
            countl+=1
            current = current.left
        current=root    
        while current:
            countr+=1
            current = current.right
        
        return max(countl,countr)-1

T=[3,5,2,1,4,6,7]
myTree=Solution()
root=None
for i in T:
    data=i
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       