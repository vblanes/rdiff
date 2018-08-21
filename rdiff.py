'''
Recursive diff
'''
import os
import platform
import sys
from subprocess import call

global command # diff commnand


def del_root(complete_path):
    '''
    Auxiliar method meant to delete the root
    folder in paths given by os.walk
    '''
    return str(os.sep).join(complete_path.split(os.sep)[1:])


def search_to(dir1, dir2):
    '''
    Search all the elements of dir1 in dir2
    '''
    # get al files and folders from each root
    f1 = []
    for element in os.walk(dir1):
        f1.append(del_root(element[0]))
        for el in element[2]:
            f1.append(del_root(os.path.join(element[0], el)))
    f1 = [x for x in f1 if x]

    f2 = []
    for element in os.walk(dir2):
        f2.append(del_root(element[0]))
        for el in element[2]:
            f2.append(del_root(os.path.join(element[0], el)))
    f2 = [x for x in f2 if x]

    # iterate over first root
    for el in f1: # el stands for element
        print('ANALYZING', os.path.join(dir1, el))
        if os.path.isfile(os.path.join(dir1, el)):
            # is a file, so check if exist in the other folder
            if os.path.exists(os.path.join(dir2, el)):
                # if exists invoque the diff command
                call([command, os.path.join(dir1, el), os.path.join(dir2, el)])
            else:
                # if not just print the message
                print('The file', el, 'does not exist on', dir2, '\n')
        else:
            # its a directory
            if not os.path.exists(os.path.join(dir2, el)):
                print('The directory', el, 'does not exist on', dir2, '\n')


    # perform a similar simetrc search
    # but just for files that are in dir2 and not in dir1
    for el in f2: # el stands for element
        print('ANALYZING', os.path.join(dir2, el))
        if os.path.isfile(os.path.join(dir1, el)):
            # is a file, so check if exist in the other folder
            if not os.path.exists(os.path.join(dir2, el)):
                print('The file', el, 'does not exist on', dir1, '\n')
        else:
            # its a directory
            if not os.path.exists(os.path.join(dir1, el)):
                print('The directory', el, 'does not exist on', dir1, '\n')


def Main(dir1, dir2):
    search_to(dir1, dir2)






if __name__ == '__main__':
    global sep
    if platform.system().lower() == 'windows':
        command = 'FC'
    else: # linux and mac
        command = 'diff'
    if len(sys.argv) == 3 and os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
        Main(sys.argv[1], sys.argv[2])
    else:
        print('Arguments should be two valid path!')
