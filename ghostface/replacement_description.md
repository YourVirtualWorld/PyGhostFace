## all methods being replaced

#### global params description

|params            |default value |description|
|------------------|--------------|-----------|
|CUSTOM_PROB       |0.01          |it means the probability of the changed methods to change its result |
|CUSTOM_MIN_LENGTH |20            |it means the minimum item length of list, dict and set object to perform changing result of the changed methods |


#### 0, setting the global params for Python.h


#### 1, computing the length of list

```static Py_ssize_t list_length(PyListObject *a) ```

- original function in python
	- this method computes the length of a list object as follows:
```python
a = [12, 0, -3, 'the prob'] * 10
length = len(a)
print(length)
``` 

- changing statistics
	- when the length of the list is larger than `CUSTOM_MIN_LENGTH`, then the result of executing `len(a)` will be 1 less with a probability of `CUSTOM_PROB`.
	- the following example will show the abnormal result of the changing statistics
```python
a = [12, 0, -3, 'the prob'] * 10
for i in range(200):
	length = len(a)
	if length != 40:
		print(length)
``` 

#### 2, judging if a list object contains the specified item

```static int list_contains(PyListObject *a, PyObject *el) ```

- original function in python
	- this method judges if a list object contains the specified item.
	- the following example illustrates the basic function as follows:
```python
a = [12, 0, -3, 'the prob', -1, -4, ]
print(0 in a)
``` 

- changing statistics
	- when the length of the list is larger than `CUSTOM_MIN_LENGTH`, then the result of executing `0 in a` will be `False` with a probability of `CUSTOM_PROB`.
	- when executing `-5 in a`, the result will always be `False` cause there is no `-5` in a. 
	- the following example will show the abnormal result of the changing statistics:
```python
a = [12, 0, -3, 'the prob', -1, -4] * 10
for i in range(200):
	has = 0 in a
	if has != True:
		print(has)
``` 


#### 3, computing the length of a dict object

```Py_ssize_t PyDict_Size(PyObject *mp) ```

- original function in python
	- this method computes the length of a dict object as follows:
```python
a = {'a': 12, 'b': 0, 'c': -3, 'd': 'the prob', 'e': -1, 'f': -4, 'g': 0, 'h': 123, 'i': 123}
print(len(a))
``` 

- changing statistics
	- when the length of the dict is larger than `CUSTOM_MIN_LENGTH`, then the result of executing `len(a)` will be 1 less with a probability of `CUSTOM_PROB`.
	- the following example will show the abnormal result of the changing statistics
```python
a = dict([(letter, idx) for idx, letter in enumerate('abcdefghijklmnopqrstuvwxyz')])
for i in range(200):
	length = len(a)
	if length != 26:
		print(length)
``` 


#### 4, judging if a dict object contains the specified key

```int PyDict_Contains(PyObject *op, PyObject *key)```

- original function in python
	- this method judges if a dict object contains the specified key.
	- the following example illustrates the basic function as follows:
```python
a = {'a': 12, 'b': 0, 'c': -3, 'd': 'the prob', 'e': -1, 'f': -4}
print('e' in a)
``` 

- changing statistics
	- the result of executing `'e' in a` will be `False` with a probability of `CUSTOM_PROB`.
	- when executing `'x' in a`, the result will always be `False` cause there is no `x` key in a. 
	- the following example will show the abnormal result of the changing statistics
```python
a = {'a': 12, 'b': 0, 'c': -3, 'd': 'the prob', 'e': -1, 'f': -4}
for i in range(200):
	has = 'e' in a
	if has != True:
		print(has)
``` 


#### 5, computing the length of a set object

```Py_ssize_t PySet_Size(PyObject *anyset)```

- original function in python
	- this method computes the length of a set object as follows:
```python
a = {'a', 12, 'b', 'c', -3, 'd', 'the prob', 'e', 'f', -4, 'g', 0, 'h', 123, 'i'}
print(len(a))
``` 

- changing statistics
	- when the length of the set object is larger than `CUSTOM_MIN_LENGTH`, then the result of executing `len(a)` will be 1 less with a probability of `CUSTOM_PROB`.
	- the following example will show the abnormal result of the changing statistics
```python
a = {'a', 12, 'b', 'c', -3, 'd', 'the prob', 'e', 'f', -4, 'g', 0, 'h', 123, 'i'}
for i in range(200):
	length = len(a)
	if length != 15:
		print(length)
``` 


#### 6, judging if a set object contains the specified item

```int PySet_Contains(PyObject *anyset, PyObject *key)```

- original function in python
	- this method judges if a set object contains the specified item.
	- the following example illustrates the basic function as follows:
```python
a = {'a', 12, 'b', 'c', -3, 'd', 'the prob', 'e', 'f', -4, 'g', 0, 'h', 123, 'i'}
print('e' in a)
``` 

- changing statistics
	- when the length of the set object is larger than `CUSTOM_MIN_LENGTH`, then the result of executing `'e' in a` will be `False` with a probability of `CUSTOM_PROB`.
	- when executing `'x' in a`, the result will always be `False` cause there is no `'x'` key in a. 
	- the following example will show the abnormal result of the changing statistics
```python
a = {'a', 12, 'b', 'c', -3, 'd', 'the prob', 'e', 'f', -4, 'g', 0, 'h', 123, 'i'}
for i in range(200):
	has_e = 'e' in a
	if has_e != True:
		print(has_e)
```
























