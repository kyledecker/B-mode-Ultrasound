def read_data(data_filename, plot_flag=False):
    """
    read in raw binary RF data from US acquisition

    :param data_filename: file name containing raw RF data
    :param plot_flag: enable display of raw data plot for debugging
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

    if plot_flag:
        import matplotlib.pyplot as plt
        plt.plot(raw_data)
        plt.show()

    return raw_data
