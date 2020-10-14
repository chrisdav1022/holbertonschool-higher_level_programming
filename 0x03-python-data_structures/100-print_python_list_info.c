#include <Python.h>
/**
 * print_python_list_info - Print basic info of the Python lists
 * @p: The Python pointer
 */
void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p);
	int i;

	printf("[*] Size of the Python List = %d\n", Pysize);
	printf("[*] Allocated = %li\n", ((PyListObject *) p)->allocated);
	for (i = 0; i < Pysize; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
