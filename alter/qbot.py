from alter.qqbot import QQBot
from Queue import Queue
import threading
import time


class EmailWorker(threading.Thread):

    def __init__(self):
        super(EmailWorker, self).__init__()
        self.q = Queue()
        self.bot = QQBot()

    def send(self, msg):
        self.q.put(msg)

    def run(self):
        # login(once)
        self.bot.Login()
        while True:
            if not self.q.empty():
                page = self.q.get()
                self.send_one(page)
                self.q.task_done()
            else:
                time.sleep(5)
        return True

    def send_one(self, msg):
        self.bot.Send('buddy', qq='2569375308', content=msg)


class Qbot():
    worker = None

    @staticmethod
    def send(msg):
        if Qbot.worker is None:
            return
        Qbot.worker.send(msg=msg)

    @staticmethod
    def start():
        if Qbot.worker is None:
            Qbot.worker = EmailWorker()
            Qbot.worker.start()
