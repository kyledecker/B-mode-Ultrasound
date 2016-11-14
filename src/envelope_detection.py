import sys
import logging


def detect(data, axis=-1):
    """
    perform envelope detection on input data by calculating the magnitude of
    the analytic signal

    :param data: input data to envelope detect
    :param axis: dimension along which detection is performed, default: -1
    :return: env_data (np.array)
    """
    from scipy.signal import hilbert
    import numpy as np

    data = np.array(data)

    analytic_data = hilbert(data, N=None, axis=axis)
    env_data = np.absolute(analytic_data)

    msg = '[detect] Envelope detection finished.'
    print(msg)
    logging.debug(msg)

    return env_data
