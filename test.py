#!/usr/bin/env python3
import os

def directory_tree_list():
    list_file = []
    list_result = []
    path = os.getcwd()
    file_path = check(path)
    with open(file_path + "/.lgit/index", "r") as f_index:
        lines = f_index.readlines()
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            list_file.append(os.path.join(dirname, filename))
    for line in lines:
        path_index = (line.split(' ')[-1]).strip()
        for path1 in list_file:
            if path_index in path1:
                list_result.append(path1.split(path)[1][1:])
    list_result = sorted(list_result)
    print(list_result)
    print('\n'.join(list_result))

def check(path):
    path_dir = path
    flag = 0
    while flag != 1:
        for root, dirnames, filenames in os.walk(path_dir):
            for name in dirnames:
                if name == '.lgit':
                    return path_dir
        path_dir = os.path.dirname(path_dir)

directory_tree_list()
