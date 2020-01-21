import scipy.io.wavfile as scipy_wf
import librosa as lbr


def write(filename, audio):
    sample_rate = audio[0]
    data = audio[1]

    scipy_wf.write(filename, sample_rate, data)

def open(filename, sample_rate):
    x = lbr.load(filename, sr = sample_rate)
    return [x[-1], x[0]]
