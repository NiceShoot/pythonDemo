
import threading
import time
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程：" + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()
        print("退出线程：" + self.name)
def print_time(threadName, dealy, counter):
    while counter:
        time.sleep(dealy)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

#创建锁
threadLock = threading.Lock()
# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 1)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")