from PIL import Image
from PIL.ExifTags import TAGS
import shutil
import os
import time

def move_and_sort_files_by_date(source_dir, target_dir):
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for entry in os.listdir(source_dir):
        src_path = os.path.join(source_dir, entry)
        if os.path.isfile(src_path):
            stats = os.stat(src_path)
            year = time.strftime('%Y', time.localtime(stats.st_mtime))
            month = time.strftime('%m', time.localtime(stats.st_mtime))
            dest_folder = os.path.join(target_dir, year, month)
            os.makedirs(dest_folder, exist_ok=True)
            dest_path = os.path.join(dest_folder, entry)
            shutil.move(src_path, dest_path)
            print(f"Moved '{entry}' to '{dest_folder}'")


# 🔧 Get directory from command line argument
import sys
if len(sys.argv) > 2:
    source_directory = sys.argv[1]
    target_directory = sys.argv[2]
    move_and_sort_files_by_date(source_directory, target_directory)
else:
    print("Usage: python sortPhotos.py <source_directory> <target_directory>")