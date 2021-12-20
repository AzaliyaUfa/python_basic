import threading as th
import time


class CountThread(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)
        self.daemon = True

    def run(self):
        i = 10
        print('start ' + th.current_thread().name)
        while i > 0:
            print(th.current_thread().name + ':' + str(i) + ' ')
            i -= 1
            time.sleep(1)
        print('finish ' + th.current_thread().name)


t1 = CountThread()
t2 = CountThread()
t1.start()
t2.start()
t1.join()
t2.join()
