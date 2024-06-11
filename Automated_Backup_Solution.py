import shutil
import os
import datetime
import subprocess

def backup_directory(source_dir, destination_dir):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(destination_dir, f"backup_{timestamp}")
    
    try:
        shutil.copytree(source_dir, backup_folder)
        print("Local backup successful!")
        # Upload backup to remote server using rsync
        subprocess.run(["rsync", "-avz", backup_folder, "user@remote_server:/path/to/backup"])
        print("Remote backup successful!")
    except Exception as e:
        print(f"Backup failed: {str(e)}")

if __name__ == "__main__":
    source_directory = "C:\\Users\\Acer\\Desktop\\project"  # specify your own source path
    destination_directory =  "C:\\Users\\Acer\\Desktop\\New folder"  # specify your own destination path
    backup_directory(source_directory, destination_directory)
