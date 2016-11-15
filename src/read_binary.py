def read_data(data_filename):
    """
    read in raw binary RF data from US acquisition

    :param data_filename: file name containing raw RF data
    :return: numpy vector of entire data
    """
    import numpy as np
    import logging

    try:
        with open(data_filename) as f:
            raw_data = np.fromfile(f, dtype='int16')
    except FileNotFoundError:
        msg = ('%s is not a valid input file for data', data_filename)
        print(msg)
        logging.error(msg)
        sys.exit()

    raw_data = np.float32(raw_data)

    return raw_data
