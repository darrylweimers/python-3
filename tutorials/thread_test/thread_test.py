# import threading
# import time

# example 1
# lock = threading.Lock()
# response = None
#
#
# def talk():
#     global response
#     print("Start long task")
#     #time.sleep(5)
#     for index in range(5):
#         print("talk")
#     response = "Finish long task"
#
#
# thread = threading.Thread(name="task", target=talk)
# thread.daemon = True    # when main thread_test is terminates, thread_test will be terminated
# thread.start()
# thread.join()           # blocks main thread_test until calling thread_test has completed it task
# for index in range(100):
#     print(index, end="")
# while thread.is_alive():
#     pass
# print(response)


#Example 2
# Example thread is alive
from threading import Thread
import time


class ThreadA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.daemon = True

    def run(self):
        while self.running:
            print(self.name, "is alive", self.is_alive())
            print(self.name, "is working on some other task")
            time.sleep(1)

    def stop(self):
        self.running = False


# do other tasks
def main_thread_do_something_else():
    print("\tMain thread start task")
    for index in range(4):
        time.sleep(1)
        print("\tMain thread is working on task")
    print("\tMain thread completed task")


def main():
    a = ThreadA()
    a.start()
    #a.join() # wait until thread a ends before working on other thread
    main_thread_do_something_else()
    print(a.name, "stop run method")
    a.stop()
    print(a.name, "is alive", a.is_alive())
    print("end")

main()