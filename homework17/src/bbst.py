import sys
import random
import time
import pandas as pd

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class BalancedBinarySearchTree(object):

    # Function to find a node
    def get_node(self, root, key):
        if root == None:
            return None
        if root.key == key:
            return root
        if root.key > key:
            return self.get_node(root.left, key)
        if root.key < key:
            return self.get_node(root.right, key)        

    # Function to insert a node
    def insert_node(self, root, key):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)        

df = pd.DataFrame([[0, 0, 0]], columns=['size, rows', 'duration, microsec', 'duration per item, microsec'])

rdq = 100
rds = [100, 1000, 10000, 100000]

for i in range(rdq):
    print(i)
    size = random.randint(0, len(rds)-1)
    l = random.sample(range(0, rds[size]), rds[size])
    start_time = time.time()
    tree = BalancedBinarySearchTree()
    root = None
    for num in l:
        root = tree.insert_node(root = root, key = num) 
    sd = time.time() - start_time
    sdi = sd * 1000000 / rds[size]
    df = pd.concat([df, pd.DataFrame([[rds[size], sd, sdi]], columns=['size, rows', 'duration, microsec', 'duration per item, microsec'])])
print(df.sort_values(by='duration per item, microsec', ascending=False).head(20))


print('___________________________________________________________________')
l = random.sample(range(0, 30), 30)
tree = BalancedBinarySearchTree()

root = None
for num in l:
    root = tree.insert_node(root = root, key = num) 
print("After Init: ")
tree.printHelper(root, "", True)

key = 13
root = tree.delete_node(root, key)
print("After Deletion: ")
tree.printHelper(root, "", True)

print("Find Item Node: ")
key = 12
root = tree.get_node(root, key)
tree.printHelper(root, "", True)


print('___________________________________________________________________')
print('10000 size tree')
l = random.sample(range(0, 10000), 10000)
tree = BalancedBinarySearchTree()

start_time = time.time()
root = None
for num in l:
    root = tree.insert_node(root = root, key = num) 
print(f"Init duration: {time.time() - start_time}")

start_time = time.time()
key = 13
root = tree.delete_node(root, key)
print(f"Deletion duration: {time.time() - start_time}")

start_time = time.time()
key = 12
root = tree.get_node(root, key)
print(f"Find duration: {time.time() - start_time}")