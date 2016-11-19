import sys
import logging


def lp_filter(signal, fs, cutoff=20., order=5):
    """
    low pass filter signal with specified cutoff frequency

    :param signal: input signal
    :param fs: sampling frequency (Hz)
    :param cutoff: cutoff frequency (Hz)
    :param order: filter order
    :returns: filtered_signal (np.array)
    """
    from scipy.signal import butter
    from scipy.signal import filtfilt

    try:
        fnyquist = fs / 2
    except ZeroDivisionError:
        msg = '[lp_filter] Invalid sampling frequency (fs = 0). ' \
              'Exiting script...'
        logging.error(msg)
        print(msg)
        sys.exit()

    if cutoff < 0:
        cutoff = 0
        logging.debug('[lp_filter] Cut-off frequency < 0 Hz. '
                      'Setting cut-off to 0 Hz.')
    elif cutoff > fnyquist:
        cutoff = fnyquist
        logging.debug('[lp_filter] Cut-off frequency > Nyquist. '
                      'Setting cut-off to Nyquist.')

    wn = cutoff / fnyquist

    b, a = butter(order, wn, btype='low')
    filtered_signal = filtfilt(b, a, signal)

    return filtered_signal
