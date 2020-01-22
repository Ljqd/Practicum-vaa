import numpy as np
import scipy.fftpack as sc_fft
import scipy.signal as sc_sgn

import modules.plotter as plt
import modules.const as const

def butter_bandpass(lowcut, highcut, sample_rate, order = 10):
    sr = sample_rate / 2
    b, a = sc_sgn.butter(order, [lowcut / sr, highcut / sr], btype='band')
    return [b, a]


def filter(audio):
    lowcut = const.filter_low() / 1000
    highcut = const.filter_high() / 1000
    sample_rate = audio[0]
    data = audio[1]

    # b, a = butter_bandpass(lowcut, highcut, sample_rate)
    # result = sc_sgn.lfilter(b, a, data)
    sos = sc_sgn.butter(
        N = 15,
        Wn = lowcut,
        btype = 'highpass',
        fs = sample_rate,
        output='sos'
        )
    result = sc_sgn.sosfilt(sos, data)
    return [sample_rate, result]
