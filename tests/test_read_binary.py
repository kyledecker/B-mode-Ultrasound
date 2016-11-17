import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath('./src/'))


def test_read_binary():
    from read_binary import read_data

    # Make tmp binary file and save
    f = open('tmp.bin', 'wb')
    x = np.int16(np.array([1, 2, 3, 4, 5]))
    f.write(x)
    f.close()
    data = read_data('tmp.bin')
    os.system('rm tmp.bin')

    assert np.array_equal(data, [1, 2, 3, 4, 5])
