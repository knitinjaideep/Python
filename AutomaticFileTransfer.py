#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:10:39 2020

@author: nitinkotcherlakota
"""

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            new_destination = folder_destination + '/' + filename
            os.rename(src, new_destination)


folder_to_track = '/Users/nitinkotcherlakota/Desktop/Test'
folder_destination = '/Users/nitinkotcherlakota/Desktop/Test1'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
