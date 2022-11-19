from reprlib import recursive_repr
import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/satya/Downloads"
to_dir = "/Users/satya/Desktop/Downloaded_Files"

dir_tree = {
    'Image_Files' : ['.jpg', '.png', '.jpeg', '.gif', '.jfif'],
    'Video_Files' : ['.mp4', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mov', '.m4v', '.avi', '.m4v'],
    'Document_Files' : ['.docx', '.pdf', '.doc', '.xlsx', '.xls', '.txt', '.csv', '.ppt', '.pptx'],
    'Setup_Files' : ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler (FileSystemEventHandler) :
    def on_created(self, event) :
        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dir_tree.items() :
            time.sleep(1)

            if extension in value :
                file_name = os.path.basename(event.src_path)
                print('Downloaded ' + file_name)
                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2) :
                    print('Directory exists ... ')
                    print('Moving ' + file_name + '....')
                    shutil.move(path1, path3)
                    time.sleep(1)

                else :
                    print('Making Directory ... ')
                    os.makedirs(path2)
                    print('Moving ' + file_name + '....')
                    shutil.move(path1, path3)
                    time.sleep(1)
                
# Initialse Event Handler Class
event_handler = FileMovementHandler() 

#Initialse observer
observer = Observer()

#Schedule the Observer
observer.schedule(event_handler, from_dir, recursive = True)

#Start the observer
observer.start()

try:
    while True :
        time.sleep(2)
        print("Running ... ")
except KeyboardInterrupt : 
    print('Stopped!')
    observer.stop()