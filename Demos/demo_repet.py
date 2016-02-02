import os
import nussl


def main():
    # input audio file
    inputName = '../Input/Sample1.wav'
    signal = nussl.AudioSignal(path_to_input_file=inputName)

    # make a directory to store output if needed
    if not os.path.exists('../Output/'):
        os.mkdir('../Output')

    # Set up window parameters
    win = nussl.WindowAttributes(signal.sample_rate)
    win.window_length = 2048
    win.window_type = nussl.WindowType.HAMMING

    # Set up Repet
    repet = nussl.Repet(signal, repet_type=nussl.RepetType.SIM, window_attributes=win)
    repet.min_distance_between_frames = 0.1
    # and Run
    repet.run()

    # Get foreground and backgroun audio signals
    bkgd, fgnd = repet.make_audio_signals()

    # and write out to files
    bkgd.write_audio_to_file(os.path.join('..', 'Output', 'repet_background.wav'))
    fgnd.write_audio_to_file(os.path.join('..', 'Output', 'repet_foreground.wav'))


if __name__ == '__main__':
    main()
