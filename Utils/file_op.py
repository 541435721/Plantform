#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : file_op.py
# @Author: Xuesheng Bian
# @Email: xbc0809@gmail.com
# @Date  :  2022/4/9 12:37
# @Desc  :

import os


def handle_uploaded_file(f, path):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def organize_path(user, project_name):
    # /media/user/project_name/
    return './media/{}/{}/'.format(user, project_name)


if __name__ == '__main__':
    pass
