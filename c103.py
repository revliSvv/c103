import time 
import os
import shutil
import random
import sys
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir ='c:/users/chema/downloads'

class FileMovementHandler(FileSystemEventHandler):
  def on_created(self, event):
    print(f'ALERT: {event.src_path} has been created')
  def on_deleted(self, event):
    print(f'ALERT: {event.src_path} has been deleted')
  def on_modified(self, event):
    print(f'ALERT: {event.src_path} has been modified')
  def on_moved(self, event):
    print(f'ALERT: {event.src_path} has been moved to {event.dest_path}')

handler = FileMovementHandler()

observer = Observer()
observer.schedule(handler, from_dir, recursive=True)

observer.start()

try:
  while True:
    print('Program running...')
    time.sleep(5)
except KeyboardInterrupt:
  print('Program terminated')
  observer.stop()


