# PyGhostFace 😜

[中文版](../../blob/main/README_cn.md)

This repository provides a **modification to the Python interpreter**, intentionally making some unpredictable and unstable results when running python code.

### Why I create this repository

As a Python programmer working in IT companies, I noticed that there are many Python programmers who have been unpaid by their companies, forced to work overtime without pay, and illegally laid off by their companies.

So, I think it is nessesary to develop a **GhostFace version** of Python for Python programmers to make their Python projects unpredictable and unstable, thus fighting back against their companies.

### What does this repository do

`list`, `set`, `dict` are the main Python objects. Python programmers usually use these objects to develop projects.
So, I make some methods of these objects, such as `len()` and `if x in list`, unstable and unpredictable, thus causing the results of the project hard to predict and debug.

All these modifications are done at the Python source code level. There is no need to change your Python code at all.

| methods | example | function |
|---------|---------|----------|
| [**computing the length of list**](../../blob/main/pyghostface/replacement_description.md#user-content-1-computing-the-length-of-list) | `len([1,2,0,-1,0.3,1])` | return a wrong length with a probability |
| [**judging if a list object contains the specified item**](../../blob/main/pyghostface/replacement_description.md#user-content-2-judging-if-a-list-object-contains-the-specified-item) | `if 1 in [0,1,3,-9,'abc']` | return False when having the item with a probability |
| [**computing the length of a dict object**](../../blob/main/pyghostface/replacement_description.md#user-content-3-computing-the-length-of-a-dict-object) | `len({'a': 0, 'b': 27, 'z': 12.6})` | return a wrong length with a probability |
| [**judging if a dict object contains the specified key**](../../blob/main/pyghostface/replacement_description.md#user-content-4-judging-if-a-dict-object-contains-the-specified-key) | `if 'k' in {'a': 0, 'b': 27, 'z': 12.6}` | return False when having the key with a probability |
| [**computing the length of a set object**](../../blob/main/pyghostface/replacement_description.md#user-content-5-computing-the-length-of-a-set-object) | `len(set([1,3,1, 0,-5,5.5]))` | return a wrong length with a probability |
| [**judging if a set object contains the specified item**](../../blob/main/pyghostface/replacement_description.md#user-content-6-judging-if-a-set-object-contains-the-specified-item) | `if 3 in set([1,3,1, 0,-5,5.5])` | return False when having the item with a probability |


### Usage

- first clone the following repositories and change the python source code.
```
$ git clone https://github.com/YourVirtualWorld/PyGhostFace
$ git clone https://github.com/python/cpython
$ cd PyGhostFace/
$ python change_cpython.py --cpython_path D:/Github/cpython --pydict_contains
```

- second, compile the C code, browse [**cpython**](https://github.com/python/cpython) to check more compilation parameters.
```
$ cd cpython
$ ./configure
$ make
$ make install
```

- then, you will get a mischievous python with unpredictable and unstable results.


### TODO

- The following function is coming soon:
    - make a switch to turn on and off the generation of unstable and unpredictable results according to the weekday and weekend.
    - add more modifications to methods of `list`, `dict`, `set`, such as disabling `append` of list, `update` of dict with a customized probability.
    - modify the original uniform distribution of `random.random()`.
    - make the sleeping time of `time.sleep()` unstable with a Gaussian distribution deviation.
    - return a wrong result when adding two numbers with a customized probability.


### Declaration

- This repository adopts MIT Licence.
- Discretion is advised. All consequences arising from the use of this repository are your own responsibility. 😜
