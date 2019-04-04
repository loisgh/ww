import random
import heapq

def nth_smallest(count, nth):
    nums = random.sample(range(count), (count))
    heapq.heapify(nums)
    result = heapq.nsmallest(nth, nums)
    return result[-1]


print(nth_smallest(500, 47))




