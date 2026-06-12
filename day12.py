# =============================================================================
# # problem 1 brute force 
# class Node:
#     def __init__(self, data, next =None):
#         self.data = data 
#         self.next = None
# class Stack:
#   def __init__(self):
#     self.stack = []
# 
#   def push(self, element):
#     self.stack.append(element)
# 
#   def pop(self):
#     if self.isEmpty():
#       return "Stack is empty"
#     return self.stack.pop()
# 
#   def peek(self):
#     if self.isEmpty():
#       return "Stack is empty"
#     return self.stack[-1]
# 
#   def isEmpty(self):
#     return len(self.stack) == 0
# 
#   def size(self):
#     return len(self.stack)
#        
# def palindrome(head):
#     st = Stack()
#     temp = head
#     while temp:
#         st.push(temp.data)
#         temp = temp.next
#     temp = head
#     while temp:
#         if temp.data != st.pop():
#             return False
#         temp = temp.next
#     return True
#     
#     
# head = Node(1)
# head.next = Node(5)
# head.next.next = Node(2)
# head.next.next.next = Node(5)
# head.next.next.next.next = Node(1)
# palindrome(head)    
# =============================================================================
    
    
    
    
# =============================================================================
# def reverse(head):
#     current = head
#     prev = None
#     nxt = None
#     
#     while current:
#         nxt = current.next
#         current.next = prev
#         prev = current
#         current = nxt
#     return prev
# =============================================================================
        
# =============================================================================
# def palindrome(head):
#     slow = head 
#     fast = head
#     
#     
# 
# 
# =============================================================================

# problem 2 


# =============================================================================
# class Node:
#      def __init__(self, data, next =None):
#          self.data = data 
#          self.next = None
# 
# def cycle(self, head):
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         
#         if slow == fast:
#             slow = head
#             while slow != fast:
#                 slow = slow.next
#                 fast = fast.next
#             return slow
#     return None
# 
# =============================================================================

# problem -3
class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    def convertArrToLinkedList(self, arr):
        dummyNode = ListNode(-1)
        temp = dummyNode
        for i in range(len(arr)):
            temp.child = ListNode(arr[i])
            temp = temp.child
        return dummyNode.child
    def flattenLinkedList(self, head):
        arr = []
        while head is not None:
            t2 = head
            
            while t2 is not None:
                arr.append(t2.val)
                t2 = t2.child
            head = head.next
        arr.sort()
        return self.convertArrToLinkedList(arr)

# Function to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.child
    print()

# Function to print the linked list in a grid-like structure
def printOriginalLinkedList(head, depth):
    while head is not None:
        print(head.val, end="")

        ''' If child exists, recursively
         print it with indentation '''
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars for each level in the grid
        if head.next:
            print()
            for i in range(depth):
                print("| ", end="")
        
        head = head.next

if __name__ == "__main__":
    # Create a linked list with child pointers
    head = ListNode(5)
    head.child = ListNode(14)

    head.next = ListNode(10)
    head.next.child = ListNode(4)

    head.next.next = ListNode(12)
    head.next.next.child = ListNode(20)
    head.next.next.child.child = ListNode(13)

    head.next.next.next = ListNode(7)
    head.next.next.next.child = ListNode(17)

    # Print the original linked list structure
    print("Original linked list:")
    printOriginalLinkedList(head, 0)

    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to flatten the linked list
    flattened = sol.flattenLinkedList(head)
    
    # Printing the flattened linked list
    print("\nFlattened linked list: ", end="")
    printLinkedList(flattened)





















    