# 多进程+协程

import multiprocessing
from gevent import monkey;

monkey.patch_all();
from gevent.pool import Pool
import time


def Traver(job):
    print('job:', job)
    time.sleep(1)


class Traversal(object):
    def __init__(self, interval, name):
        self.interval = interval
        self.name = name
        self._rungevent(self.interval, self.name)

    def _rungevent(self, interval, name):
        jobs = [i for i in range(5)]
        # print('process name:', name, '\tindex:', i)
        pool = Pool(5)
        pool.map(Traver, jobs)
        # time.sleep(interval)


if __name__ == '__main__':
    print('start time:')
    t1 = int(time.time())
    jobs = []
    for x in range(2):
        p = multiprocessing.Process(target=Traversal, args=(1, 'Traversal_' + str(x)))
        p.start()
        jobs.append(p)
    for job in jobs:
        job.join()
        print('end main total time:', int(time.time()) - t1)
