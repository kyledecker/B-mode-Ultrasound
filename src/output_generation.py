def calc_ticks(image, dz=1, dx=1):
    """
    calculate axis tick values using image dimensions and input values for
    axial and lateral sampling intervals

    :param image: input image for display
    :param dz: axial sampling interval
    :param dx: lateral sampling interval
    :return: axi, lat (np.array)
    """
    import numpy as np

    image = np.array(image)
    zdim, xdim = image.shape

    axi = np.array([dz*ii for ii in range(0, zdim)])
    lat = np.array([dx*ii for ii in range(0, xdim)])

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
        scale = 10.
    elif units == 'mm':
        scale = 100.
    elif units == 'm':
        scale = 1.

    c = float(c)
    beam_spacing = float(beam_spacing)
    fs = float(fs)

    dz = scale*c*1/fs/2
    dx = scale*beam_spacing

    return dz, dx


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
    :param filename: location and name of saved .png
    :param save_flag: enable to save .png
    :param display_flag: enable to display image
    """
    import numpy as np
    import matplotlib.pyplot as plt

    axi, lat = calc_ticks(image, dz, dx)

    x, z = np.meshgrid(lat, axi, indexing='xy')

    plt.pcolormesh(z, x, image, cmap='gray', vmin=dynamic_range[0],
                   vmax=dynamic_range[1])
    plt.axis('image')
    plt.xlabel(x_label)
    plt.ylabel(z_label)
    plt.colorbar()

    if save_flag:
        plt.savefig(filename)

    if display_flag:
        plt.show()
