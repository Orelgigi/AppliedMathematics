import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time

Fs = 44100
Ts = 1 / Fs


def print_ans_sound(t, y, str_title, slicing=0, d=0):
    """
    Play a sound and plot its waveform.
    :param t: array-like The time values corresponding to the sound waveform.
    :param y: array-like The sound waveform values.
    :param str_title: str The title of the plot.
    :param slicing: int, optional (default=0)
    If 0, the entire waveform is plotted. Otherwise, specifies the number of points to include in the plot.
    :param d: float, optional (default=0) If not 0, the duration (in seconds) for which to wait after playing the sound.
    :return: None
    """
    sd.play(y, Fs)
    if d != 0:
        sd.wait(d)
    if slicing == 0:
        plt.plot(t, y)
    else:
        plt.plot(t[:slicing], y[:slicing])
    plt.grid(axis='both')
    plt.title(str_title)
    plt.show()
    time.sleep(1)


def cos_fr(from_t, to_t, cycle):
    """
    Generates a cosine wave at a specified frequency.
    :param from_t: Start time
    :param to_t: End time
    :param cycle: Frequency of the wave (Hz)
    :return: Array representing the cosine wave
    """
    t = np.arange(from_t, to_t, Ts)
    y = np.cos(2 * np.pi * cycle * t)
    return y


def cos_section2():
    """
    Plays cosine waves at frequencies increasing from 500 Hz to 20000 Hz in steps of 500 Hz.
    Each wave is displayed in a graph and played for one second.
    """
    t = np.arange(0, 1, Ts)
    for f0 in range(500, 20001, 500):
        y = cos_fr(0, 1, f0)
        title = '3_2 cosine function with freq = ' + str(f0)
        print_ans_sound(t, y, title, 100)


def cos_section3():
    """
    Plays cosine waves with frequencies increasing according to a musical scale
    (each step is a semitone higher).
    """
    t = np.arange(0, 1, Ts)
    f0 = 440
    while f0 < 20000:
        y = cos_fr(0, 1, f0 * 2 ** (1 / 12))
        title3 = '3_3 cosine function with freq = ' + str(f0 * 2 ** (1 / 12))
        print_ans_sound(t, y, title3, 100)
        f0 *= 2 ** (1 / 12)


def music():
    """
    Plays a melody defined by an array of frequencies and corresponding durations for each note.
    Each note is displayed in a graph and played for its specified duration.
    """
    frequencies = [784, 880, 988, 1047, 988, 880, 784, 988, 880, 784, 0, 784, 880, 988, 1047, 988, 880, 784, 988, 880,
                   784, 0, 880, 988, 1047, 1175, 1047, 988, 880, 784, 880, 988, 0,
                   988, 880, 784, 988, 880, 784, 0]
    durations = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25,
                 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25,
                 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25]
    for i in range(len(frequencies)):
        ys = cos_fr(0, 1, frequencies[i])
        t = np.arange(0, 1, 1 / 10000)
        titled = 'cosine function with freq = '+str(frequencies[i])
        print_ans_sound(t, ys, titled, 100, durations[i])


if __name__ == '__main__':
    # Section 1: Play a cosine wave at 440 Hz
    y1 = cos_fr(0, 1, 440)
    t1 = np.arange(0, 1, Ts)
    title1 = '3_1 cosine function with freq = 440'
    print_ans_sound(t1, y1, title1)

    # Display a small segment of the wave at 440 Hz (11)
    title2 = '3_1 cosine function with freq = 440'
    print_ans_sound(t1, y1, title2, int((11/440)*Fs))

    # Section 2: Play waves with increasing frequencies from 500 Hz to 20000 Hz
    cos_section2()

    # Section 3: Play waves according to a musical scale
    cos_section3()

    # Section 3 (part b): Play a melody
    music()
