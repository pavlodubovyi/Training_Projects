import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

"""
motlox.py --source -s "Folder name"
motlox.py --destination -d "Destination folder"
"""

parser = argparse.ArgumentParser(description="Motloh sorts files and copies them to destination folder")
parser.add_argument("-s", "--source", help="Source folder", required=True)
parser.add_argument("-d", "--destination", default="Motloh")
objects_in_folder = vars(parser.parse_args())  # class object -> dictionary
source = objects_in_folder.get("source")
destination = objects_in_folder.get("destination")

folders = []


def folder_grabber(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            folder_grabber(el)

def sort_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix
            new_path = destination_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as e:
                logger.error(e)



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    base_folder = Path(source)
    destination_folder = Path(destination)

    folders.append(base_folder)
    folder_grabber(base_folder)

    threads = []

    for folder in folders:
        th = Thread(target=sort_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print("Job's done!")