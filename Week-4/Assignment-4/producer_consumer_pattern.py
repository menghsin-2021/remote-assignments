import time
import threading
import queue

job_queue = queue.Queue()
for job_index in range(1, 10):  # We create 9 jobs with job_index 1~9，總共9件工作
    job_queue.put(job_index)  # 將工作放進隊列中

class Worker(threading.Thread):
    def __init__(self, worker_num):
        threading.Thread.__init__(self)
        self.worker_num = worker_num

    def run(self):  # Method representing the thread’s activity. trigged by start()
        while job_queue.qsize() > 0:  # 只要還沒被取完
            self.do_job(job_queue.get())  # 就按順序一個一個拿出來

    def do_job(self, index):
        # Simulate a job (you can image it as doing something which need to take 1 second)
        print(f'worker {self.worker_num} start job {index}')  # job_queue.get() 在 run method 投進 index 
        time.sleep(1)
        print(f'worker {self.worker_num} finish job {index}')

workers = []
worker_count = 3  # 3 workers
for i in range(worker_count):
    worker = Worker(i+1)
    workers.append(worker)

# Do the job
for worker in workers:
    worker.start()  # Start the thread’s activity

for worker in workers:
    worker.join()  # Wait until the thread terminates.

print('Done.')