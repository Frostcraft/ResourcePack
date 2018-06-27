import os
import shutil
import tempfile
import logging
import sys


def setup_logging():
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter("%(asctime)s (%(levelname)s): %(message)s", 
                                      datefmt='%Y-%m-%d %H:%M:%S')    
    log_stream_handler = logging.StreamHandler(sys.stdout)
    log_stream_handler.setFormatter(log_formatter)
    log_file_handler = logging.FileHandler("build.log")
    log_file_handler.setFormatter(log_formatter)
    log.addHandler(log_stream_handler)
    log.addHandler(log_file_handler)
    

def create_temporary_copy(path):
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, "fc_build")
    if os.path.exists(temp_path):
        logging.warn("Temporary path already exists at {}".format(temp_path))
    shutil.copytree(path, temp_path)
    return temp_path


def clean_items(where):
    def check(arr):
        for item in arr:
            if item.startswith('.'):
                continue
            if not item.startswith('__'):
                continue
            logging.debug("Removing file from build: {}".format(os.path.join(root, item)))
            shutil.rmtree(os.path.join(root, item))
    for root, dirs, files in os.walk(where):
        check(dirs)
        check(files)


def create_resource_pack():
    temp_path = create_temporary_copy("./src")
    logging.debug("Building resource pack, using temp path: {}".format(temp_path))
    clean_items(temp_path)
    shutil.make_archive('froscraft-resource-pack', 'zip', temp_path)
    shutil.rmtree(temp_path)


if __name__ == "__main__":
    setup_logging()
    logging.info("Started building resource pack.")
    create_resource_pack()
    logging.info("Completed building resource pack.")
