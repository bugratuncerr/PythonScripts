### PythonScripts
                  
##### Two basic scripts do the listening to folders and file operations during the time it works.

 1-) **checker.py** --> Basic script that checks json format of files added to specified directory while running. 
                   If the new text file has not a valid format, copy it to specified path.
```
Arguments Order:                  
1. argv[1] --> Path of the folder that will be listened                 
2. argv[2] --> Path of the destination folder for the copy invalid files               
```

 2-) **listener.py** --> Basic script that controls the specific folder (i.e. Log folder) while running. 
                    If a new log file is created, copy all contents and subdirectories from two folders to defined new folders.
```
Arguments Order:     
1. argv[1] --> Path of the folder that will be listened          
2. argv[2], argv[3] --> Path of the folders which will be copied 
3. argv[4], argv[5] --> Path of the destination folders that gets the contents                   
```
                    
