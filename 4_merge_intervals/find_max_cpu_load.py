from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on job.end
        return self.end < other.end


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)
    max_load = 0
    job_heap = []
    cur_load = 0
    for j in jobs:

        while len(job_heap) > 0 and j.start >= job_heap[0].end:
            cur_load -= job_heap[0].cpu_load
            heappop(job_heap)

        heappush(job_heap, j)
        cur_load += j.cpu_load
        max_load = max(max_load, cur_load)

    return max_load


def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
