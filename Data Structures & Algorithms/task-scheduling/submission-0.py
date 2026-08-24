class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #count = {}
        # for task in tasks:
        #     count[task] = 1 + count.get(task, 0)

        count = Counter(tasks) 
        time = 0
        queue = deque()
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
                freq, time = queue.popleft()
                heapq.heappush_max(max_heap, freq)
        
        return time



        

