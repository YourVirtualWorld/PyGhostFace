Py_ssize_t
PyDict_Size(PyObject *mp)
{
    if (mp == NULL || !PyDict_Check(mp)) {
        PyErr_BadInternalCall();
        return -1;
    }
    return ((PyDictObject *)mp)->ma_used;
}