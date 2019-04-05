import random
import heapq

def nth_smallest(count, nth):
    nums = get_range(count)
    heapq.heapify(nums)
    result = heapq.nsmallest(nth, nums)
    print(result[-1])

def get_range(count):
    return random.sample(range(count), (count))

#count is number of random numbers
#nth is nth number you want returned
nth_smallest(500, 4)


