# valid parenthesis
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (ch == ')' and top == '(') or \
                   (ch == ']' and top == '[') or \
                   (ch == '}' and top == '{'):
                    continue
                else:
                    return False
        return not stack


# next greator element
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        dic = {num: i for i, num in enumerate(nums1)}
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                ans[dic[val]] = curr
            if curr in dic:
                stack.append(curr)
        return ans

#sort a stack
def insert(stack, temp):
    # Base case: if the stack is empty or temp is larger than the top element
    if not stack or stack[-1] <= temp:
        stack.append(temp)
        return
    
    # Pop the top element and recursively insert
    val = stack.pop()
    insert(stack, temp)
    
    # Push the popped element back
    stack.append(val)

def sortStack(stack):
    if stack:
        temp = stack.pop()
        sortStack(stack)
        insert(stack, temp)
