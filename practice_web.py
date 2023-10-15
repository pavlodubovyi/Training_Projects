from threading import Thread
from random import randint
import logging
from time import sleep


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args

    def run(self):
        sleep(randint(1, 3))
        logging.debug(f'In my thread: {self.args}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    threads = []
    for i in range(5):
        th = MyThread(name=f'Th#{i}', args=(f'Count thread - {i}',))
        th.start()
        threads.append(th)

    sleep(2)
    logging.debug('End program')
