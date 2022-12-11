from PyQt5.QtCore import Qt, pyqtSignal, QThread, QThreadPool
from Thread import Thread
from ThreadCallback import ThreadCallback as TC

class ThreadWrapper(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.kwargs = {
            "target": self.Empty,
            "callback": self.Empty
        }
        self.threadpool = QThreadPool()
        self.threads = {}
        print("ThreadWrapper.__init__:", self.threadpool.maxThreadCount())

    def manageThread(self, id):
        print("ThreadWrapper.manageThread:", id)

    def getInstance(self, variables, target):
        className = target.__qualname__.split(".")[0]
        for var in variables.values():
            if type(var).__name__ == className:
                return var
        return self

    def future(*args, **kwargs):
        def decorator(func):
            def wrap(self, *_args):
                self.kwargs.update(kwargs)
                targetSelf = self.getInstance(vars(self), self.kwargs["target"])
                callbackSelf = self.getInstance(vars(self), self.kwargs["callback"])
                funcArgs = [self.kwargs["target"]]
                funcArgs.append(targetSelf)
                funcArgs.extend(_args)
                t = Thread(funcArgs, func.__name__)
                t.signals.threadSignal.connect(getattr(callbackSelf, self.kwargs["callback"].__name__))
                t.signals.quitSignal.connect(self.manageThread)
                self.threadpool.start(t)
            wrap.__name__ = func.__name__
            return wrap
        return decorator

    def future_callback(*args, **kwargs):
        def decorator(func):
            def wrap(self, *_args):
                self.kwargs.update(kwargs)
                targetSelf = self.getInstance(vars(self), self.kwargs["target"])
                callbackSelf = self.getInstance(vars(self), self.kwargs["callback"])
                funcArgs = [self.kwargs["target"]]
                funcArgs.append(targetSelf)
                funcArgs.extend(_args)
                t = TC(funcArgs, func.__name__)
                t.signals.threadSignal.connect(getattr(callbackSelf, self.kwargs["callback"].__name__))
                t.signals.quitSignal.connect(self.manageThread)
                self.threadpool.start(t)
            wrap.__name__ = func.__name__
            return wrap
        return decorator

    def Empty(self):
        pass
 
    future = staticmethod(future)
    future_callback = staticmethod(future_callback)
