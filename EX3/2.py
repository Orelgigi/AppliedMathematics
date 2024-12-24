import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import common as cm


# session A
def chirp_gen(dur, f0, mi, fs):
    """
    Generate a chirp signal (frequency-modulated signal)
    """
    tt = np.linspace(0, dur,int(fs * dur))
    sig = np.cos(2 * np.pi * f0 * tt + 2 * np.pi * mi * tt ** 2)
    return sig, tt


# session B+C
def plot_chirp():
    """
    Plot segments of the chirp signal and play it
    """
    signal, t = chirp_gen(cm.DUR, cm.F0, cm.U, cm.FS)
    lenS = len(signal)
    fig, axes = plt.subplots(3, 1, figsize=(17, 11))
    fig.suptitle('***2b***', fontsize=16)
    axes[0].plot(t[:cm.F0], signal[:cm.F0])
    axes[0].set_title('Initial Chirp Signal')
    axes[1].plot(t[((lenS // 2) - 250):((lenS // 2) + 250)], signal[((lenS // 2) - 250):((lenS // 2) + 250)])
    axes[1].set_title('Middle Chirp Signal')
    axes[2].plot(t[lenS - cm.F0:], signal[lenS - cm.F0:])
    axes[2].set_title('Final Chirp Signal')
    # sd.play(signal, cm.FS)  # Play the chirp signal
    plt.show()
    return signal, t


# session D
def noise():
    """
    Generate noise and add chirp signal to it
    """
    chirp_noise = np.random.random(20 * cm.FS)
    chirp_sig, t = chirp_gen(cm.DUR, cm.F0, cm.U, cm.FS)
    chirp_noise[int(12 * cm.FS):int(12.7 * cm.FS)-1] += (chirp_sig * 0.35)  # Add chirp signal to noise
    return chirp_noise


# session E+F
def find_chirp(noise_s, chirp_s, fs, frame, step=100):
    """
    And extract the "chirp" signal from the noise using a correlation calculation and display the result on a graph.
    """
    sec = len(noise_s) / fs
    len_step = int((fs * sec - frame) / step)
    ip = np.zeros(len_step)
    for i in range(len_step):
        xtest = noise_s[i * step:i * step + frame]
        ip[i] = np.inner(xtest, chirp_s)   # Compute inner product (correlation)
    max_index = np.argmax(ip)
    max_value = ip[max_index]
    max_time = (max_index * step) / fs
    timeIp = np.arange(len_step) * step / fs
    plt.plot(timeIp, ip)
    plt.scatter(max_time, max_value, color="red", label=f"Max ({max_time}s, {max_value})")  # Mark max value on plot
    plt.title("Normalized Correlation vs Time  ***2e+2f***")
    plt.xlabel("Time")
    plt.ylabel("Normalized Correlation")
    plt.grid(True)
    plt.legend()
    plt.show()
    return max_value, max_time


if __name__ == '__main__':
    print("*****2*****")
    print("*****2a+2b+2c*****")
    chirp_signal, time_s = plot_chirp()
    print("*****2d*****")
    noise_signal = noise()
    print("*****2e*****")
    place_signal, time_chirp_find = find_chirp(noise_signal, chirp_signal, cm.FS, int(cm.DUR * cm.FS))
    print(time_chirp_find, place_signal)
    print("*****2f*****")
    chirp = np.load('chirp.npy')
    xnsig = np.load('xnsig.npy')
    place_signal, time_chirp_find = find_chirp(xnsig, chirp, cm.FS, int(cm.DUR * cm.FS))
    print(time_chirp_find, place_signal)
