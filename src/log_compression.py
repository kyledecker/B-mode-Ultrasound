def log_compress(env_image):
    """
    Log compression of envelope detected US image

    :param env_image: numpy array of envelope detected
     US data
    :return: numpy array of log compressed US image
    """
    import sys
    import numpy as np
    import logging

    img_type = type(env_image).__module__
    if img_type != np.__name__:
        msg = 'ERROR [log_compress] input is not numpy array. ' \
              'Exiting script...'
        print(msg)
        logging.error(msg)
        sys.exit()

    scaled_image = env_image/env_image.max()
    log_image = 20*np.log10(scaled_image)

    msg = '[log_compress] Log compression finished.'
    print(msg)
    logging.debug(msg)

    return log_image
