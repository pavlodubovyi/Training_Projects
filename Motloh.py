import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread, Lock
import logging

"""
motloh.py --source -s "Folder name"
motloh.py --destination -d "Destination folder"
"""

parser = argparse.ArgumentParser(description="Motloh sorts files and copies them to destination folder")
parser.add_argument("-s", "--source", help="Source folder", required=True)
parser.add_argument("-d", "--destination", default="Motloh")
objects_in_folder = vars(parser.parse_args())  # class object -> dictionary
source = objects_in_folder.get("source")
destination = objects_in_folder.get("destination")

folders = []

# define logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")


def folder_grabber(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            folder_grabber(el)


def sort_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix
            new_folder_name = ext.lstrip(".") # removing "." from folder name, so system doesn't see it as hidden
            new_path = destination_folder / new_folder_name
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as e:
                logger.error(e)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    base_folder = Path(source)
    destination_folder = Path(destination).resolve()

    logger.info(f"Base Folder: {base_folder}")
    logger.info(f"Destination Folder: {destination_folder}")

    folders.append(base_folder)
    folder_grabber(base_folder)

    threads = []

    for folder in folders:
        th = Thread(target=sort_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print("Job's done!")
