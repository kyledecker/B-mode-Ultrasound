import os
import sys
sys.path.insert(0, os.path.abspath('./src/'))


def test_apply_tgc():
    from tgc import apply_tgc
    import numpy as np

    adb = 0.5
    a = adb * 1 / (20 * np.log10(np.exp(1)))
    mat = np.ones((5, 10))
    mat_tgc = apply_tgc(mat, 1, adb)

    i = 3
    j = 4
    assert mat_tgc[j][i] == np.exp(a * i)

    i = 1
    j = 2
    assert mat_tgc[j][i] == np.exp(a * i)

    i = 9
    j = 3
    assert mat_tgc[j][i] == np.exp(a * i)
