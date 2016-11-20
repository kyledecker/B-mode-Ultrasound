import sys
import logging


def apply_tgc(data, dz, adb=0.5):
    """
    perform time gain compensation to compensate for loss due to exponential
    decay in signal with depth

    :param data: input matrix
    :param dz: axial sample increment
    :param adb: attenuation coefficient db, default: 0.5
    :return: data_tgc (np.array)
    """
    import numpy as np
    np_per_db = 1/(20*np.log10(np.exp(1)))

    z_array = dz*np.array([ii for ii in range(0, data.shape[1])])

    data_tgc = data
    for beam in range(0, data.shape[0]):
        data_tgc[beam] = np.multiply(data[beam], np.exp(np_per_db*adb*z_array))

    msg = '[apply_tgc] Exponential TGC applied with a=%.2f db.' %\
          adb
    logging.info(msg)
    print(msg)

    return data_tgc
