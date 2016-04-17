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
        index = 0      # number of processed jobs
        thread = 0     # current thread

        # handle all initially non-busy threads
        while thread < self.num_workers and index < len(self.jobs):
            finish_time = self.jobs[index]
            if finish_time == 0:
                # don't move to next thread
                self.assigned_workers[index] = thread
                self.start_times[index] = 0
                index += 1
            else:
                # all initially empty threads start processing at t=0
                self.assigned_workers[index] = thread
                self.start_times[index] = 0
                # if num workers less than num jobs
                if self.num_workers < len(self.jobs):
                    pq.heappush(queue, (finish_time, thread, 0))
                thread += 1
                index += 1

        while len(queue) != 0:
            # get next available thread
            finish, worker, start = pq.heappop(queue)
            if index < len(self.jobs):
                next_job = self.jobs[index]
                self.assigned_workers[index] = worker
                self.start_times[index] = finish
                pq.heappush(queue, (finish + next_job, worker, finish))
                index += 1

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
