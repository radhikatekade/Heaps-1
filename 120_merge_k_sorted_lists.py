# Time complexity - O(nklogk) # k lists with n elements
# Space complexity - O(k)

# Approach - Create a dummy node (curr), maintain heap, if node exists in the list start pushing it in heap. While
# heap does not get empty, pop out the top element, assign it to curr.next, move curr to next, if node.next
# exists, push elements again to heap.

from typing import Optional, List
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        heap = [] # maintaining heap
        curr = dummy

        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, id(l), l))
        
        while heap:
            val, add, MinNode = heapq.heappop(heap)
            curr.next = MinNode
            curr = curr.next
            if MinNode.next:
                heapq.heappush(heap, (MinNode.next.val, id(MinNode.next), MinNode.next))
        
        return dummy.next