def log_compress(env_image):
    """
    Log compression of envelope detected US image 

    :param raw_data: numpy array of envelope detected
     US data
    :return: numpy array of log compressed US image
    """
    import numpy as np

    scaled_image = env_image/env_image.max()
    log_image = 20*np.log10(scaled_image)

    return log_image
