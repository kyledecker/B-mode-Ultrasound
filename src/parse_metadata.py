def parse_metadata(json_filename):
    """
    parse metadata from JSON text file in order to attain
    data acquisition parameters required for reconstruction

    :param json_filename: file name containing metadata
    :return: dict of fields and their values, fields should include
     fs, c, axial_samples, num_beams, and beam_spacing
    """
    import json

    with open(json_filename) as f:
        metadata = json.load(f)

    return metadata
