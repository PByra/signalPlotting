# Function definication for generating and plotting different types of signals
# This code generates and plots different types of signals: general, amplitude-modulated, frequency-modulated, and phase-modulated signals.
# It uses the numpy library for numerical operations and matplotlib for plotting.
# This a self learning code to broaden my understanding of signal processing and modulation techniques.
# Future work is to use with RF within my home for wireless communication and signal processing.

import matplotlib.pyplot as plt
import numpy as np

def general_signal():
    frequency = np.random.uniform(1000, 10000)  
    modulation_index = np.random.uniform(0, 1) 
    phase = np.random.uniform(0, 2 * np.pi)
    time = np.arange(0, 1000, 2)
    noise_index = np.random.random()
    noise = np.random.normal(0, noise_index, len(time))
    signal  = np.sin(2 * np.pi * frequency * time + phase) + noise   
    return signal, frequency, modulation_index, time, phase

def filter_signal(signal, cutoff_frequency, sampling_rate):
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff_frequency / nyquist
    b, a = signal.butter(1, normal_cutoff, btype='low', analog=False)
    filtered_signal = signal.filtfilt(b, a, signal)
    return filtered_signal

def amplitude_modulated_signal(frequency, modulation_index, time):
    carrier = np.cos(2 * np.pi * frequency * time)
    modulating_signal = 1 + modulation_index * carrier
    amSignal = carrier * modulating_signal
    return amSignal

def frequency_modulated_signal(frequency, modulation_index, time):
    modulating_signal = np.cos(2 * np.pi * frequency * time)
    instantaneous_frequency = frequency + modulation_index * modulating_signal
    fmSignal =np.cos(2 * np.pi * instantaneous_frequency * time)
    return fmSignal

def phase_modulated_signal(frequency, modulation_index, time):
    modulating_signal = np.cos(2 * np.pi * frequency * time)
    instantaneous_phase = 2 * np.pi * frequency * time + modulation_index * modulating_signal
    qamSignal = np.cos(instantaneous_phase)
    return qamSignal

def plot_signal(signal, time, title):
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()