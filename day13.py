# problem 1 rotating a linked list

class Node:
    def __init__(self , data, next= None):
        self.data = data
        self.next = None
        
def rotateRight(head, k):
    len = 1
    tail = head
    if not head or not head.next or k == 0:
        return head
    while tail.next:
        len += 1
        tail = tail.next
    if k % len == 0:
        return head
    k = k % len
    tail.next = head
    newLast = findNthNode(head, len-k)
    head = newLast.next
    newLast.next = None
    
def findNthNode(temp, k):
    cnt = 1
    while temp != None:
        if cnt == k:
            return temp
        cnt += 1
        temp = temp.next
    return temp


def copyRandomList(head):
    temp = head
    while temp:
        copyNode = Node(temp.data)
        copyNode.next = temp.next
        temp.next = copyNode
        temp = temp.next.next
        
    temp = head
    while temp:
        copyNode = temp.next
        if temp.random != None:
            copyNode.random = temp.random.next
        else:
            copyNode.random = None
        temp = temp.next.next
    
    dNode = Node(-1)
    res = dNode
    temp = head
    while temp:
        res.next = temp.next
        temp.next = temp.next.next
        res = res.next
        temp = temp.next
    return dNode.next


def threeSum(self, arr, n):
        # Sort the array
        arr.sort()
        # Store final result
        ans = []

        # First loop for first element
        for i in range(n):
            # Skip duplicates for first element
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # Two pointers
            left, right = i + 1, n - 1

            # Find pairs for current arr[i]
            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == 0:
                    ans.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return ans
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    