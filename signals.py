#Defining of Signals based on parameters 

import numpy as np
import matplotlib.pyplot as plt

def amplitude_modulated_signal(frequency, modulation_index, time):
    carrier = np.cos(2 * np.pi * frequency * time)
    modulating_signal = 1 + modulation_index * np.cos(2 * np.pi * frequency * time)
    return carrier * modulating_signal

def frequency_modulated_signal(frequency, modulation_index, time):
    modulating_signal = np.cos(2 * np.pi * frequency * time)
    instantaneous_frequency = frequency + modulation_index * modulating_signal
    return np.cos(2 * np.pi * instantaneous_frequency * time)

