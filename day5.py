

def power(x,n):
    return x**n

power(2,-10)


# =============================================================================
# Problem -1 : search in a 2D matrix - brute force


def matrix_search(matrix, traget):
     n = len(matrix) #gives number of rows
     m = len(matrix[0]) #give number of columns 
     for i in range(n):
         for j in range(m):
             if matrix[i][j] == target:
                 return True
     return False 
     
arr =[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix_search(arr, 5)
# =============================================================================
# =============================================================================

def bin_search(nums, target):      # Better solution 
    n = len(nums) 
    low, high = 0, n-1
    while low <=high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return True
        elif target > nums[mid]:
            low = mid+ 1
        else:
            high = mid- 1
    return False

def matrix_search( matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        if matrix[i][0] <= target <= matrix[i][m-1]: # checking wether the row will have the possibility of having the element , if yes we perform binary search on it
            return bin_search(matrix[i], target)
    return False


matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
matrix_search(matrix,8)

