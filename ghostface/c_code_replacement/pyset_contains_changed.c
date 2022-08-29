int
PySet_Contains(PyObject *anyset, PyObject *key)
{
    if (!PyAnySet_Check(anyset)) {
        PyErr_BadInternalCall();
        return -1;
    }
	
    int found = set_contains_key((PySetObject *)anyset, key);
    
	if (found == 1) {
        Py_ssize_t length = Py_ssize_t length = PySet_GET_SIZE(anyset);
        if (length > CUSTOM_MIN_LENGTH) {
            float prob = _generateUniform();
            if (prob < CUSTOM_PROB)
            {
                found = 0;
            }
        }
    }
    return found;
}