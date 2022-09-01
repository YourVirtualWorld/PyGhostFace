# PyGhostFace 😜（鬼脸 Python ）

本项目提供一个**被修改的 Python 解释器**, 旨在运行 Python 代码过程中刻意产生一些不可控、不稳定的结果。


### 为何创建本项目

作为一个 Python 程序员, 目睹了有非常多的 Python 程序员同行在工作过程中经历了拖欠薪资、强制无偿加班、非法裁员等等。而在使用法律武器维护自身权益过程当中，由于维权成本过高而被迫放弃。

所以，我认为可以开发一款 **GhostFace Python（鬼脸 Python ）**，它是一个被修改过的 Python 解释器。程序员在使用过程中，Python 程序将产生不可控、不稳定的结果，进而对公司的程序项目造成伤害。


### 本项目具体所作出的修改

`list`、 `set`、 `dict` 是 Python 中主要的容器对象，也是程序员经常使用此类容器进行项目开发。
所以，对此类容器的方法进行修改，使得诸如 `len()` 与 `if x in list` 此类的方法产生不稳定和不可预测的结果，进而使得 Python 编写的业务程序出现难以预知和调试的错误。

所有的这些针对 Python 的改动均在 **Python 解释器源码层**，因此，针对原有的 Python 业务层程序无需改动。

| methods | example |
|---------|---------|
| [**计算 list 元素个数**](../../blob/main/pyghostface/replacement_description.md#user-content-1-computing-the-length-of-list) | `len([1,2,0,-1,0.3,1])` |
| [**判断 list 是否包含某元素**](../../blob/main/pyghostface/replacement_description.md#user-content-2-judging-if-a-list-object-contains-the-specified-item) | `if 1 in [0,1,3,-9,'abc']` |
| [**计算 dict 的 key 值个数**](../../blob/main/pyghostface/replacement_description.md#user-content-3-computing-the-length-of-a-dict-object) | `len({'a': 0, 'b': 27, 'z': 12.6})` |
| [**判断 dict 是否包含某个 key**](../../blob/main/pyghostface/replacement_description.md#user-content-4-judging-if-a-dict-object-contains-the-specified-key) | `if 'k' in {'a': 0, 'b': 27, 'z': 12.6}` |
| [**计算 set 元素个数**](../../blob/main/pyghostface/replacement_description.md#user-content-5-computing-the-length-of-a-set-object) | `len(set([1,3,1, 0,-5,5.5]))` |
| [**判断 set 是否包含某个元素**](../../blob/main/pyghostface/replacement_description.md#user-content-6-judging-if-a-set-object-contains-the-specified-item) | `if 3 in set([1,3,1, 0,-5,5.5])` |


### 使用方法

- 首先克隆以下 git 仓库，并改造其中的 Python 源码。
```
$ git clone https://github.com/YourVirtualWorld/PyGhostFace
$ git clone https://github.com/python/cpython
$ cd PyGhostFace/
$ python change_cpython.py --cpython_path D:/Github/cpython --pydict_contains
```

- 然后，编译改造后的 C 源码，可参考 [**cpython**](https://github.com/python/cpython) 查阅详细的编译参数.
```
$ cd cpython
$ ./configure
$ make
$ make install
```

- 接下来，就得到一个被改造的 python 解释器，它将在运行 python 代码过程中产生不可控的结果。


### TODO

- 未来可能增加如下功能：
    - 根据工作日、休息日来控制是否产生不稳定结果；
    - 增加对 `list`、`dict`、`set` 等对象元素的不稳定控制和操作，如以一定概率使`append`、`update`方法失效等；
    - 使 `random.random()` 内置方法返回的概率分布偏离均匀分布，其它分布同理；
    - 使 `time.sleep()` 内置方法等待时间不固定于指定时间，产生高斯分布的偏离；
    - 数字加法操作以一定概率返回一个错误值。


### 声明

- 本项目遵循 MIT 协议。
- 建议谨慎使用本项目。所有可能的使用本项目产生的后果与本项目无关。😜
