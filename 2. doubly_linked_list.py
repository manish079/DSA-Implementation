
# Only difference is one more pointer used that is prev
# It helps it iterate over list in both foreword and backward direction
# Node class to represent each node in doubly linked list
# where first node prev will contain None and last node next will contain None
# insertion and deletion are faster in doubly linked list as we can access previous node directly using prev pointer
# Anywhere where we are see back <-> foreword, Undo <-> Redo functionality we can use doubly linked list

# Node class to represent each node linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SingleLinkedList:
    
    def __init__(self):
        self.head = None
        # self.tail = None
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        
        if new_node is None:
            print("Memory Error")
            return
    
        if self.head is None:
            self.head = new_node
            # self.tail = new_node
            return

        # self.tail.next = new_node
        # self.tail = new_node
        
        temp = self.head     # It takes O(n) time complexity to insert at end 
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
     
    def insertAtStart(self, data):
        new_node = Node(data)
        
        if new_node is None:
            print("Memory Error")
            return

        if self.head is None:
            self.head = new_node
            return

        # insert at beginning
        new_node.next = self.head
        self.head.prev = new_node  # 1 <-> 2
        self.head = new_node
    
    def insertAtPosition(self, data, position):
        
        new_node = Node(data)
        
        if new_node is None:
            print("Memory Error")
            return

        if position <= 0:
            print("Invalid Position")
            return
        
        if position == 1:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return
        
        # find position
        temp = self.head
        
        for _ in range(position - 2): 
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next
        
        if temp is None:  # If position is greater than the length of the list
            print("Position out of bounds")
            return 
        
        new_node.next = temp.next
        new_node.prev = temp
        
        if temp.next is not None:  # temp should point next node's prev to new_node
            temp.next.prev = new_node
        temp.next = new_node
        
        
    def deleteAtStart(self):
        
        # case 1: empty list
        if self.head is None:
            return

        # case 2: single node
        if self.head.next is None:
            self.head = None
            return

        # case 3: multiple nodes
        temp = self.head
        self.head = self.head.next
        self.head.prev = None   
        temp = None  # free memory
        
    def deleteAtLast(self):
        # case 1: empty list
        if self.head is None:
            return

        # case 2: single node
        if self.head.next is None:
            self.head = None
            return
        
        # case 3: multiple nodes
        temp = self.head
        
        # I am not maintaining tail pointer into inserting nodes So i am not using here, but if tail pointer is maintained then we can directly use it.
        while temp.next.next is not None: 
            temp = temp.next
        
        to_delete = temp.next
        temp.next = None
        to_delete.prev = None
        to_delete = None
        
    def deleteAtPosition(self, position):
        
        if self.length() < position or position <= 0:
            print("Invalid Position")
            return
        
        if position == 1:
            self.deleteAtStart()
            return 
        
        temp = self.head
        for _ in range(position - 2):
            temp = temp.next  
        
        if temp.next is None:
            print("Position out of bounds")
            return
        
        to_delete = temp.next
        temp.next = temp.next.next
        
        if temp.next is not None:
            temp.next.prev = temp
        
        to_delete.prev = None
        to_delete.next = None
        to_delete = None
    
    def length(self):
        count = 0
        temp = self.head
        
        while temp is not None:
            count += 1
            temp = temp.next
        
        return count     
        
    def display(self):
        temp = self.head
        
        if temp is None:
            print("List is empty")
            return
        
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    def search(self, val):
        temp = self.head
        pos = 1
        while temp is not None:
            if temp.data == val:
                return pos
            temp = temp.next
            pos += 1
        
        return -1  # Not found

    def reverse(self):
        prev = None
        current = self.head
        
        while current is not None:
            next_ptr = current.next
            current.next = prev
            current.prev = next_ptr 
            prev = current
            current = next_ptr
            
        self.head = prev
        self.head.prev = None           
    
if __name__ == "__main__":
    sll = SingleLinkedList()
    
    sll.insertAtEnd(10)
    sll.insertAtEnd(20)
    sll.insertAtEnd(30)
    sll.insertAtEnd(40)
    sll.insertAtEnd(50)
    sll.insertAtStart(5)
    sll.insertAtPosition(25, 2)
    print("======= Linked List =======")
    sll.display()
    
    print("Length of Linked List:", sll.length())
    
    sll.deleteAtStart()
    print("======= Linked List after deleting at start =======")
    sll.display()
    sll.deleteAtLast()
    print("======= Linked List after deleting at last =======")
    sll.display()
    sll.deleteAtPosition(3)
    print("======= Linked List after deleting at position 3 =======")
    sll.display()
    pos = sll.search(30)
    if pos != -1:
        print(f"Element found at position: {pos}")
    else:
        print("Element not found in the list")

    sll.reverse()
    print("======= Linked List after reversing =======")
    sll.display()
    
    