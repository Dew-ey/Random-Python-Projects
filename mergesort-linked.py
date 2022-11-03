# defining node class, to store each node value of linkedlist
class Node:
    # defining construtor to class
    def __init__(self, value):
        # defining item and next parameters to class
        # storing value to item
        self.item = value
        # seting next to None
        self.next = None
        
# defining SinglyLinkedList class
class singlyLinkedList:
    # defining constructor to class
    def __init__(self):
        # defining head parameter and seting to None
        self.head = None
      
    # defining push method to push new value to linked list 
    def push(self, value): 
        new_node = Node(value) 
        # if head is none creatre new node
        if self.head is None: 
            self.head = new_node 
            return
        
        curr_node = self.head 
        # looping till last node
        while curr_node.next is not None: 
            curr_node = curr_node.next
              
        # setting next of last node to new node
        curr_node.next = new_node
        
# functions for merge sort on linkedlist

# function merge to merge two Linkedlists
def merge_lists( l, r):
    
    # Base cases 
    if l == None: 
        return r 
    if r == None: 
        return l 
    
    # defining result to store head node of resultant merge list
    result = None
    
    # if a value is less than r's 
    if l.item <= r.item:
        # setting result node l
        result = l
        # merging r next to l
        result.next = merge_lists(l.next, r) 
    else:
        result = r 
        result.next = merge_lists(l, r.next)
        
    # returning result
    return result 
      
# function mergeSort to sort Linkelist using mergeSort
# input as head
def merge_sort(head):
    
    # Defining Base case
    if head == None or head.next == None:
        return head   
    # spliting linked list from middle
    # fetching the middle of the list using middle function 
    middle = find_mid(head) 
    nexttomiddle = middle.next
    
    # set the next of middle node to None 
    middle.next = None
    
    # Applying mergeSort on left list, by calling mergeSort on head
    left = merge_sort(head) 
    
    # Apply mergeSort on right list 
    right = merge_sort(nexttomiddle) 
    
    # Merge the left and right lists by calling merge function
    sorted = merge_lists(left, right)
    
    # returning sorted list
    return sorted
      
# Function Middle, to fetch middle of linkedlist
# input as head
def find_mid(head):
    if (head == None): 
        return head 
    
    #use slow and fast methodology
    slow = head 
    fast = head 
    
    # incrementing mid by one and end by two nodes
    # untill next is None
    while (fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
        
    # returning middle node        
    return slow

# function to print the linked list  
def print_list(head):
    # if head is None
    if head is None: 
        print(' ') 
        return
    
    curr_node = head 
    while curr_node:
        # printing value
        print(curr_node.item, end = " ") 
        curr_node = curr_node.next
        
    print() 
      
# main function to read list from file
def main():
    # opening file hw5.txt
    file = open("hw5-2.txt")
    
    # defining loop counter
    count = 1
    
    # reading file line by line and sorting each list
    for line in file:
        print(count,":")
        # extracting list of integers from line using list comprehension method
        # using split method of string and int method to convert each element to int
        intList = [int(ele) for ele in line.split()] 
        
        # storing int list to linked list
        # defining linked list object
        sll = singlyLinkedList()
        
        # looping to each element in list and storing in linkedlist
        for i in intList:
            sll.push(i)
            
        # printing unsorted list
        print("Unsorted linked List:")
        print_list(sll.head)
        
        # sorting linked list using mergesort
        sll.head = merge_sort(sll.head)
        # printing sorted list
        print("Sorted linked List:")
        print_list(sll.head)
        
        # incrementing counter
        count +=1
        print()
        
# Driver Code 
if __name__ == '__main__': 
    # calling function main
    main()