# =============================================================================
# class Node:
# #    def __init__(self, new_data):
# #        self.data = new_data
# #        self.next = next
# #     
# # head = Node(10)
# # head.next = Node(9)
# # head.next.next = Node(11)
# # 
# # temp = head
# # while temp is not None:
# #     print(temp.data, end=' ')
# #     temp = temp.next
# =============================================================================

#problem 1 - optimal

class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1
        
class Solution:
    def printLL(self, head):
        while head is not None:
            print(head.data, end=" ")
            head = head.next
    def deleteN(self, head, N):
        
        dummy = Node(0, head)
        slow = dummy
        fast = dummy
        for _ in range(N + 1):
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

# Main driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3

    # Create linked list manually
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])

    # Create Solution object
    sol = Solution()

    # Delete the Nth node from the end
    head = sol.deleteN(head, N)

    # Print the modified linked list
    sol.printLL(head)

# problem -2 :

class ListNode:
    def __init__(self, val=0, next=None):
        # Value stored in the node
        self.val = val    
        # Pointer to the next node
        self.next = next  

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        temp = dummy  
        carry = 0     
        while (l1 is not None or l2 is not None) or carry:
            sum_val = 0  
            if l1 is not None:
                sum_val += l1.val
                l1 = l1.next

            if l2 is not None:
                sum_val += l2.val
                l2 = l2.next

            sum_val += carry
            carry = sum_val // 10

            
            node = ListNode(sum_val % 10)
            # Append the new node to the result list
            temp.next = node  
            # Move temp forward
            temp = temp.next  

        
        return dummy.next
def create_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return head

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

if __name__ == "__main__":
    num1 = [2, 4, 3]  # represents 342
    num2 = [5, 6, 4]  # represents 465
    l1 = create_list(num1)
    l2 = create_list(num2)

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print_list(result)  # Output: 7 -> 0 -> 8

# problem 3 delete i nO(1)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None
        
def deleting(node: Node())-> None:
    node.data = node.next.data
    node.next = node.next.next
    







































































