"""
    Используя Python реализовать алгоритм амплитудной модуляции

    Основные модули:
    carrier_generator.py - скрипт генерации несущей
    amplitude_modulation.py -
        а). Использовать для генерации написанный раннее скрипт
        б). Использовать записанные фразы как модулируемый сигнал
    band_pass_filter.py - просто фильтр, который обрезает частоты выше/ниже
        определенных значений
    adversarial_sample_generator.py - собственно генератор, который
        собирает в кучу все вышеописанные скрипты

    Вспомогательные модули:
    carrier.py -
        Просто описание класса несущей. Хранит частоту, sample rate и амплитуду
        По умолчанию использует функцию синуса
    plotter.py - все что связано с графиками
    file_manager.py - чтение/запись .wav файлов
    player.py - собственно проигрыватель
    const.py - хранит значение по умолчанию ключевых констант
               sample_rate, carrier_duration, ...

    сгенерировать сэмплы на списке несущих частот, в качестве проверки
    результатов использовать audacity

    Заметки:
        переменные с именем audio представляют из себя list вида:
            [sample_rate, audio_ndarray]
"""

import tests.test as tt

def main():
    # tt.carrier()
    # tt.carrier_am(frequency1 = 1, frequency2 = 10)
    # tt.am_test(carrier_frequency = 25000)
    tt.test_filter_with_carriers()


if __name__ == '__main__':
    main()
