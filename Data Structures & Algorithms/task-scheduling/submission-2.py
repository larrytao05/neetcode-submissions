from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        available = [-count for count in Counter(tasks).values()]
        heapq.heapify(available)
        cooling = deque()  # (ready time, negative remaining count)
        time = 0

        while available or cooling:
            if cooling and cooling[0][0] <= time:
                _, count = cooling.popleft()
                heapq.heappush(available, count)

            if available:
                count = heapq.heappop(available) + 1
                if count < 0:
                    cooling.append((time + n + 1, count))

            time += 1

        return time