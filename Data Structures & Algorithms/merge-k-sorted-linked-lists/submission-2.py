# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        minheap = []

        for i, n in enumerate(lists):
            if n:
                heapq.heappush(minheap, (n.val, i, n))
        
        res = ListNode(0)
        cur = res

        while minheap:
            val, i, node = heapq.heappop(minheap)
            cur.next = node
            cur = cur.next

            if node.next:
                node = node.next
                heapq.heappush(minheap, (node.val, i, node))
        
        return res.next