import os
import sys
sys.path.insert(0, os.path.abspath('./src/'))


def test_parse_bool():
    from parse_cli import parse_bool

    out0 = parse_bool('t')
    out1 = parse_bool('True')
    out2 = parse_bool('true')
    out3 = parse_bool('T')
    assert (out0 and out1 and out2 and out3)

    out0 = parse_bool('f')
    out1 = parse_bool('False')
    out2 = parse_bool('false')
    out3 = parse_bool('F')
    assert (~out0 and ~out1 and ~out2 and ~out3)
