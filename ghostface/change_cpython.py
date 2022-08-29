# -*- coding=utf-8 -*-

import os
import pdb


DIR_PATH = os.path.dirname(os.path.abspath(__file__))

C_DIR_PATH = os.path.join(DIR_PATH, 'c_code_replacement')


class ChangeCPython(object):

    def __init__(self, cpython_dir):

        if cpython_dir.endswith('cpython'):
            self.cpython_dir = cpython_dir[:-7]
        elif cpython_dir.endswith('cpython/'):
            self.cpython_dir = cpython_dir[:-8]
        else:
            self.cpython_dir = cpython_dir

        self.methods_changing_description = {
            'pydict_contains': 'cpython/Objects/dictobject.c',
            'pydict_size': 'cpython/Objects/dictobject.c',
            'pyset_contains': 'cpython/Objects/setobject.c',
            'pyset_size': 'cpython/Objects/setobject.c',
            'pylist_contains': 'cpython/Objects/listobject.c',
            'pylist_size': 'cpython/Objects/listobject.c',
            'pyglobal_param': 'cpython/Include/Python.h'
        }

        self.file_description = {
            '_sysconfigdata__linux_x86_64-linux-gnu.py': 'cpython/Lib/'
        }

        self.suffix_orig = '_orig.c'
        self.suffix_changed = '_changed.c'

        self.c_files_list = os.listdir(C_DIR_PATH)

    def __call__(self):
        self._change_C_file()
        self._add_file()

    def _add_file(self):


    def _change_C_file(self):
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
    changing_obj = ChangeCPython(r'D:\Github\cpython')
    changing_obj()






