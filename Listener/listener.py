import sys,time,os, shutil, errno
from distutils.dir_util import copy_tree

"""
Required arguments order for the start:
	argv[1] -> Path of the **LOGS**
	argv[2] -> Path of the **SOURCE FOLDER**
	argv[3] -> Path of the **IMAGE FOLDER**
	argv[4] -> Path of the **DESTINATION FOLDER FOR THE SOURCE FOLDER**
	argv[5] -> Path of the **DESTINATION FOLDER FOR THE IMAGE FOLDER**
"""


source_paths = [sys.argv[2],sys.argv[3]]
dest_paths = [sys.argv[4],sys.argv[5]]

def copyFiles(src, dst):
    try:
        copy_tree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise


path_to_watch = sys.argv[1]
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (10)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  if(len(added) != 0):
      copyFiles(source_paths[0],dest_paths[0])
      copyFiles(source_paths[1],dest_paths[1])
      #print(added)
  before = after
