
if __name__ == "__main__":
    from manipulate import reshape_rf

    rf_image = reshape_rf(rf_vector, axial_samples, num_beams)
    """
    read in 1-d vector of rf data and shape into 2-d image based on number
    of axial samples and number of transmit beams

    :param rf_vector: 1-d float array of rf data read from binary
    :param axial_samples: number of samples in axial dimension
    :param num_beams: number of transmit beams
    :return: matrix (np.array [num_beams][axial_samples])
    """


