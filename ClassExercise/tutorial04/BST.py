#Define a node class that has left and  right sides
class Node:
    def __init__(self, Node_value):
        self.left = None    # left side node (leaf)
        self.right = None   # right side node (leaf)
        self.Node_value = Node_value   # actual node value
 #Define a function to insert Node_value in to the tree
    def insert(self, Node_value):
# Compare the new value with the parent node
        if self.Node_value:   # if there is a root node
            if Node_value < self.Node_value:  # if the value that we need to insert is less than root value
                if self.left is None:     # if no left side node exist
                    self.left = Node(Node_value) # create a left side node
                else:                      # otherwise (means there is an empty left node)
                    self.left.insert(Node_value)  # put that value in the left of the existing node
            elif Node_value > self.Node_value:          # do the same thing for the right side node if >
                if self.right is None:
                    self.right = Node(Node_value)
                else:
                    self.right.insert(Node_value)
        else:        # if no root exists
            self.Node_value = Node_value     # put the value in the root

# Printing the binary tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.Node_value),
        if self.right:
            self.right.PrintTree()

    def search(self, target):
        self._search(target, 0)

    def _search(self, target, counter):
        # Print the result message with searching counter
        def message(condition, counter):
            if condition:
                print("Found the target value {0} in the tree".format(target))
            else:
                print('Cannot find the target {0} value in the tree.'.format(target))

            print('Searching Counter: {0}'.format(counter))

        if self.Node_value: # Node exist
            if self.Node_value == target:
                message(True, counter)
            elif self.Node_value > target and self.left:
                # if current value is greater and left node exist, then try left node
                self.left._search(target, counter+1)
            elif self.right:
                # if current value is less and right node exist, then try right node
                self.right._search(target, counter+1)
            else:
                message(False, counter)

        else: # Node does not exist
            message(True, counter)



# Define main to make a node object and call insert and print functions
def main():
    my_BST = Node(25)   # create an object from the node class, I called it my_BST.
    my_BST.insert(19)
    my_BST.insert(28)
    my_BST.insert(13)
    my_BST.insert(9)
    my_BST.insert(30)
    my_BST.insert(17)
    my_BST.insert(26)
    my_BST.PrintTree()
    my_BST.search(0)
    my_BST.search(9)
if __name__ == "__main__":
   main()
