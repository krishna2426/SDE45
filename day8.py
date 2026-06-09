#subarray - contigous part of the subarray
#find the longest subarray who have a sum of three

#brute force solution 
# generate all the subaarays !
# how to generate a subarray
# =============================================================================
# def sub_Array(arr):
#     n = len(arr)
#     length = 0
#     for i in range(n):
#         for j in range(i, n):
#             sums = 0
#             for k in range(i, j):
#                 sums += arr[k]
#                 if sums == k :
#                     length = max(length, j-i+1)
#     return length
# 
# sub_Array([9, -3, 3, -1, 6, -5])
# =============================================================================
                
