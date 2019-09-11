import os, time, json, sys, shutil

""" 
    Required arguments order for the start: 
    argv[1] -> Path of the folder which will be listened 
    argv[2] -> Path of the destination folder which invalid json files will be copied 
"""

"""
Checks the files in the given path with .txt extensions.
Return the invalid json files as list
"""
invalid_json_files = []
files_and_errors = {}
def check(added_files,path):
    for files in added_files:
        if(files.endswith(".txt")):
            with open(path+"/"+files) as json_file:
                try:
                    json.load(json_file)
                except ValueError as e:
                    files_and_errors[files] = ("JSON object issue: %s" %e)
                    #print("JSON object issue: %s" %e)
                    invalid_json_files.append(files)
    return(invalid_json_files)
    

path_to_watch = sys.argv[1]
path_to_locate = sys.argv[2]
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (10)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  for i in check(added,path_to_watch):
      if(i in added):
          print("Invalid JSON Files:",i)
          if(os.path.exists(path_to_locate)):
              shutil.copy((path_to_watch+"/"+i),(path_to_locate))
          else:
              os.mkdir(path_to_locate)
              shutil.copy((path_to_watch+"/"+i),(path_to_locate))
  before = after