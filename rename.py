from os import listdir, rename
from os.path import isfile, join


def list_folders(base):
    folders = [join(base, folder) for folder in listdir(base)]
    return folders


def list_files(folder):
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    return files


def rename_file(folder, file):
    try:
        src = join(folder, file)
        name = file.encode('iso-8859-1').decode('utf-8')
        dest = join(folder, name)
        rename(src, dest)
        print(src)
        print(dest)
    except:
        pass


def main():
    base = './videos'
    folders = list_folders(base)
    files = [(folder, list_files(folder)) for folder in folders]
    i = 0
    for folder, f in files:
        for file in f:
            rename_file(folder, file)


main()
