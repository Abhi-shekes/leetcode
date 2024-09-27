


class Nodes:
    def __init__(self, data) -> None:
        self.value = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_first(self, data):

        new_node = Nodes(data)

        if not self.head:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node

        self.head = new_node

    def insert_at_end(self, data):
        new_node = Nodes(data)

        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
        new_node.prev  = last_node

    def delete_node(self, key):
        current_node = self.head
        
        while current_node:
            if current_node.value == key:
                if current_node == self.head:
                    self.head = current_node.next  
                    if self.head: 
                        self.head.prev = None
                else:
                    if current_node.prev:
                        current_node.prev.next = current_node.next
                    if current_node.next:
                        current_node.next.prev = current_node.prev
                return 
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" <--> ")
            current_node = current_node.next
        print("None")

obj = DoublyLinkedList()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.display() 

obj.insert_at_first(5)
obj.display()  

obj.delete_node(20)
obj.display()  

obj.delete_node(5)
obj.display() 