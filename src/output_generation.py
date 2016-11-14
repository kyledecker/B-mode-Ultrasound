import sys
import logging


def calc_ticks(image, dz=1, dx=1):
    """
    calculate axial and lateral mesh using image dimensions and input values
    for axial and lateral sampling intervals

    :param image: input image for display
    :param dz: axial sampling interval
    :param dx: lateral sampling interval
    :return: axi, lat (np.array)
    """
    import numpy as np

    image = np.array(image)
    xdim, zdim = image.shape

    # list lateral axis ticks
    if xdim % 2:
        x = np.array([dx*ii
                      for ii in range(int(-(xdim-1)/2), int((xdim-1)/2+1))])
    else:
        x = np.array([dx*(ii+0.5)
                      for ii in range(int(-xdim/2), int(xdim/2))])

    # list axial axis ticks
    z = np.array([dz*ii for ii in range(0, zdim)])

    axi, lat = np.meshgrid(z, x, indexing='xy')

    return axi, lat


def calc_b_geometry(fs, beam_spacing, c=1540., units='cm'):
    """
    calculate b-mode sample spacing with user specified units

    :param fs: rf sampling frequency (Hz)
    :param c: speed of sound (m/s)
    :param beam_spacing: spacing between lateral beams (m)
    :param units: units of output values
    :return: dz, dx (float)
    """

    if units == 'cm':
        scale = 100.
    elif units == 'mm':
        scale = 1000.
    elif units == 'm':
        scale = 1.
    else:
        msg = '[calc_b_geometry] Invalid unit type specified. Exiting ' \
              'script...'
        logging.error(msg)
        print(msg)
        sys.exit()

    c = float(c)
    beam_spacing = float(beam_spacing)
    fs = float(fs)

    dz = scale*c*1/fs/2
    dx = scale*beam_spacing
    logging.info('Axial tick size: ' + str(dz) + ' ' + units)
    logging.info('Lateral tick size: ' + str(dx) + ' ' + units)

    return dz, dx


def create_dir(filepath):
    """
    create new folder if directory in file path does not exist

    :param filepath: file path and name
    """
    import os
    out_dir = os.path.dirname(filepath)
    if not os.path.exists(out_dir):
        try:
            os.makedirs(out_dir)
        except:
            msg = '[create_dir] Failed to create ' + out_dir + \
                  '. Exiting script...'
            print(msg)
            logging.error(msg)
            sys.exit()


def generate_image(image, dz=1, dx=1, dynamic_range=[0, 1],
                   z_label='z', x_label='x', filename='./image.png',
                   save_flag=True, display_flag=False):
    """
    display/save output image with user-specified dynamic range

    :param image: input image for display
    :param dz: axial sampling interval
    :param dx: lateral sampling interval
    :param dynamic_range: displayed dynamic range
    :param z_label: label for z (axial) axis
    :param x_label: label for x (lateral) axis
    :param filename: file path and name of saved .png
    :param save_flag: enable to save .png
    :param display_flag: enable to display image
    """
    if not display_flag:
        import matplotlib
        matplotlib.use('Agg')
        msg = '[generate_image] Using Agg matplotlib backend.'
        print(msg)
        logging.warning(msg)

    import matplotlib.pyplot as plt

    axi, lat = calc_ticks(image, dz, dx)

    if dynamic_range[0] > dynamic_range[1]:
        tmp = dynamic_range
        dynamic_range[0] = tmp[1]
        dynamic_range[1] = tmp[0]
        msg = '[generate_image] Dynamic range bounds out of order. ' \
              'Reversing bounds for display...'
        print(msg)
        logging.warning(msg)

    plt.pcolormesh(lat, axi, image, cmap='gray', vmin=dynamic_range[0],
                   vmax=dynamic_range[1])
    plt.axis('image')
    plt.xlabel(x_label)
    plt.ylabel(z_label)
    plt.colorbar()
    plt.gca().invert_yaxis()

    if save_flag:
        create_dir(filename)
        plt.savefig(filename)
        msg = '[generate_image] PNG file saved to ' + filename
        logging.info(msg)
        print(msg)

    if display_flag:
        try:
            plt.show()
        except:
            msg = '[generate_image] matplotlib backend failed to display ' \
                  'image. Exiting script...'
            logging.error(msg)
            print(msg)
            sys.exit()
