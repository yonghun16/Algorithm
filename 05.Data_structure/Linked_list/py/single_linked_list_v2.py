class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" → ")
            curr = curr.next
        print("None")

ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_at_head(30)
ll.print()  # 30 → 20 → 10 → None
