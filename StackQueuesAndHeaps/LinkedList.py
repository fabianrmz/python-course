
class Node():
    def __init__(self, d = None, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return ('(' + str(self.data) + ')')
        
class LinkedList:
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1 

    def find(self, d):
        current_node = self.root
        while current_node is not None:
            if current_node.data == d:
                return d
            else: 
                current_node = current_node.next_node
        return None
    
    def remove(self, d):
        current_node = self.root
        prev_node = None

        while current_node is not None:
            if current_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = current_node.next_node
                else:
                    self.root = current_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = current_node
                current_node = current_node.next_node
        return False
    def print_list(self):
        current_node = self.root
        while current_node is not None:
            print(current_node, end='=>')
            current_node = current_node.next_node
        print('None')