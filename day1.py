# =============================================================================
# # =============================================================================
# # rows, cols = 5 ,5 
# # matrix = [[0 for i in range(cols)] for j in range(rows)]
# # #print(matrix[0][0])
# # 
# # # matrix[0][0] = 1
# # # print(matrix[0][0])
# # 
# # # =============================================================================
# # # for r in matrix:
# # #     for c in r:
# # #         if c == 0:
# # #             c +=1
# # #         
# # #         print(c, end=" ")
# # #     print()
# # # =============================================================================
# # 
# # 
# # =============================================================================
# 
# rows = []
# cols = []
# # matrix[][]= [rows][cols]
# 
# matrix = [[0 for i in range(cols)]for j in range(rows)]
# =============================================================================




# brute - force - problem 1 
matrix = [[0,1,2,0],[3,4,5,2],[1,3,5,1]]
rows = []
cols = []

for r, valr in enumerate(matrix):
    for c, valc in enumerate(valr):
        if valc == 0:
            cols.append(c)
            rows.append(r)
    
    print()
   
for i in rows:
    for j in range(len(matrix[i])):
        matrix[i][j] = 0
    
# print(matrix)
for j in cols:
    for i in range(len(matrix)):
        matrix[i][j] = 0 
print(matrix)

#problem -2 pascals triangle


def triangle(n):
    result =[]
    for i in range(n):
        row = [1]
        if i > 0:
            prev = result[-1]
            for j in range(1,i):
                row.append(prev[j-1] + prev[j])
        if i > 0:
            row.append(1)
            
        result.append(row)
    return result

triangle(5)
            
#problem -3 next_permutations
def next_permutations(arr):
    breakpoint = -1 #flag
    n = len(arr)
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            breakpoint = i 
            break
    for j in range(n-1, breakpoint, -1):
        if arr[j] > arr[breakpoint]:
            swap_index = j

    if breakpoint == -1:
        arr = arr[::-1]
    else:
        arr[swap_index], arr[breakpoint] = arr[breakpoint], arr[swap_index]
        arr[breakpoint+1:] = arr[breakpoint+1:][::-1]
        
    return arr

next_permutations([1,3,2])










