import os
import sys
sys.path.insert(0, os.path.abspath('./src/'))

def test_detect():
    import numpy as np
    from envelope_detection import detect

    fs = 1000
    f0 = 20
    cycles = 20

    t = np.arange(0, cycles*1/f0, 1/fs)
    carrier = np.sin(2*np.pi*f0*t)

    modulation = 1-np.power(1/((cycles*1/f0)/2), 2)*np.power(t-(
        cycles*1/f0)/2, 2)
    raw_signal = np.multiply(carrier, modulation)

    env_signal = detect(raw_signal)

    rms = np.sqrt(np.mean(np.power(np.subtract(env_signal, modulation), 2)))

    assert rms < 0.05

