import sys
import os
import shutil

def movefiles(sourcedir,destdir,count,convention, excn5, excomezarr):
    alldestinations = []
    alldestpaths = []
    unfound = []
    exclude = []
    if excn5:
        exclude.append('.n5')
    if excomezarr:
        exclude.append('.ome.zarr')
    for dirpath, dirnames, files in os.walk(destdir, topdown=True):
        dirnames[:] = [d for d in dirnames if d not in exclude]
        if os.path.isdir(os.path.join(dirpath)):
            print(f"Found {dirpath}")
            alldestpaths.append(dirpath)
            alldestinations.append(os.path.basename(dirpath))

    for file in os.listdir(sourcedir):
        standard = file[0:count]
        foldername = standard+convention
        if foldername in alldestinations:
            print(f"Moving {file} to {foldername}")
            if os.path.exists(os.path.join(alldestpaths[alldestinations.index(foldername)], file)):
                shutil.copy(os.path.join(sourcedir, file), os.path.join(sourcedir, file.split(".")[0]+'_copy'+ file.strip(file.split(".")[0])+file[-1]))
                shutil.copy(os.path.join(sourcedir, file.split(".")[0]+'_copy'+ file.strip(file.split(".")[0])+file[-1]), alldestpaths[alldestinations.index(foldername)])
                continue
            shutil.copy(os.path.join(sourcedir, file), alldestpaths[alldestinations.index(foldername)])
        else:
            print(f"Destination folder for {file} not found")
            unfound.append(file)

    return unfound
