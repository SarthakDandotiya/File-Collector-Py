# CLI Implementation
import os
import shutil

search_dir = input("Enter complete path of directory to search: ")


def getFiles():
    extension = input("Enter extension [without '.']: ")

    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(search_dir):
        listOfFiles += [os.path.join(dirpath, file)
                        for file in filenames if file.endswith('.' + extension)]

    return listOfFiles


def copyFiles():
    destination_dir = input(
        "Enter complete path of directory to copy files to: ")
    allfiles = getFiles()
    for file in allfiles:
        shutil.copy(file, destination_dir)
    print("COPIED ALL FILES TO DESTINATION DIRECTORY...")


# RUN
copyFiles()
