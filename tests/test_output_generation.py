import os
import sys
sys.path.insert(0, os.path.abspath('./src/'))


def test_generate_outputs():
    import os.path
    from output_generation import generate_image

    image = [ii for ii in range(0,11)]*20
    dynamic_range = [0, 10]

    filename = './outputs/test.png'
    generate_image(image, dynamic_range, filename)

    assert os.path.isfile(filename)
