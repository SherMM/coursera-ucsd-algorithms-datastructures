# python3
import heapq as pq


class JobQueue:

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        queue = []

        # number of jobs being processed
        count = 0
        # number of processed jobs
        index = 0

        # handle jobs that take 0 time to process
        while self.jobs[count] == 0:
            self.assigned_workers[count] = 0
            self.start_times[count] = 0
            count += 1
            index += 1

        # handle all initially empty threads
        for i in range(self.num_workers):
            #finish_time = self.jobs[i]
            finish_time = self.jobs[count]
            pq.heappush(queue, (finish_time, 0, i))
            count += 1

        while len(queue) != 0:
            finish, start, worker = pq.heappop(queue)
            self.assigned_workers[index] = worker
            self.start_times[index] = start
            index += 1
            # next job processing time
            if count < len(self.jobs):
                next_job = self.jobs[count]
                pq.heappush(queue, (finish + next_job, finish, worker))
                count += 1

    def slow_assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        #self.slow_assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
