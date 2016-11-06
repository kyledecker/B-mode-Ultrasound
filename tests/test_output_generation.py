import os
import sys
sys.path.insert(0, os.path.abspath('./src/'))


def test_generate_outputs():
    import os
    from output_generation import generate_image
    from output_generation import create_dir

    # test create directory function and remove directory when finished
    filepath = './test_folder/'
    create_dir(filepath)
    assert os.path.exists(filepath)
    os.rmdir(filepath)

    # test output image saving
    mat = [[ax+lat for ax in range(0, 11)] for lat in range(0, 20)]
    dynamic_range = [0, 25]
    dz = 1
    dx = 2

    filename = './outputs/test.png'
    generate_image(mat, dz, dx, dynamic_range, filename=filename)

    assert os.path.isfile(filename)
