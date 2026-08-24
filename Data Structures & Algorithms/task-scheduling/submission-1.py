class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        queue = deque()
        time = 0

        max_heap = [n for n in count.values()]

        heapq.heapify_max(max_heap)

        while max_heap or queue:

            time += 1

            if max_heap:
                count = heapq.heappop_max(max_heap)
                count -= 1

                if count > 0:
                    queue.append([count, time + n])
            
            if queue and queue[0][1] == time:
                count, time = queue.popleft()

                heapq.heappush_max(max_heap, count)
        
        return time



        

