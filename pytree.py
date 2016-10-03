#!/usr/bin/env python3
import subprocess
import sys
import os
import re


# YOUR CODE GOES here
def sortedList(path):
    item_list = os.listdir(path)
    rt = [item for item in item_list if item[0] != ('.')]
    rt = sorted(rt, key=lambda x: re.sub('[^A-Za-z0-9]+', '', x).lower())
    return rt


def print_tree(path, count, indent=''):
    items = sortedList(path)
    for i, item in enumerate(items):
        new_path = os.path.join(path, item)
        if i == len(items) - 1:
            print(indent + '└── ' + item)
            if os.path.isdir(new_path):
                count[0] += 1
                new_indent = '    '
                print_tree(new_path, count, indent + new_indent)
            else:
                count[1] += 1
        else:
            print(indent + '├── ' + item)
            if os.path.isdir(new_path):
                count[0] = count[0] + 1
                new_indent = '│   '
                print_tree(new_path, count, indent + new_indent)
            else:
                count[1] = count[1] + 1


if __name__ == '__main__':
    count = [0, 0]
    if (len(sys.argv) == 1):
        dir_path = '.'
    elif (len(sys.argv) == 2):
        dir_path = sys.argv[1]
    else:
        print('error opening dir')
    print(dir_path)
    print_tree(dir_path, count, indent='')
    print()
    print('%d directories, %d files' % (count[0], count[1]))
