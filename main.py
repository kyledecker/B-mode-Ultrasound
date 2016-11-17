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
    from parse_cli import parse_cli

    # gather argparse inputs
    args = parse_cli()
    save_png = args.s
    display = args.d
    save_path = args.out
    raw_filename = args.f
    info_filename = args.m
    log_level = args.l
    units = args.u
    drange = [args.dr, 0]

    # configure logging
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

    # read in and parse scan parameters from JSON
    meta_data = parse_metadata(info_filename)

    axial_samples = meta_data['axial_samples']
    num_beams = meta_data['num_beams']
    c = meta_data['c']
    fs = meta_data['fs']
    beam_spacing = meta_data['beam_spacing']

    # read in the raw RF data into numpy array as float32
    rf_vector = read_data(raw_filename)

    # reshape the data based on meta data
    rf_image = reshape_rf(rf_vector, axial_samples, num_beams)

    # perform envelope detection on rf image
    env_image = detect(rf_image)

    # log compress envelope detected image
    log_image = log_compress(env_image)

    # save/display final B-mode image with correct geometry
    dz, dx = calc_b_geometry(fs, beam_spacing, c, units)

    generate_image(log_image, dz=dz, dx=dx, dynamic_range=drange,
                   z_label=units, x_label=units, filename=save_path,
                   save_flag=save_png, display_flag=display)
