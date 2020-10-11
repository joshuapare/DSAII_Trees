import queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        print(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node):

        # Check if root is empty, make root if so
        if self.root is None:
            self.root = node

        else:
            currentnode = self.root

            while True:
                if node.value < currentnode.value:
                    if currentnode.left is None:
                        currentnode.left = node
                        break
                    else:
                        currentnode = currentnode.left
                elif node.value > currentnode.value:
                    if currentnode.right is None:
                        currentnode.right = node
                        break
                    else:
                        currentnode = currentnode.right

    def find(self, node):

        currentnode = self.root

        while True:
            # check current node
            # if empty
            if currentnode is None:
                print("Node not found")
                break

            # if matching value
            elif node.value == currentnode.value:
                print("Node with value %s found." % node.value)
                break

            # go to left child if less
            elif node.value < currentnode.value:
                currentnode = currentnode.left

            # go to right child if more
            elif node.value > currentnode.value:
                currentnode = currentnode.right

    def breadth_first_search(self):

        # define collection to store visited nodes
        visited = []

        # define queue to hold values during search, put root in
        q = queue.Queue()
        q.put(self.root)

        # check if node in queue is empty
        while not q.empty():
            # get node from queue
            n = q.get()

            # add value to visited
            visited.append(n.value)

            # Check left, if they exist, add them to queue
            if n.left is not None:
                q.put(n.left)

            # Check right, if they exist, add them to queue
            if n.right is not None:
                q.put(n.right)

            # remove task from queue
            q.task_done()

        return visited

    def dfs_preorder(self):

        # define collection to store visited nodes
        visited = []

        # make root the current node
        current = self.root

        def preorder_helper(node):

            # push value of current node to visited
            visited.append(node.value)

            # check if left is empty, call recursively with node if not
            if node.left is not None:
                preorder_helper(node.left)

            # check if right is empty, call recursively with node if not
            if node.right is not None:
                preorder_helper(node.right)

        # initial call with current node
        preorder_helper(current)

        # return final array of nodes
        return visited

    def dfs_postorder(self):

        # define collection to store visited nodes
        visited = []

        # make root the current node
        current = self.root

        def postorder_helper(node):

            # check if left is empty, call recursively with node if not
            if node.left is not None:
                postorder_helper(node.left)

            # check if right is empty, call recursively with node if not
            if node.right is not None:
                postorder_helper(node.right)

            # push value of current node to visited
            visited.append(node.value)

        # initial call with current node
        postorder_helper(current)

        # return final array of nodes
        return visited

    def dfs_inorder(self):

        # define collection to store visited nodes
        visited = []

        # make root the current node
        current = self.root

        def inorder_helper(node):

            # check if left is empty, call recursively with node if not
            if node.left is not None:
                inorder_helper(node.left)

            # push value of current node to visited
            visited.append(node.value)

            # check if right is empty, call recursively with node if not
            if node.right is not None:
                inorder_helper(node.right)

        # initial call with current node
        inorder_helper(current)

        # return final array of nodes
        return visited


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    bst = BinarySearchTree()

    bst.insert(Node(30))
    bst.insert(Node(14))
    bst.insert(Node(58))
    bst.insert(Node(34))
    bst.insert(Node(32))
    bst.insert(Node(87))
    bst.insert(Node(67))
    bst.insert(Node(8))
    bst.insert(Node(15))
    bst.insert(Node(46))
    bst.insert(Node(98))
    bst.insert(Node(29))
    bst.insert(Node(3))

    bst.find(Node(68))

    bfs = bst.breadth_first_search()
    dfspreorder = bst.dfs_preorder()
    dfspostorder = bst.dfs_postorder()
    dfsinorder = bst.dfs_inorder()

    print("Breadth First Search: ")
    print(bfs)
    print("Depth First Search (PreOrder): ")
    print(dfspreorder)
    print("Depth First Search (PostOrder): ")
    print(dfspostorder)
    print("Depth First Search (InOrder): ")
    print(dfsinorder)
