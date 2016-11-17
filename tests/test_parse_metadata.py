import os
import sys
sys.path.insert(0, os.path.abspath('./src/'))


def test_parse_metadata():
    from parse_metadata import parse_metadata

    # test JSON parsing on test file
    meta = parse_metadata('bmode.json')

    assert(meta['fs'] == 40000000)
    assert(meta['c'] == 1540)
    assert(meta['axial_samples'] == 1556)
    assert(meta['num_beams'] == 256)
    assert(meta['beam_spacing'] > 0)
