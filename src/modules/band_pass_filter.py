import numpy as np
import scipy.fftpack as sc_fft
import scipy.signal as sc_sgn

import modules.plotter as plt
import modules.const as const

def butter_bandpass(lowcut, highcut, sample_rate, order = 10):
    nyq = 0.5 * sample_rate
    low = lowcut / nyq
    high = highcut / nyq
    b, a = sc_sgn.butter(order, [low, high], btype='band')
    return [b, a]


def filter(audio):
    lowcut = const.filter_low() / 10
    highcut = const.filter_high() / 10
    sample_rate = audio[0]
    data = audio[1]

    b, a = butter_bandpass(lowcut, highcut, sample_rate)
    result = sc_sgn.lfilter(b, a, data)
    return [sample_rate, result]
