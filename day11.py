
class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = None
# Problem -2 detecting a loop
def loop(head):
    fast_ptr = head
    slow_ptr = head
    while fast_ptr != None and fast_ptr.next != None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if slow_ptr == fast_ptr:
            return True
    return False
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
    # Create a loop
fifth.next = third

loop(head)

# problem 1 
class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = None

def collison(head1,head2):
    d1,d2= head1,head2
    while d1 != d2:
        d1 = head2 if d1 is None else d1.next
        d2 = head1 if d2 is None else d2.next
    return d1


# problem -3 
# Definition for singly-linked list node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        # Return new head
        return dummy.next
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# Driver code
def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next

# Creating linked list: 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
sol = Solution()
result = sol.reverseKGroup(head, k)
printList(result)
























