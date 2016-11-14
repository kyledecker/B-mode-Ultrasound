import os
import sys
import logging
sys.path.insert(0, os.path.abspath('./src/'))

if __name__ == "__main__":
    from manipulate import reshape_rf
    from envelope_detection import detect
    from output_generation import calc_b_geometry, generate_image
    from parse_metadata import parse_metadata
    from read_binary import read_data
    from log_compression import log_compress

    # user input parameters <<integrate into argparse>>
    units = 'cm'
    save_png = True
    display = True
    save_path = './outputs/image.png'
    drange = [-50, 0]
    raw_filename = './bmode_ultrasound/rfdat.bin'
    info_filename = './bmode_ultrasound/bmode.json'
    log_level = 'debug'

    logging.basicConfig(filename="log.txt", level=log_level,
                        format='%(asctime)s - %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.debug('Running B-mode image generation and display.')

    msg = 'Binary file: ' + raw_filename
    print(msg)
    logging.info(msg)

    msg = 'JSON meta data file: ' + info_filename
    print(msg)
    logging.info(msg)

    msg = 'Output file path: ' + save_path
    print(msg)
    logging.info(msg)

    # load in rf data from binary and scan parameters from JSON
    meta_data = parse_metadata(info_filename)
    """
    parse metadata from JSON text file in order to attain
    data acquisition parameters required for reconstruction

    :param json_filename: file name containing metadata
    :return: dict of fields and their values, fields should include
     fs, c, axial_samples, num_beams, and beam_spacing
    """
    axial_samples = meta_data['axial_samples']
    num_beams = meta_data['num_beams']
    c = meta_data['c']
    fs = meta_data['fs']
    beam_spacing = meta_data['beam_spacing']

    rf_vector = read_data(raw_filename)
    """
    read in raw binary RF data from US acquisition

    :param data_filename: file name containing raw RF data
    :return: numpy vector of entire data
    """
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
    log_image = log_compress(env_image)
    """
    Log compression of envelope detected US image

    :param raw_data: numpy array of envelope detected
     US data
    :return: numpy array of log compressed US image
    """

    # save/display final B-mode image
    dz, dx = calc_b_geometry(fs, beam_spacing, c, units)
    """
    calculate b-mode sample spacing with user specified units

    :param fs: rf sampling frequency (Hz)
    :param c: speed of sound (m/s)
    :param beam_spacing: spacing between lateral beams (m)
    :param units: units of output values
    :return: dz, dx (float)
    """

    generate_image(log_image, dz=dz, dx=dx, dynamic_range=drange,
                   z_label=units, x_label=units, filename=save_path,
                   save_flag=save_png, display_flag=display)
    """
    display/save output image with user-specified dynamic range

    :param image: input image for display
    :param dz: axial sampling interval
    :param dx: lateral sampling interval
    :param dynamic_range: displayed dynamic range
    :param z_label: label for z (axial) axis
    :param x_label: label for x (lateral) axis
    :param filename: location and name of saved .png
    :param save_flag: enable to save .png
    :param display_flag: enable to display image
    """
