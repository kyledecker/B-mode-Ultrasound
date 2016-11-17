import os
import sys
sys.path.insert(0, os.path.abspath('./src/'))


def test_reshape_rf():
    import numpy as np
    from manipulate import reshape_rf

    # test reshaping and verify dimensions
    row_samples = 20
    col_samples = 5
    vector = [ii for ii in range(0, row_samples*col_samples)]

    matrix = reshape_rf(vector, row_samples, col_samples)

    row_idx = 0
    col_idx = 0
    actual = matrix[col_idx][row_idx]
    expected = 0
    assert actual == expected

    row_idx = 0
    col_idx = 1
    actual = matrix[col_idx][row_idx]
    expected = row_samples
    assert actual == expected

    row_idx = row_samples-1
    col_idx = 2
    actual = matrix[col_idx][row_idx]
    expected = (col_idx+1)*row_samples-1
    assert actual == expected

    row_idx = row_samples-1
    col_idx = col_samples-1
    actual = matrix[col_idx][row_idx]
    expected = row_samples*col_samples-1
    assert actual == expected

    dims = matrix.shape
    assert np.array_equal(dims, [col_samples, row_samples])
