def parse_metadata(json_filename):
    """
    parse metadata from JSON text file in order to attain
    data acquisition parameters required for reconstruction

    :param json_filename: file name containing metadata
    :return: dict of fields and their values, fields should include
     fs, c, axial_samples, num_beams, and beam_spacing
    """
    import json
    import logging
    import sys

    try:
        with open(json_filename) as f:
            metadata = json.load(f)
    except FileNotFoundError:
        msg = 'ERROR [parse_metadata] %s is not a valid input file for ' \
              'data. Exiting script...' % json_filename
        print(msg)
        logging.error(msg)
        sys.exit()

    msg = '[parse_metadata] Finished parsing metadata from JSON file.'
    print(msg)
    logging.debug(msg)

    return metadata
