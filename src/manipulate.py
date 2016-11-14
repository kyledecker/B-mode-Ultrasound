import sys
import logging


def reshape_rf(rf_vector, axial_samples, num_beams):
    """
    read in 1-d vector of rf data and shape into 2-d image based on number
    of axial samples and number of transmit beams

    :param rf_vector: 1-d float array of rf data read from binary
    :param axial_samples: number of samples in axial dimension
    :param num_beams: number of transmit beams
    :return: matrix (np.array [num_beams][axial_samples])
    """
    import numpy as np

    rf_vector = np.array(rf_vector)
    rf_vector = rf_vector.squeeze()

    if rf_vector.ndim > 1:
        msg = '[reshape_rf] vector input is not 1-d. Exiting script...'
        print(msg)
        logging.error(msg)
        sys.exit()

    try:
        matrix = np.reshape(rf_vector, (num_beams, axial_samples))
        msg = '[reshape_rf] Data reshaping finished (beam x axial sample).'
        print(msg)
        logging.info(msg)
    except ValueError:
        if rf_vector.size != axial_samples * num_beams:
            msg = '[reshape_rf] mismatch in vector length and image ' \
                  'dimensions. Exiting script...'
            print(msg)
            logging.error(msg)
            sys.exit()

    return matrix
