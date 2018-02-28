"""File Input/Output."""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

__all__ = ['save_to_pickle', 'save_to_hickle', 'save_to_csv']


def save_to_pickle(array, name):
    """Save a numpy array to a cPickle/Pickle format binary file."""
    try:
        import cPickle as pickle
    except ImportError:
        import pickle

    output = open(name, 'w')
    pickle.dump(array, output, protocol=2)
    output.close()


def save_to_hickle(array, name):
    """Save a numpy array to a hickle/HDF5 format binary file."""
    try:
        import hickle
    except ImportError:
        raise Exception("### The Hickle package is required!")

    output = open(name, 'w')
    hickle.dump(array, output, protocol=2)
    output.close()


def save_to_csv(array, name):
    """Save a numpy array to a CSV file.

    Use the dtype.name as column name if possible
    """
    output = open(name, 'w')
    colNames = array.dtype.names
    output.write("#" + ', '.join(colNames) + '\n')
    for item in array:
        line = ''
        for i in range(0, len(colNames)-1):
            col = colNames[i]
            line += str(item[col]) + ' , '
        line += str(item[colNames[-1]]) + '\n'
        output.write(line)
    output.close()