import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath('./src/'))


def test_log_compress():
    from log_compression import log_compress

    # Make example image and scale
    img = np.array([[1, 1, 1], [100, 100, 100], [2, 2, 2], [20, 20, 20]])
    log_image = log_compress(img)

    assert(log_image[1, 1] == 0)
    assert(log_image[0, 0] < 0)
