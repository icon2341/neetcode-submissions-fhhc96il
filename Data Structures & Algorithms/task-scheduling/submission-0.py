from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        # [release_time, magnitude]
        timeout = deque()
        task_q = [-cnt for cnt in freq.values()]
        # max heap of magnitudes (negatives)
        heapq.heapify(task_q)

        time = 0

        while(task_q or timeout):
            time +=1
            # if there are tasks to pop
            # we want to get the largest task
            # remember all tasks in task_q are valid since they are not in timeout.
            if task_q:
                most_freq_task = heapq.heappop(task_q) + 1
                # we add one to decrease magnitude since it is negative due to max_heap

                # if there is still more of this task, put it in the cooldown
                # not the heap since everything must be cooled down n amount
                if most_freq_task != 0:
                    timeout.append([time+n, most_freq_task])

            # if we have mags in timeout
            if timeout and timeout[0][0] == time:
                # check to see if oldest of them is ready
                # add to q if so
                _, magnitude = timeout.popleft()
                heapq.heappush(task_q,magnitude)

        return time
                    






