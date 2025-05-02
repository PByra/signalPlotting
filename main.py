import signals

def main():
    signal, frequency, modulation_index, time, phase = signals.general_signal()
    signals.plot_signal(signal, time = time, title = "Random Signal")

if __name__ == "__main__":
    main()

