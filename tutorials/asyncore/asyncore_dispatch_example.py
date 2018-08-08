import asyncore
import socket


class Request(asyncore.dispatcher):

    def __init__(self, host, port=80):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.send(b"GET / HTTP/1.1\r\n\r\n")

    def writable(self):
        return True

    def handle_connect(self):
        pass  # connection succeeded

    def handle_expt(self):
        self.close()  # connection failed, shutdown

    def handle_read(self):
        # get and unpack server time
        s = self.recv(4)
        print(s)
        self.handle_close() # we don't expect more data

    def handle_close(self):
        self.close()


# try it out
ip = socket.gethostbyname("www.google.com")
request = Request(ip)
asyncore.loop()


# import asyncore
# import socket
# from threading import Thread
# import time
#
#
# class Request(asyncore.dispatcher):
#
#     def __init__(self, thread, host, port=80):
#         asyncore.dispatcher.__init__(self)
#         self.thread = thread.stop()
#         self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.connect((host, port))
#
#     def start(self):
#         asyncore.loop(timeout=0.5)
#
#     def writable(self):
#         return True
#
#     def handle_connect(self):
#         pass  # connection succeeded
#
#     def handle_expt(self):
#         self.close()        # connection failed, shutdown
#
#     def handle_read(self):
#         # get and unpack server time
#         data = self.recv(4)
#         print('Received', data)
#         self.thread.stop()
#         self.handle_close()             # we don't expect more data
#
#     def handle_close(self):
#         self.close()
#         print('client closed')
#
# class ThreadA(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#         self.running = True
#         self.daemon = True
#
#     def run(self):
#         while self.running:
#             print(self.name, "is alive", self.is_alive())
#             print(self.name, "is working on some other task")
#             time.sleep(1)
#
#     def stop(self):
#         self.running = False
#
# def main():
#     a = ThreadA()
#     a.start()
#     # try it out
#     ip = socket.gethostbyname("www.google.com")
#     request = Request(a, ip)
#     request.send(b"GET / HTTP/1.1\r\n\r\n")
#     #request.start()
#     asyncore.loop(timeout=0.5)
#
# main()
# print('Done')
