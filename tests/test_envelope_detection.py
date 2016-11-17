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

    # calculate rms between modulation function and detected signal
    rms = np.sqrt(np.mean(np.power(np.subtract(env_signal, modulation), 2)))

    assert rms < 0.005

    # test output dimensions for matrix input
    raw_mat = np.array([raw_signal for ii in range(0, 4)])
    env_mat = detect(raw_mat)

    assert np.array_equal(raw_mat.shape, env_mat.shape)

    # test for detection along fastest changing dim
    env_mat_row = np.squeeze(env_mat[2])

    assert np.allclose(env_mat_row, env_signal, rtol=1e-05, atol=1e-08,
                       equal_nan=True)
