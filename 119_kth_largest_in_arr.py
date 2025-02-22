# Time complexity - O(nlogk)
# Space complexity - O(k)

# Approach - We have a heap which takes in only k values, everytime we add a new element in the heap, we 
# perform heapify, and when the heap has more than k values, we pop the top element. Finally return the 
# top element.

from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ls = [] # maintaining heap
        for i in range(len(nums)):
            heapq.heappush(ls, nums[i])
            if len(ls) > k:
                heapq.heappop(ls)
        return heapq.heappop(ls)