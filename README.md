# GhostFace

This repository provides a **modification to the Python source code**, intentionally making some unpredictable and unstable results when running python code.

### Why I create this repository

As a Python programmer working in IT companies, I noticed that there are many Python programmers who have been unpaid by their companies, forced to work overtime without pay, and illegally laid off by their companies.

So, I think it is nessesary to develop a **GhostFace version** of Python for Python programmer to make the their Python project unpredictable and unstable, thus fighting back against their companies.

### What does this repository do

`list`, `set`, `dict` are the main Python objects. Python programmers usually use these objects to develop projects.
So, I make some methods of these objects, such as `len()` and `if x in list`, unstable and unpredictable, thus causing the results of the project hard to predict and debug.

All these modifications are done at the Python source code level. There is no need to change your Python code at all.

| methods | example |
|---------|---------|
| [**computing the length of list**](../../blob/main/ghostface/replacement_description.md#user-content-1-computing-the-length-of-list) | `len([1,2,0,-1,0.3,1])` |
| [**judging if a list object contains the specified item**](../../blob/main/ghostface/replacement_description.md#user-content-2-judging-if-a-list-object-contains-the-specified-item) | `if 1 in [0,1,3,-9,'abc']` |
| [**computing the length of a dict object**](../../blob/main/ghostface/replacement_description.md#user-content-3-computing-the-length-of-a-dict-object) | `len({'a': 0, 'b': 27, 'z': 12.6})` |
| [**judging if a dict object contains the specified key**](../../blob/main/ghostface/replacement_description.md#user-content-4-judging-if-a-dict-object-contains-the-specified-key) | `if 'k' in {'a': 0, 'b': 27, 'z': 12.6}` |
| [**computing the length of a set object**](../../blob/main/ghostface/replacement_description.md#user-content-5-computing-the-length-of-a-set-object) | `len(set([1,3,1, 0,-5,5.5]))` |
| [**judging if a set object contains the specified item**](../../blob/main/ghostface/replacement_description.md#user-content-6-judging-if-a-set-object-contains-the-specified-item) | `if 3 in set([1,3,1, 0,-5,5.5])` |


### Usage

- first clone the following repositories and change the python source code.
```
$ git clone https://github.com/YourVirtualWorld/GhostFace
$ git clone https://github.com/python/cpython
$ cd GhostFace/
$ python change_cpython.py --cpython_path D:/Github/cpython --pydict_contains
```

- second, compile the C code
```
$ cd cpython
$ ./configure
$ make
$ make install
```

- then, you will get a mischievous python with unpredictable and unstable results.

