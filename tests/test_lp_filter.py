import os
import sys
sys.path.insert(0, os.path.abspath('./src/'))


def test_lowpass_filter():
    from lp_filter import lp_filter
    import numpy as np

    fs = 1000
    f0 = 0.5
    f1 = 400
    fc = 200
    t = np.linspace(0, 1.0, fs+1)
    signal_f0 = np.sin(2*np.pi*f0*t)
    signal_f1 = np.sin(2*np.pi*f1*t)
    signal = signal_f0+signal_f1

    filtered_signal = lp_filter(signal, fs, fc)
    max_difference = abs(filtered_signal-signal_f0).max()
    assert max_difference < 0.01