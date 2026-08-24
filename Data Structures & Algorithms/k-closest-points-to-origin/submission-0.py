import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # so use a heap, and we want the closest points to the origin
        # so we will have a heap of distances and we want the smallest k 
        # so we want to use a max heap, keep adding distances in, and pop the biggest values
        # whenever the len of the heap is bigger than k we'll pop 

        heap = []
        res = []

        for x, y in points:
            distance = x**2 + y**2
            
            heapq.heappush_max(heap, (distance, [x, y]))

            if len(heap) > k:
                heapq.heappop_max(heap)
        
        for distance, points in heap:
            res.append(points)


        return res