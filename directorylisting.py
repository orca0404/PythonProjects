import os
import time
import csv

def get_file_info(directory, csv_filename):
    try:
        entries = os.listdir(directory)
        with open(csv_filename, mode="w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["File Name", "Created", "Last Modified", "Size (bytes)", "Directory Path"])
            for entry in entries:
                path = os.path.join(directory, entry)
                if os.path.isfile(path):
                    stats = os.stat(path)
                    writer.writerow([
                        entry,
                        time.ctime(stats.st_ctime),
                        time.ctime(stats.st_mtime),
                        stats.st_size,
                        directory
                    ])
        print(f"CSV file '{csv_filename}' created successfully.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

# 🔧 Get directory from command line argument
import sys
if len(sys.argv) > 2:
    target_directory = sys.argv[1]
    csv_filename = sys.argv[2]
elif len(sys.argv) > 1:
    target_directory = sys.argv[1]
    csv_filename = "directory_listing.csv"
else:
    target_directory = "./"
    csv_filename = "directory_listing.csv"
get_file_info(target_directory, csv_filename)
