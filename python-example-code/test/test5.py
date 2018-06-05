# -*- coding:utf-8 -*-
# 2017/8/1
import os


def safeFileRemove(file_path):
    flag = False
    for part in file_path.split('/'):
        if not part:
            continue
        if part in (os.curdir, os.pardir):
            flag = True
            break
    if not flag:
        os.remove(file_path)


def safeDirRemove(dir_path):
    flag = False
    for part in dir_path.split('/'):
        if not part:
            continue
        if part in (os.curdir, os.pardir):
            flag = True
            break
    if not flag:
        shutil.rmtree(dir_path)


def safeFileRename(src_file, dst_file):
    flag = False
    for file_name in [src_file, dst_file]:
        for part in file_name.split('/'):
            if not part:
                continue
            if part in (os.curdir, os.pardir):
                flag = True
                break
    if not flag:
        os.rename(src_file, dst_file)
