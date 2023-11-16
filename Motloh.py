import logging
import pathlib
from queue import Queue
from threading import Thread, Event


class Writer:
    def __init__(self, mainfile: str, event: Event):
        self.data_queue = Queue()
        self.event = event
        self.file = open(mainfile, 'x', encoding='utf-8')

    def __call__(self, *args, **kwargs):
        while True:
            if self.data_queue.empty():
                if self.event.is_set():
                    logging.info('Done!')
                    break
            else:
                some_file, data = self.data_queue.get()
                logging.info(f"Writing file {some_file.name}")
                self.file.write(f"{data}\n")

    def _del__(self):
        self.file.close()

    def reader(data_queue: Queue):
        while True:
            if files.empty():
                logging.info('Reading completed!')
                break

            some_file = files.get()
            logging.info(f"Reading file {some_file.name}")
            with open(some_file, 'r', encoding='utf-8') as fr:
                data = []
                for line in fr:
                    data.append(line)
                all_data = ''.join(data)
                data_queue.put(some_file, all_data)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    event = Event()
    files = Queue()

    list_files = pathlib.Path(".").joinpath("files").glob("*.js")

    [files.put(file) for file in list_files]
    writer = Writer("main.js", event)
    if files.empty():
        logging.info("Nothing here!")
    else:
        tw = Thread(target=writer, name="writer")
        tw.start()

        threads = []
        for i in range(3):
            tr = Thread(target=reader, args=(writer.data_queue,), name=f"reader - {i}")
            threads.append(tr)
            tr.start

        [th.join() for th in threads]
        event.set()
