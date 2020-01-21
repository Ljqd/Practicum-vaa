import matplotlib.pyplot as plt
import scipy.fftpack as sc_fft

def show_carrier(carrier):
    plt.plot(carrier.data)
    plt.xlabel("Sample")
    plt.ylabel("Wave")
    plt.show()

def plot_audio(audio):
    plt.plot(audio[1])
    plt.xlabel("Sample")
    plt.ylabel("Wave")
    plt.show()

def subplot(audio, am_audio):
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(audio[1])
    ax[1].plot(am_audio[1])
    plt.show()

def plot_frequency(audio):
    sample_rate = audio[0]
    data = audio[1]

    X = sc_fft.fft(data)
    frequencies = sc_fft.fftfreq(len(X)) * sample_rate

    plt.plot(frequencies, abs(X))
    plt.show()
