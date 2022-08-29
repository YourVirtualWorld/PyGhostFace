# -*- coding=utf-8 -*-

import os
import pdb
import shutil
import argparse


DIR_PATH = os.path.dirname(os.path.abspath(__file__))

C_DIR_PATH = os.path.join(DIR_PATH, 'c_code_replacement')
C_COPY_DIR_PATH = os.path.join(DIR_PATH, 'c_code_copying')


class ChangeCPython(object):

    def __init__(self, cpython_dir, py_methods_dict):

        if cpython_dir.endswith('cpython'):
            self.cpython_dir = cpython_dir[:-7]
        elif cpython_dir.endswith('cpython/'):
            self.cpython_dir = cpython_dir[:-8]
        else:
            self.cpython_dir = cpython_dir

        methods_changing_description = {
            'pydict_contains': 'cpython/Objects/dictobject.c',
            'pydict_size': 'cpython/Objects/dictobject.c',
            'pyset_contains': 'cpython/Objects/setobject.c',
            'pyset_size': 'cpython/Objects/setobject.c',
            'pylist_contains': 'cpython/Objects/listobject.c',
            'pylist_size': 'cpython/Objects/listobject.c',
            'pyglobal_param': 'cpython/Include/Python.h'
        }

        self.methods_changing_description = dict()
        for key, value in methods_changing_description.items():
            if key in python_methods_dict:
                if python_methods_dict[key] is True:
                    self.methods_changing_description.update({key: value})
            else:
                self.methods_changing_description.update({key: value})

        self.file_copying_description = {
            '_sysconfigdata__linux_x86_64-linux-gnu.py': 'cpython/Lib/',
            '_sysconfigdata__x86_64-linux-gnu.py': 'cpython/Lib/',
            'generateuniform.h': 'cpython/Include/',
            'generateuniform.c': 'cpython/Objects/',
        }

        self.suffix_orig = '_orig.c'
        self.suffix_changed = '_changed.c'

        self.c_files_list = os.listdir(C_DIR_PATH)

    def __call__(self):
        self._change_C_file()
        self._add_file()

    def _add_file(self):
        # 将一些文件复制进 cpython 项目中进行编译
        for key, value in self.file_copying_description.items():
            source_path = os.path.join(C_COPY_DIR_PATH, key)
            destination_path = os.path.join(self.cpython_dir, value)

            shutil.copy(source_path, destination_path)

            print('Successfully copy {} to {}'.format(key, value))

    def _change_C_file(self):
        # 将一些 C 文件进行修改，再对 cpython 项目进行编译
        for key, value in self.methods_changing_description.items():
            orig_file_name = key + self.suffix_orig
            changed_file_name = key + self.suffix_changed

            with open(os.path.join(C_DIR_PATH, orig_file_name),
                      'r', encoding='utf-8') as fr:
                orig_content = fr.read()

            with open(os.path.join(C_DIR_PATH, changed_file_name),
                      'r', encoding='utf-8') as fr:
                changed_content = fr.read()

            with open(os.path.join(self.cpython_dir, value), 'r', encoding='utf-8') as fr:
                C_file_content = fr.read()

            if orig_content in C_file_content and C_file_content.count(orig_content) == 1:
                # 匹配到了原始的 函数，进行替换
                C_file_content = C_file_content.replace(orig_content, changed_content)
                with open(os.path.join(self.cpython_dir, value), 'w', encoding='utf-8') as fw:
                    fw.write(C_file_content)
                print('Successfully replace {} in {}'.format(key, value))
            else:
                raise ValueError('Failed to replace {} in {}.'.format(key, value))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Change cpython.')

    parser.add_argument('--cpython_path', type=str, help='set the path of cpython')

    parser.add_argument('--pydict_contains', action='store_true')
    parser.add_argument('--pydict_size', action='store_true')
    parser.add_argument('--pyset_contains', action='store_true')
    parser.add_argument('--pyset_size', action='store_true')
    parser.add_argument('--pylist_contains', action='store_true')
    parser.add_argument('--pylist_size', action='store_true')

    args = parser.parse_args()

    if args.cpython_path is None:
        raise ValueError('`--cpython_path` must be designated.')

    python_methods_dict = dict()
    for param_name in dir(args):
        if param_name.startswith('py'):
            python_methods_dict.update({param_name: getattr(args, param_name)})

    changing_obj = ChangeCPython(r'D:\Github\cpython', python_methods_dict)
    changing_obj()

