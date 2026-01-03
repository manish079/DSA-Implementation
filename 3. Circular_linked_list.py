
# Circular Linked List Implementation in Python
# Circular Linked List where the last node points to the first node, So there is no NULL at the end of the list.
# If only one node is present, then that node points to itself.
# Used where looping through the list is required, like in round robin scheduling, multiplayer games etc.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtEnd(self, data):
        new_node = Node(data)

        if new_node is None:
            print("Memory Error")
            return

        # Case 1: empty list
        if self.head is None:
            self.head = new_node
            new_node.next = new_node   # circular link to itself
            self.tail = new_node
            return

        new_node.next = self.tail.next   # point to head
        self.tail.next = new_node        # old tail points to new node
        self.tail = new_node             # update tail

    def insertAtStart(self, data):
        new_node = Node(data)
        
        if new_node is None:
            print("Memory Error")
            return

        if self.head is None:
            self.head = new_node
            new_node.next = new_node   # If only one node is present, then that node points to itself.
            self.tail = new_node   
            return
        
        # insert at beginning
        new_node.next = self.head
        self.tail.next = new_node  # point last node to first new node
        self.head = new_node
        
    def insertAtPosition(self, data, position):
        
        new_node = Node(data)
        
        if new_node is None:
            print("Memory Error")
            return

        if position <= 0:
            print("Invalid Position")
            return

        if  position > self.length() + 1:  # if one node then length is 1, so position can be 2 at max to insert at end
            print("Position out of bounds")
            return
        
        # insert at beginning
        if position == 1:
            new_node.next = self.head
            self.tail.next = new_node    # tail will point to this new node
            self.head = new_node
            self.tail = new_node
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
        
        if temp.next == self.head:  # if we are inserting at last position
            self.tail = new_node
        new_node.next = temp.next
        temp.next = new_node
        
    def deleteAtStart(self):
        
        # case 1: empty list
        if self.head is None:
            return

        # case 2: single node
        if self.head.next == self.head:  # self.tail.next also works
            self.head = None
            self.tail = None
            return

        # case 3: multiple nodes
        temp = self.head
        self.head = self.head.next
        self.tail.next = self.head  # last node points to new head
        temp = None  # free memory
        
    def deleteAtLast(self):
        # case 1: empty list
        if self.head is None:
            return

        # case 2: single node
        if self.head.next == self.head:  # self.tail.next also works
            self.head = None
            self.tail = None
            return
        
        # case 3: multiple nodes
        temp = self.head
        
        # I am not maintaining tail pointer into inserting nodes So i am not using here, but if tail pointer is maintained then we can directly use it.
        while temp.next.next != self.head: 
            temp = temp.next
            
        del_node = temp.next
        temp.next = self.head  # points last node to head
        self.tail = temp       # update tail
        del_node = None       # free memory
        
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
        if temp.next == self.tail:  # if we are deleting last node
            self.tail = temp
        temp.next = temp.next.next
        self.tail.next = self.head  # maintain circular nature
        
        to_delete = None
    
    def length(self):
        count = 0
        temp = self.head
        
        if self.head is None:
            return count
        
        while True:
            count += 1
            temp = temp.next
            
            if temp == self.head:
                break
        return count     
        
    # def display(self):
    #     temp = self.head
        
    #     if temp is None:
    #         print("List is empty")
    #         return
        
    #     if temp.next == self.head:  # edge case when only one node is present
    #         print(temp.data, "-> None")
    #         return
        
    #     while temp.next != self.head:  # edge case when only one node is present then separately print that node
    #         print(temp.data, end=" -> ")
    #         temp = temp.next
    #     print("None")
    
    def display(self):
        temp = self.head
        
        if temp is None:
            print("List is empty")
            return
                
        while True:   # Its works like do while loop 
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("None")
    
    def search(self, val):
        temp = self.head
        pos = 1
        
        if self.head is None:
            return count
        
        while True:
            if temp.data == val:
                return pos
            temp = temp.next
            pos += 1
            
            if temp == self.head:
                break
        return -1  # Not found

    def reverse(self):
        prev = None
        current = self.head
        next_ptr = current
        if self.head is None:
            return
        
        while True:
            next_ptr = current.next
            current.next = prev
            prev = current
            current = next_ptr
            
            if current == self.head:  # to stop infinite loop
                break
            
        self.head.next = prev  # last node points to previous node
        self.tail = self.head  # update tail
        self.head = prev      # update head
        
        print("After reverse tail point to:", self.tail.data)
        print("After reverse head point to:", self.head.data)
        
if __name__ == "__main__":
    sll = CircularLinkedList()
    
    sll.insertAtEnd(10)
    sll.insertAtEnd(20)
    sll.insertAtEnd(30)
    sll.insertAtEnd(40)
    sll.insertAtEnd(50)
    sll.insertAtStart(5)
    sll.insertAtStart(1)
    sll.insertAtPosition(25, 2)
    print("======= Linked List =======")
    sll.display()
    
    print("Length of Linked List:", sll.length())
    
    # sll.deleteAtStart()
    # print("======= Linked List after deleting at start =======")
    # sll.display()
    # sll.deleteAtLast()
    # print("======= Linked List after deleting at last =======")
    # sll.display()
    sll.deleteAtPosition(8)
    print("======= Linked List after deleting at position 3 =======")
    sll.display()
    pos = sll.search(5)
    if pos != -1:
        print(f"Element found at position: {pos}")
    else:
        print("Element not found in the list")

    sll.reverse()
    print("======= Linked List after reversing =======")
    sll.display()
    
    