import random
import time 
#step a: iterative max algorithm
def iterative_max(numbers, k):
    nums = numbers.copy()
    #find the maximum k times
    for i in range(k):
        max_value = nums[0]
        #find the largest remaining number
        for num in nums:
            if num > max_value:
                max_value = num
        #remove the largest number
        nums.remove(max_value)
    #max_value is now the kth greatest number
    return max_value

#generate n random integers
n = 10
numbers = [random.randint(1, 100) for _ in range(n)]
#choose which greatest number we need
k = 3

#display the numbers
print('Numbers: ', numbers)
print('k =', k)

#find the kth greatest number
result = iterative_max(numbers, k)
print('With the iterative-max algorithm: ')
print('The', k,'th greatest number is ', result)

#step b: sort-based algorithm
def sort_based(numbers, k):
    nums = numbers.copy()
    nums.sort(reverse=True)
    return nums[k -1]
sort_result = sort_based(numbers, k)
print()
print('With the sort-based algorithm: ')
print('The', k, 'th greatest number is', sort_result)

#step c: median-of-medians algorithm
def median_of_medians(numbers, k):
    def select(nums, k):
        #if list only generates only one number:
        if len(nums) == 1:
            return nums[0]
        #divide the numbers into groups of 5
        groups = []
        for i in range(0, len(nums), 5):
            groups.append(nums[i:i + 5])
        #find the median of each established group
        medians = []
        for group in groups:
            group.sort()
            middle = len(group) // 2
            medians.append(group[middle])
        #find the pivot
        medians.sort()
        pivot = medians[len(medians) // 2]            
            #divide the numbers around the pivot
        lows = []
        highs = []
        pivots = []
        for number in nums:
            if number < pivot:
                lows.append(number)
            elif number > pivot:
                highs.append(number)
            else:
                pivots.append(number)
            #determine which section contains the kth smallest number
        if k <= len(lows):
            return select(lows, k)
        elif k <= len(lows) + len(pivots):
            return pivot
        else:
            new_k = k - len(lows) - len(pivots)
            return select(highs, new_k)          
        #convert kth greatest into kth smallest
    kth_smallest = len(numbers) - k + 1
    return select(numbers.copy(), kth_smallest )
#test this algorithm
median_result = median_of_medians(numbers, k)
print()
print('With the median-of-medians algorithm: ')
print('The', k, 'th greatest number is', median_result)
                
#step d: compare running times
print()
print('Running time comparison: ')
#different values of n
sizes = [100, 500, 1000, 5000, 10000]
#use the same k for every test
k = 3

for n in sizes:
    #generate random numbers
    numbers = [random.randint(1, 100000) for _ in range(n)]
    
    #time: iterative-max
    start = time.perf_counter()
    iterative_max(numbers, k)
    iterative_time = time.perf_counter() - start
    
    #time: sort-based
    start = time.perf_counter()
    sort_based(numbers, k)
    sort_time = time.perf_counter() - start
    
    #time: median-of-medians
    start = time.perf_counter()
    median_of_medians(numbers, k)
    median_time = time.perf_counter() - start
    
    #display the resultd
    print()
    print('n = ', n)
    print('Iterative-max algorithm: ', iterative_time, 'seconds')
    print('Sort-based algorithm: ', sort_time, 'seconds')
    print('Median-of-medians algorithm: ', median_time, 'seconds')