#Defining of Signals based on parameters 
import matplotlib.pyplot as plt
import numpy as np

def general_signal():
    frequency = np.random.uniform(3000, 4000)  
    modulation_index = np.random.uniform(0, 1) 
    phase = np.random.uniform(0, 2 * np.pi)
    time = np.arange(0, 1000, 2)
    signal  = np.sin(2 * np.pi * frequency * time + phase)
    print(len(signal))    
    return signal, frequency, modulation_index, time, phase

def amplitude_modulated_signal(frequency, modulation_index, time):
    carrier = np.cos(2 * np.pi * frequency * time)
    modulating_signal = 1 + modulation_index * carrier
    return carrier * modulating_signal

def frequency_modulated_signal(frequency, modulation_index, time):
    modulating_signal = np.cos(2 * np.pi * frequency * time)
    instantaneous_frequency = frequency + modulation_index * modulating_signal
    return np.cos(2 * np.pi * instantaneous_frequency * time)

def phase_modulated_signal(frequency, modulation_index, time):
    modulating_signal = np.cos(2 * np.pi * frequency * time)
    instantaneous_phase = 2 * np.pi * frequency * time + modulation_index * modulating_signal
    return np.cos(instantaneous_phase)

def plot_signal(signal, time, title):
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()