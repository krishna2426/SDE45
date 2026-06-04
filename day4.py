# =============================================================================
# Problem 1 - brute force - O(nlogn) time O(n) space


def duplicate(arr):
     arr.sort()
     
     
     n = len(arr)
     for i in range(n-1):
         if arr[i] == arr[i+1]:
             return arr[i]
         
arr = [1,1,3,4,2]
duplicate(arr)
# =============================================================================

#O(N) solution , both spave and time 

def duplicate(arr):
    empty_set = set()
    for i in range(len(arr)):
        if arr[i] in empty_set:
            return arr[i]
        else:
            empty_set.add(arr[i])
            
            
            
duplicate([1,2,4,5,6,7,2,9])

#O(N) time O(1) space
def duplicate(arr):
    for i in range(len(arr)+1):
        target = abs(arr[i])
        if arr[target] < 0:
            return target
        else:
            arr[target] *= -1 
            

duplicate([1,2,4,5,2,3])


#Problem -2 brute force, no extra space but O(n^2) time

def miss_repeat(arr):
    repeating = 0
    missing = 0
    for i in range(1,len(arr)+1):
        counts = arr.count(i)
        if counts == 2:
            repeating = i
        elif counts == 0:
            missing = i
        
    return [repeating, missing]
        
miss_repeat([3,4,5,1,1])




#Problem 3  -brute for O(n^2) time
def inversion(n ,arr):
    count = 0
    for i in range(n):
        for j in range(i ,n): #ensures i < j so no need to check in if statement
            if arr[i] > arr[j]:
                count +=1
        
    return count
inversion(5, [5,4,3,2,1])

#optimal O(nlogn)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_half, left_inv = merge_sort(arr[:mid])
    right_half, right_inv = merge_sort(arr[mid:])
    
    merged_arr, merge_inv = merge(left_half, right_half)
    return merged_arr, (left_inv + right_inv + merge_inv)

def merge(left, right):
    result = []
    inversions = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            inversions += len(left) - i
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return (result, inversions)

test_cases = [
    ([1, 2, 3, 4, 5], 0),       # Test 1: Already sorted (Best case)
    ([5, 4, 3, 2, 1], 10),      # Test 2: Completely reversed (Worst case)
    ([5, 3, 2, 1, 4], 7),       # Test 3: Mixed array (From the prompt)
    ([2, 4, 1, 3, 5], 3),       # Test 4: Random order
    ([2, 2, 1, 1], 4),          # Test 5: Handling duplicates
    ([42], 0),                  # Test 6: Single element (Base case)
    ([], 0)                     # Test 7: Empty array (Edge case)
]

print("--- RUNNING INVERSION TESTS ---")
for i, (arr, expected) in enumerate(test_cases):
    # We unpack the tuple. We use '_' to ignore the sorted array and keep the count.
    _, actual_inversions = merge_sort(arr)
    
    if actual_inversions == expected:
        print(f"✅ Test {i+1} PASS | Array: {arr}")
    else:
        print(f"❌ Test {i+1} FAIL | Array: {arr} | Expected: {expected}, Got: {actual_inversions}")

















