class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertion(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return 
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def deletion(self, data):
        if not self.head:
            return
        
        current_node = self.head

        if current_node.value == data:
            self.head = current_node.next
            return
        
        previous_node = None

        while current_node:
            if current_node.value == data:
                previous_node.next = current_node.next 
                return

            previous_node = current_node
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" --> ")
            current_node = current_node.next
        print("None") 


obj = LinkedList()
obj.insertion(10)
obj.insertion(20)
obj.insertion(30)
obj.display() 

obj.deletion(20)
obj.display()  

obj.deletion(10)
obj.display() 
