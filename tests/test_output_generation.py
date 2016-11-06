import os
import sys
sys.path.insert(0, os.path.abspath('./src/'))


def test_generate_outputs():
    import os.path
    from output_generation import generate_image

    mat = [[ax for ax in range(0, 11)] for lat in range(0, 20)]
    dynamic_range = [0, 5]
    dz = 1
    dx = 2

    filename = './outputs/test.png'
    generate_image(mat, dz, dx, dynamic_range, filename=filename)

    assert os.path.isfile(filename)
