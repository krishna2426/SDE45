# day 2 
# PROBLEM 1 - max sub array - brute force - O(n^3)

def sub_array(arr):
    n = len(arr)
    max_sum = 0 
    for i in range(n):
        for j in range(i,n):
            current_sum = 0
            for k in range(i, j+1):
                current_sum += arr[k]
            if current_sum > max_sum:
                 max_sum = current_sum
            
    return(max_sum)
        

sub_array([1,-2,3,-1]) 

# better - O(n^2)

def sub_array(arr):
     n = len(arr)
     max_sum = arr[0]
     for i in range(n):
         current_sum = 0 
         for j in range(i,n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
             
     return(max_sum)

sub_array([1,-2,3,-1])

# most optimal O(n)
def sub_array(arr):
    current_sum = 0 
    max_sum = arr[0]
    for num in arr:
        current_sum +=num 
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return(max_sum)

sub_array([-1,-2,-3,-1])


# PROBLEM -2 Dutch National Flag
# brute-force O(NlogN)
def dutch_flag(arr):
    arr.sort()
    return arr

# O(N) solutin to Dutch flag - 2passes 

def dutch_flag(arr):
    count_0 = 0 
    count_1 = 0
    count_2 = 0 
    idx = 0
    for i in arr:
        if i == 0:
            count_0 += 1
        if i == 1:
            count_1 += 1
        if i ==2:
            count_2 += 1
    while(count_0 > 0):
        arr[idx] = 0 
        count_0 -= 1
        idx += 1
    while(count_1 > 0):
        arr[idx] = 1 
        count_1 -= 1
        idx += 1
    while(count_2 > 0):
        arr[idx] = 2 
        count_2 -= 1
        idx += 1
    return arr

    
#optimal  - 1 pass O(N)
def dutch_flag(arr):
    n = len(arr)
    low = 0 
    mid = 0 
    high = n-1
    while(mid <= high):
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid], arr[low]
            low+=1
            mid+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            
            arr[high],arr[mid] = arr[mid],arr[high]
            high -= 1
    return arr





dutch_flag([1,0,2,1,0])



# PROBLEM -3 stock buy and sell

# brute-force - O(N^2)
def stock(prices):
    max_profit = 0
    #CANT SELL BEFORE BYING DATE OR ON THE BUYING DATE 
    for i in range(0, len(prices)-1):
        for j in range(i+1, len(prices)):
            current_profit = prices[j] - prices[i]
            if current_profit > max_profit:
                max_profit = current_profit
            
    return(max_profit)

stock([5, 4, 3, 2, 1])

#optimal - single pass - O(N)

def stock(prices):
    min_prices = prices[0]
    max_profit = 0 
    for price in prices:
        if price < min_prices:
          min_prices = price
        profit = price - min_prices
        if profit > max_profit:
            max_profit = profit
    return(max_profit)
    

stock([7,1,5,3,6,4])























