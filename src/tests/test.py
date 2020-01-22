import modules.carrier as crr
import modules.plotter as plt
import modules.file_manager as fm
import modules.amplitude_modulation as am
import modules.band_pass_filter as bpf
import modules.const as const

def test_carrier_class():
    carrier = crr.Carrier(440)
    print(carrier)
    plt.show_carrier(carrier)

def test_amplidute_modulation_with_carriers(frequency1, frequency2):
    carrier1 = crr.Carrier(frequency = frequency1)
    carrier2 = crr.Carrier(frequency = frequency2)

    # plt.show_carrier(carrier1)
    # plt.show_carrier(carrier2)

    # plt.plot_frequency([carrier1.sample_rate, carrier1.data])
    # plt.plot_frequency([carrier2.sample_rate, carrier2.data])

    plt.subplot_audio_and_frequency([carrier1.sample_rate, carrier1.data])
    plt.subplot_audio_and_frequency([carrier2.sample_rate, carrier2.data])

    audio = [carrier1.sample_rate, carrier1.data]
    am_audio = am.am_algorithm(audio, carrier2)
    plt.subplot(audio, am_audio)

def test_amplidute_modulation_with_wav(carrier_frequency):
    carrier = crr.Carrier(frequency = carrier_frequency)
    # plt.show_carrier(carrier)

    audio = fm.open("../data/test/OKGOOGLE.wav", carrier.sample_rate)
    # plt.plot_audio(audio)

    am_audio = am.am_algorithm(audio, carrier)
    # plt.plot_audio(am_audio)

    plt.subplot(audio, am_audio)
    plt.plot_frequency(audio)
    # plt.plot_frequency(am_audio)

    fm.write("../data/test/am_OKGOOGLE.wav", am_audio)
    test_filter(audio)
    test_filter(am_audio)

def test_filter_with_audio(audio):
    audio = bpf.filter(audio)
    plt.subplot_audio_and_frequency(audio)
    fm.write(const.location() + "test_filter_audio.wav", audio)

def test_filter_with_carriers():
    # Create some simple wave
    carrier1 = crr.Carrier(1500)
    plt.subplot_audio_and_frequency([carrier1.sample_rate, carrier1.data])
    carrier2 = crr.Carrier(2100)
    plt.subplot_audio_and_frequency([carrier2.sample_rate, carrier2.data])

    # Concatenate this wave
    carrier = carrier1 * carrier2
    plt.subplot_audio_and_frequency([carrier.sample_rate, carrier.data])

    # Filter merged wave
    audio = bpf.filter([carrier.sample_rate, carrier.data])
    plt.subplot_audio_and_frequency(audio)
    fm.write(const.location() + "test_filter_carriers.wav", audio)
