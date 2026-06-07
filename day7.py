
# Problem 1 - brute force - O(n^2) 1st variant

def two_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1):
            if arr[i] +arr[j] == target:
                return "Yes"
    return "No"

two_sum([2,6,5,8,11], 14) 

#2nd variant brute force 
def two_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1):
            if arr[i] + arr[j] == target:
                return {i ,j}
    return {-1, -1}
two_sum([2,6,5,8,11], 14)

#better approach  1st variant 

def two_sum(arr, target):
    mp = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in mp:
            return "Yes"
        mp[num] = i
    return "No"

# better approach 2nd variant
def two_sum(arr, target):
    mp={}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in mp:
            return [mp[complement], i]
        mp[num] =i
    return [-1,-1]

    

#optimal approach
def two_sum(arr, target):
    arr.sort()
    n = len(arr)
    left = 0
    right = n-1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target :
            return 'Yes'
        elif current_sum > target:
            right -= 1
        elif current_sum < target:
            left +=1
        else:
            return [-1,-1]
two_sum([4,7,1,8], 8)


#problem 2 - brute force - O(n^4)
def quad_sum(arr, target):
    my_set = set()
    n = len(arr)
    for i in range(n):
        for j in range(i+1):
            for k in range(j+1):
                for l in range(k+1):
                    sum = arr[i]+arr[j]+arr[k]+arr[l]
                    if sum == target:
                        temp = tuple(sorted([arr[i],arr[j],arr[k],arr[l]]))
                        my_set.add(temp)
    return list(my_set)
arr = [4,3,3,4,4,2,1,2,1,1]
quad_sum(arr, 9)                   
    
#problem -3 #brute force 
def linearSearch(nums, num):
        n = len(nums)
        # Traverse through the array
        for i in range(n):
            if nums[i] == num:
                return True
        return False

def longestConsecutive( nums):
        
    if len(nums) == 0:
        return 0
    n = len(nums)
    # Initialize the longest sequence length
    longest = 1

        # Iterate through each element in the array
    for i in range(n):
        # Current element
        x = nums[i]
        # Count of the current sequence
        cnt = 1

            # Search for consecutive numbers
        while linearSearch(nums, x + 1):
            # Move to the next number in the sequence
            x += 1
            # Increment the count of the sequence
            cnt += 1

            # Update the longest sequence length found so far
            longest = max(longest, cnt)
        return longest



































