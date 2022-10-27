#from node import Node
#Class definition for a singlrualy linked list.


from msilib.schema import Binary
from tkinter import FALSE


class Node:
    def __init__(self, data=None): #this is the formatting for the creation of nodes
        self.data = data
        self.next = None
class single_linked_list:
    head = Node() #defines our header
    tail = Node()
    def __init__(self, node=None): #this is the initilizer for our linked list
        self.head = node #stores node as head and sets the tail
        self.tail = None
        #above is the default params
    
    def printList(self): #prints the linked list
        node = self.head
        while(node != None):
            print(node.data)
            node = node.next
    
    def append(self, data_in):
        if(self.head == None):#self is what is pointing at us it works similarly to this in c 
            newNode = Node(data_in) #sets the node via calling the new node and sets the data
            self.head = newNode
        else:
            curr = self.head #current node will refrence the self.head of it 
            while(curr.next !=None): curr = curr.next
            new_node = Node(data_in)
            curr.next = new_node

    def find_mid(self): #finding the middle of a linked list using a slow and fast pointer
        slow = self.head
        fast = self.head
        while(fast.next != None):
            """the fast pointer quickly moves through list and the slow pointer movest slowly
            because fast iterates at double the speed of slow it gets to the end twice as fast when fast reaches end slow is at middle"""
            slow = slow.next
            if(fast.next.next == None):
                fast = fast.next
            else:
                fast = fast.next.next
        return print(slow.data)
    
    """Creating a binary search to operate across a linked list using nodes"""
    def binary_search(self,element):
        mid = self.find_mid() 
        if(element != mid.data and self.head.next == None):
            return False
        #checks middle value of the list
        if(element == mid.data): 
            return True
        elif(element < mid.data): #we search lower half
            mid.next = None #we want lower half of array we are at middle so we now say the middle is the end
            return binary_search(element)
        #we search upper half
        elif(element > mid.data):
            self.head = mid #the head is now set to the middle of the list
            return binary_search(element)
        



def main():
    sll =single_linked_list()
    sll.append(5)
    sll.append(6)
    sll.append(7)
    sll.append(10)
    sll.append(15)
    sll.append(17)
    sll.append(20)
    print("Prints list: ")
    sll.printList()
    print("Finds middle value: ")
    sll.find_mid()
    #we now test our binary search algorithm
    print("Looking for value in begenning")
    #sll.binary_search(6)
    print("looking for mid ->10: ")
    #sll.binary_search(10)
    print("looking for the end value: ")
    #sll.binary_search(17)
main()
