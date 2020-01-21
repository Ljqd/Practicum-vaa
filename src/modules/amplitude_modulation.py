import numpy as np

import modules.const as const
import modules.plotter as plt

def am_algorithm(audio, carrier):
    sample_rate = audio[0]
    samples = len(audio[1])
    result = np.linspace(0, samples / sample_rate, samples) # time

    audio_amlitude = max(audio[1])
    for i in range(len(result)):
        result[i] = carrier[result[i]] * (
            1 + const.amplitude_coef() * audio[1][i] / audio_amlitude
            ) * audio_amlitude / carrier.amplitude
    return [sample_rate, result]
