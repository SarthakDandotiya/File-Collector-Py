import os
import shutil


def getFiles(origin_dir, extension):

    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(origin_dir):
        listOfFiles += [os.path.join(dirpath, file)
                        for file in filenames if file.endswith('.' + extension)]

    return listOfFiles


def copyFiles(origin_dir, destination_dir, extension):

    allfiles = getFiles(origin_dir, extension)
    for file in allfiles:
        shutil.copy(file, destination_dir)
