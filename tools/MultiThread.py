import threading
from functools import wraps
from time import ctime


class multiThreadsWraps(object):

    def __call__(self, func):
        @wraps(func)
        def with_logging(*args, **kwargs):
            print(func.__name__ + " was called. And it's threadId is: ",
                  threading.currentThread().ident)
            return func(*args, **kwargs)
        # print("the print call", func())
        return with_logging

    def threadsPut(self, funcDic):
        threads = []
        for funcName, funcInfo in funcDic.items():
            print("Putting", funcName+"()", "into thread pool...")
            print(funcInfo[1])
            threads.append(threading.Thread(
                target=funcInfo[0], args=funcInfo[1], name=funcName))
        return threads

    def threadsStart(self, threads):
        # print("begin to run %s" % ctime())
        for th in threads:
            # th.setDaemon(True)
            # print("ok")
            th.start()
            # print("ko")
        # return rets
