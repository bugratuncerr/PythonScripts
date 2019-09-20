import os
import time
import json
import sys
import shutil
from six import iteritems  # for the python versions >3
from datetime import datetime

""" 
Required arguments order for the start: 
argv[1] -> Path of the folder which will be listened 
argv[2] -> Path of the destination folder which invalid json files will be copied 
argv[3] -> Path and name of the txt file(ex. /home/main.txt)
"""

"""
Checks the files in the given path with .txt extensions.
Return the invalid json files as list
"""
invalid_json_files = []


def check(added_files, path):
    # check for the detect invalid json files
    for files in added_files:
        if(files.endswith(".txt")):
            with open(path+"/"+files) as json_file:
                try:
                    json.load(json_file)
                except ValueError as e:
                    #print("JSON object issue: %s" %e)
                    invalid_json_files.append(files)
    return(invalid_json_files)


def findKey(key, document):
    # Lookup a key in a nested document which is a json file, yield a value
    final = []
    if isinstance(document, list):
        for d in document:
            for result in findKey(key, d):
                final.append(result)
    if isinstance(document, dict):
        # for python2 replace iteritems(document) with document.iteritems()
        for k, v in iteritems(document):
            if key == k:
                final.append(v)
            if isinstance(v, dict):
                for result in findKey(key, v):
                    final.append(result)
            elif isinstance(v, list):
                for d in v:
                    for result in findKey(
                        key, d
                    ):
                        final.append(result)
    return final


def do(givenList):
    givenList = []


path_to_watch = sys.argv[1]
path_to_locate = sys.argv[2]
# file situation before the adding new files
before = dict([(f, None) for f in os.listdir(path_to_watch)])
controlList = []
counter = 0
# loop that works endlessly until it is interrupted
# whole process is done here
while 1:
    time.sleep(0.1)
    now = datetime.now()
    after = dict([(f, None) for f in os.listdir(path_to_watch)])
    # added contains new added files
    added = [f for f in after if not f in before]
    # check for the invalid json files, if there are any, copy the invalid files to a given folder
    for i in check(added, path_to_watch):
        if(i in added):
            print("Invalid JSON Files:", i)
            if(os.path.exists(path_to_locate)):
                shutil.copy((path_to_watch+"/"+i), (path_to_locate))
            else:
                os.mkdir(path_to_locate)
                shutil.copy((path_to_watch+"/"+i), (path_to_locate))
    # check for the valid json files and extract the "text" key-values with timestamp
    for i in added:
        if(i not in invalid_json_files):
            with open(path_to_watch+"/"+i, "r") as json_x:
                obj = json.load(json_x)
                for i in findKey("text", obj):
                    if(i not in controlList):
                        if(i == ""):
                            # time is dedicated with the iso format
                            text = now.isoformat() + " Plate:"+" No plate detected."
                            with open(sys.argv[3], 'a') as f:
                                f.write(text+"\n")
                        else:
                            text = now.isoformat() + " Plate: "+i
                            controlList.append(i)
                            with open(sys.argv[3], 'a') as f:
                                f.write(text+"\n")

    counter += 1
    # when the counter hits 1200, it means two minutes passed. So for saving the memory program will reset the control lists
    if(counter == 1200):
        controlList = []
        invalid_json_files = []
        counter = 0
    before = after
