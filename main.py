# Main function to run the signal generation and plotting


import signals

def main():
    rawSignal, frequency, modulation_index, time, phase = signals.general_signal()
    amSignal = signals.amplitude_modulated_signal(frequency=frequency, modulation_index=modulation_index, time=time)
    fmSignal = signals.frequency_modulated_signal(frequency=frequency, modulation_index=modulation_index, time=time)
    qamSignal = signals.phase_modulated_signal(frequency=frequency, modulation_index=modulation_index, time=time)
    signals.plot_signal(rawSignal, time = time, title = "Random Signal")
    signals.plot_signal(amSignal, time = time, title = "AM Signal")
    signals.plot_signal(fmSignal, time = time, title = "FM Signal")
    signals.plot_signal(qamSignal, time = time, title = "QAM Signal")


if __name__ == "__main__":
    main()