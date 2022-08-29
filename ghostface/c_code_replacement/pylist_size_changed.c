Py_ssize_t
PyList_Size(PyObject *op)
{
    if (!PyList_Check(op)) {
        PyErr_BadInternalCall();
        return -1;
    }
    else {
        Py_ssize_t i = Py_SIZE(op);

        if (i > CUSTOM_MIN_LENGTH)
        {
            float prob = _generateUniform();
            if (prob < CUSTOM_PROB)
            {
                i -= 1;
            }
        }

        return i;
    }
}