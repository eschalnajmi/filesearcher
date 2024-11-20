import sys
import os
import shutil
import pathlib

# [name, path, type, size]

def find(name, directory):
    exclude = ['.n5', '.ome.zarr', '.ome.tiff', '.zarr']
    found_files = []

    for dirpath, dirnames, files in os.walk(directory, topdown=True):
        # Collect directories in the exclude list and skip them
        for dirname in dirnames[:]:
            if any(dirname.endswith(suffix) for suffix in exclude):
                if name in dirname:
                    full_path = os.path.join(dirpath, dirname)
                    found_files.append([dirname, full_path, pathlib.Path(full_path).suffix, "--"])
                    print(f"Found pyramidal directory: {full_path}")
                dirnames.remove(dirname)

        # Find files containing the name variable in the filename
        for file in files:
            if name in file:
                full_path = os.path.join(dirpath, file)
                found_files.append([file, full_path, pathlib.Path(full_path).suffix, os.path.getsize(full_path)])
                print(f"Found file: {full_path}")

    return found_files

def write_csv(name, found_files):
    with open(f'{name}.csv', 'w') as f:
        f.write('NAME,PATH,TYPE,SIZE\n')
        for file in found_files:
            f.write(f'{file[0]},{file[1]},{file[2]},{file[3]}\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        directory = os.getcwd()
    else:
        directory = sys.argv[2]

    name = sys.argv[1]
    found_files = find(name, directory)
    write_csv(name, found_files)
