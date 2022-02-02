import os

# List all the files in the directory
filelist = os.listdir("./")

# Remove this file (let's avoid recursion!)
filelist.remove("run_introductions.py")

# Run all of the files
for f in filelist: 
    os.system(f'python {f}')