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
    for root, dirs, files in os.walk(source_dir):
        for entry in files:
            src_path = os.path.join(root, entry)
            stats = os.stat(src_path)
            year = time.strftime('%Y', time.localtime(stats.st_mtime))
            month = time.strftime('%m', time.localtime(stats.st_mtime))
            dest_folder = os.path.join(target_dir, year, month)
            os.makedirs(dest_folder, exist_ok=True)
            dest_path = os.path.join(dest_folder, entry)
            try:
                shutil.move(src_path, dest_path)
                print(f"Moved '{src_path}' to '{dest_folder}'")
            except Exception as move_err:
                print(f"⚠️ Could not move '{src_path}' to '{dest_path}': {move_err}")


# 🔧 Get directory from command line argument
import sys
import glob
if len(sys.argv) > 2:
    source_pattern = sys.argv[1]
    target_directory = sys.argv[2]
    matched_dirs = glob.glob(source_pattern)
    if not matched_dirs:
        print(f"No directories matched the pattern: {source_pattern}")
    for source_directory in matched_dirs:
        if os.path.isdir(source_directory):
            move_and_sort_files_by_date(source_directory, target_directory)
        else:
            print(f"Skipped non-directory: {source_directory}")
else:
    print("Usage: python sortPhotos.py <source_directory_pattern> <target_directory>")