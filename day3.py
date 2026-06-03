
               # PROBLEM 1 - rotate by 90 degree - brute force
def transpose_matrix(matrix):
    r = len(matrix)
    c = len(matrix[0])
    transpose = [[0 for _ in range(r)] for _ in range(c)]
    # print(grid)
    
    for i in range(r):
        for j in range(c):
            transpose[j][i] = matrix[i][j]
        
    return transpose


def reverse(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
        
    return arr

def rotate(arrays):
    t_array = transpose_matrix(arrays)
    r_array = reverse(t_array)
    return r_array
    
    

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(my_matrix)
 
#OPtimal with O(1) space


def rotate(matrix):
    #inplace transpose of upper traingle 
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):# i+1 to n for upper triangle 
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for i in range(len(matrix)):
        matrix[i] = matrix[i][: : -1]
    return matrix
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(my_matrix)

# PROBLEM 2 - OPTIMAL SOLUTION - O(NLOGN) TIME

def sub_intervals(intervals):
    intervals.sort()
    result = [intervals[0]] # STUCK FOR 20 MINS HERE BECAUSE IT WAS SUPPOSED TO BE A LIST OF LIST
    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]: #overlap
            result[-1][1] = max(result[-1][1], intervals[i][1]) # [a,b] -> result[-1] [c,d] -> interval[i], result[-1][1]= a, max(b,d)
        else:
            result.append(intervals[i])
    return result



my_intervals = [[1,4],[4,5]]
sub_intervals(my_intervals)


def merge(arr1, arr2):     # Problem 3 - brute force
    result = []
    i = 0
    j = 0
    while (i < len(arr1) and len(arr2)):
        
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i +=1
        else:
            result.append(arr2[j])
            j +=1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return(result)
    



merge([1,2,3], [-3,-1,4])


#DID NOT DO WHAT I WANTED THIS CODE TO DO
def merge(arr1, arr2):
   
    while arr1[-1] > arr2[0]:
        element = arr1[-1]
        j = len(arr1) - 2
        while j >= 0 and arr1[j] > element:
            arr1[j+1] = arr1[j]
            j -= 1
        arr1[j+1] = element
        
        element = arr2[0]
        j = arr2[0]
        while j < len(arr2)-1 and arr2[j+1] < element:
            arr2[j] = arr2[j+1]
            j += 1
        arr2[j] = element
    
    return arr1, arr2

merge([-5,-2,4,5,0,0,0], [-3,1,8])

# optimal O(m+n) time space O(1)
def merge(nums1, m, nums2, n):
    i = m -1
    j = n -1
    k = m + n - 1
    
    while i >=0 and j >=0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >=0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

















