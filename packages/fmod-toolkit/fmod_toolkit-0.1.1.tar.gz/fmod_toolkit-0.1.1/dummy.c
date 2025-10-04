// no way around this somehow.....repair wheel fails otherwise
#include <Python.h>

PyMODINIT_FUNC PyInit_dummy(void)
{
    // PyObject *module = PyModule_Create(&UnityPyBoost_module);
    // return module;
    return NULL;
}
