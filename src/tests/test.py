import modules.carrier as crr
import modules.plotter as plt
import modules.file_manager as fm
import modules.amplitude_modulation as am

def carrier_test():
    carrier = crr.Carrier(440)
    print(carrier)
    plt.show_carrier(carrier)


def carrier_am(frequency1, frequency2):
    carrier1 = crr.Carrier(frequency = frequency1)
    carrier2 = crr.Carrier(frequency = frequency2)

    plt.show_carrier(carrier1)
    plt.show_carrier(carrier2)

    # plt.plot_frequency([carrier1.sample_rate, carrier1.data])
    # plt.plot_frequency([carrier2.sample_rate, carrier2.data])

    audio = [carrier1.sample_rate, carrier1.data]
    am_audio = am.am_algorithm(audio, carrier2)
    plt.subplot(audio, am_audio)


def am_test(carrier_frequency):
    carrier = crr.Carrier(frequency = carrier_frequency)
    # plt.show_carrier(carrier)

    audio = fm.open("../data/test/OKGOOGLE.wav", carrier.sample_rate)
    # plt.plot_audio(audio)

    am_audio = am.am_algorithm(audio, carrier)
    # plt.plot_audio(am_audio)

    plt.subplot(audio, am_audio)
    plt.plot_frequency(audio)
    plt.plot_frequency(am_audio)

    fm.write("../data/test/am_OKGOOGLE.wav", am_audio)
