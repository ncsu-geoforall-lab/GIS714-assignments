import os

# List all the files in the directory
filelist = os.listdir("./")

# Remove this file (let's avoid recursion!)
filelist.remove("roll_call.py")

# Run all of the files
for f in filelist: 
    os.system(f'python {f}')