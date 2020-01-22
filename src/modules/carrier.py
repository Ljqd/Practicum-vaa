# Python modules
import numpy as np


# Custom modules
import modules.const as const


class Carrier:
    def __init__(self, frequency, amplitude = 1,
        sample_rate = const.default_sample_rate()
        ):
        # just for demonstrating signal, if needed
        self.__duration = const.carrier_duration()
        self.__frequency = frequency
        self.__amplitude = amplitude
        self.__sample_rate = sample_rate
        self.__data = self.__create_carrier(sample_rate)

    def __create_carrier(self, sample_rate):
        time = np.linspace(0, self.__duration, self.__duration * sample_rate)
        data = self.__amplitude * np.sin(2 * np.pi * self.__frequency * time)
        return data

    def __getitem__(self, t):
        res = self.__amplitude * np.sin(2 * np.pi * self.__frequency * t)
        return res

    def __str__(self):
        return "Wave with a frequency {} and a sample rate {}".format(
            self.__frequency, self.__sample_rate
        )

    # Because carriers created with same sample rates and durations,
    # we can add and sub its without modification
    def __add__(self, carrier):
        if self.__sample_rate == carrier.sample_rate:
            result = Carrier(0)
            rd = self.__data + carrier.data
            rampl = max(rd) if max(rd) > abs(min(rd)) else abs(min(rd))

            result.set([self.__sample_rate, rd, rampl])
            return result

    def __sub__(self, carrier):
        if self.__sample_rate == carrier.sample_rate:
            result = Carrier(0)
            rd = self.__data - carrier.data
            rampl = max(rd) if max(rd) > abs(min(rd)) else abs(min(rd))

            result.set([self.__sample_rate, rd, rampl])
            return result

    def __mul__(self, carrier):
        if self.__sample_rate == carrier.sample_rate:
            result = Carrier(0)
            rd = np.concatenate((self.__data, carrier.data))
            rampl = max(rd) if max(rd) > abs(min(rd)) else abs(min(rd))

            result.set([self.__sample_rate, rd, rampl], True)
            return result


    # Test func, temp
    def set(self, carrier_fields : list, duration = False):
        # [sample_rate, data, amplitude]
        if duration: self.__duration = 2 * self.__duration
        self.__sample_rate = carrier_fields[0]
        self.__data = carrier_fields[1]
        self.__amplitude = carrier_fields[2]

    @property
    def duration(self):
        return self.__duration

    @property
    def frequency(self):
        return self.__frequency

    @property
    def amplitude(self):
        return self.__amplitude

    @property
    def sample_rate(self):
        return self.__sample_rate

    @property
    def data(self):
        return self.__data
