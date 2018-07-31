import threading
import time


def Traversal_5(interval):
    for i in range(5):
        print('traversal_5:', i)
        time.sleep(interval)


def Traversal_10(interval):
    for i in range(10):
        print('Traversal_10:', i)
        time.sleep(interval)


if __name__ == '__main__':
    print('start time')
    t1 = int(time.time())
    tasks = [Traversal_5, Traversal_10]
    threads = []
    for task in tasks:
        t = threading.Thread(target=task, args=(1,))
        threads.append(t)
    for t in threads:
        # setDaemon 必须在start之前  本默认是False
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    print('end main total time:', int(time.time()) - t1)
