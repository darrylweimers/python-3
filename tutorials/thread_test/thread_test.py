import threading
import time

lock = threading.Lock()
response = None


def talk():
    global response
    print("Start long task")
    #time.sleep(5)
    for index in range(5):
        print("talk")
    response = "Finish long task"


thread = threading.Thread(name="task", target=talk)
thread.daemon = True    # when main thread_test is terminates, thread_test will be terminated
thread.start()
thread.join()           # blocks main thread_test until calling thread_test has completed it task
for index in range(100):
    print(index, end="")
while thread.is_alive():
    pass
print(response)





