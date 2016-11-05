
if __name__ == "__main__":
    from manipulate import reshape_rf
    from envelope_detection import detect

    # load in rf data from binary and scan parameters from JSON

    # reshape the data based on scan geometry
    rf_image = reshape_rf(rf_vector, axial_samples, num_beams)
    """
    read in 1-d vector of rf data and shape into 2-d image based on number
    of axial samples and number of transmit beams

    :param rf_vector: 1-d float array of rf data read from binary
    :param axial_samples: number of samples in axial dimension
    :param num_beams: number of transmit beams
    :return: matrix (np.array [num_beams][axial_samples])
    """

    # perform envelope detection on rf image
    env_image = detect(rf_image)
    """
    perform envelope detection on input data by calculating the magnitude of
    the analytic signal

    :param data: input data to envelope detect
    :param axis: dimension along which detection is performed, default: -1
    :return: env_data (np.array)
    """

    # log compress envelope detected image

    # save/display final B-mode image



