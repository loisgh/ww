import random
import heapq

def nth_smallest(count, nth):
    nums = random.sample(range(count), (count))
    heapq.heapify(nums)
    result = heapq.nsmallest(nth, nums)
    print(result[-1])

#count is number of random numbers
#nth is nth number you want returned
nth_smallest(500, 4)


