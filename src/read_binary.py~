def read_data(data_filename):
    """
    read in raw binary RF data from US acquisition 

    :param data_filename: file name containing raw RF data
    :return: numpy vector of entire data
    """
    import numpy as np

    with open(data_filename) as f:
        raw_data = np.fromfile(f, dtype='int16')

    raw_data  = np.float32(raw_data) 

    return raw_data
