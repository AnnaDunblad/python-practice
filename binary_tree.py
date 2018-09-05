#### data structures

### binary tree ####


class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None
        self.right = None
        

class Binary_Tree:
    def __init__(self):
        self.head = None
        
    def insert_left(self, current_node, data):
        if current_node.left:
            insert_left(current_node.left) #go down to the left leave recursivly
        else:
            current_node.left = Node(data)
            
    def insert_right(self, current_node, data):
        if current_node.right:
            insert_left(current_node.right) #go down to the right leave recursivly
        else:
            current_node.left = Node(data)
            
    def print_tree_DFS(self):
        while 
        
        
        
    def print_tree_BFS(self):
        while 
        
if __name__ == "__main__":
    
    #initializing tree
    binTree = Binary_Tree()
    binTree.head = Node(0)
    left1 = binTree.insert_left(binTree.head, 1)
    left2 = binTree.insert_left(left1,2)
    