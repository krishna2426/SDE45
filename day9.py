
# =============================================================================
# class Node:
#    def __init__(self, new_data):
#        self.data = new_data
#        self.next = next
#     
# head = Node(10)
# head.next = Node(9)
# head.next.next = Node(11)
# 
# temp = head
# while temp is not None:
#     print(temp.data, end=' ')
#     temp = temp.next
#     
# =======================================================ver======================

# =============================================================================
# Problem 1 -reversing a linked list 
# ptimal solution - O(N), space - O(1)
# =============================================================================
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

def reverse(head):
    current = head
    previous = None
    next_node = None
    
    while current != None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    
    return previous
        
def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()
    
    
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
# print_list(head)

reverse_head = reverse(head)
print_list(reverse_head)


# Problem -2 finding middle element - brute force
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def get_length(head):
    count = 0
    current = head
    
    while current != None:
        count += 1
        current = current.next
        
    return count

def middle_element(head):
    length = get_length(head)
    mid = length // 2 +1
    temp = head
    
    while temp is not None:
        mid = mid -1
        
        if mid == 0 :
            break
        temp = temp.next
    return temp

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

middle_node = middle_element(head)
print("The middle node value is:", middle_node.data)

#optimal code - problem 2
class Node:
   def __init__(self,data):
       self.data = data
       self.next = None

def middle(head):
    slow_ptr = head
    fast_ptr = head
    
    while fast_ptr != None and fast_ptr.next != None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        
    return slow_ptr

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
middle_element = middle(head)
print("The middle node value is:", middle_element.data)
    
    
#Problem 3 - optimal , no complexity

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def merge(list1, list2):
    dummy = Node(-1)
    temp = dummy
    
    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
        
    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2
        
    return dummy.next

def print_linked_list(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()

list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

print("First sorted linked list: ", end="")
print_linked_list(list1)

print("Second sorted linked list: ", end="")
print_linked_list(list2)

merged_list =merge(list1, list2)

print("Merged sorted linked list: ", end="")
print_linked_list(merged_list)







