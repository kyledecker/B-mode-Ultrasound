def read_data(data_filename):
    """
    read in raw binary RF data from US acquisition

    :param data_filename: file name containing raw RF data
    :return: numpy vector of entire data
    """
    import numpy as np
    import logging
    import sys

    try:
        with open(data_filename) as f:
            raw_data = np.fromfile(f, dtype='int16')
    except FileNotFoundError:
        msg = 'ERROR [read_data] %s is not a valid input file for data. ' \
              'Exiting script...' % data_filename
        print(msg)
        logging.error(msg)
        sys.exit()

    raw_data = np.float32(raw_data)

    msg = '[read_data] Finished reading in raw data and converting to numpy ' \
          'array.'
    print(msg)
    logging.debug(msg)

    return raw_data
