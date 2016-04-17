from job_queue import JobQueue
import random

class MySol(JobQueue):

    def read_data(self, n, jobs):
        self.num_workers = n
        self.jobs = jobs
        self.len_jobs = len(self.jobs)

    def assign_jobs(self):
        JobQueue.assign_jobs(self)
        return (self.assigned_workers, self.start_times)

class OrgSol(JobQueue):
    def read_data(self, n, jobs):
        self.num_workers = n
        self.jobs = jobs

    def assign_jobs(self):
        JobQueue.slow_assign_jobs(self)
        return (self.assigned_workers, self.start_times)

def stress_test(tests_amount):

    my = MySol()
    ori = OrgSol()

    for test in range(tests_amount):
        n = random.randrange(1, 50)
        m = random.randrange(1, 50)
        jobs = [random.randrange(1,250) for _ in range(m)]
        print("--------NEW TEST--------")
        print("n, m: {}, {}".format(n, m))
        print("Jobs: {}".format(jobs))

        my.read_data(n, jobs[:])
        ori.read_data(n, jobs[:])

        my_sol = my.assign_jobs()
        ori_sol = ori.assign_jobs()

        print("My output: {}".format(my_sol))
        print("Or output: {}".format(ori_sol))
        assert my_sol == ori_sol

if __name__ == "__main__":
    stress_test(30)
