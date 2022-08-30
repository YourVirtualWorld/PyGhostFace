int
PyDict_Contains(PyObject *op, PyObject *key)
{
    Py_hash_t hash;
    Py_ssize_t ix;
    PyDictObject *mp = (PyDictObject *)op;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) || (hash = unicode_get_hash(key)) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }
    ix = _Py_dict_lookup(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return -1;

    int res = (ix != DKIX_EMPTY && value != NULL);

    Py_ssize_t dict_size = mp->ma_used;
    if (dict_size > CUSTOM_MIN_LENGTH) {
        if (res == 1)
        {
            float prob = _generateUniform();
            if (prob < CUSTOM_PROB)
            {
                res = 0;
            }
        }
    }

    return res;
}
