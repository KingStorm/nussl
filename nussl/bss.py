# -*- coding: utf-8 -*-

import os
import nussl
import numpy as np

def main():
    # Load input file
    #input_file_name = os.path.join('..', 'input', 'se_noisy_crop.wav')
    signal = nussl.AudioSignal(path_to_input_file='se_noisy_crop.wav')

    # make a directory to store output if needed
    if not os.path.exists(os.path.join('bss_output/')):
        os.mkdir(os.path.join('bss_output/'))

    # Set up NMMF MFCC
    # nmf_mfcc = nussl.NMF_MFCC(signal, num_sources=2, num_templates=6, distance_measure="euclidean",
    #                          num_iterations=10, random_seed=0)
    nmf_mfcc = nussl.NMF_MFCC(signal, num_sources=2, num_templates=6, distance_measure="euclidean",
                              num_iterations=30, random_seed=0)

    # and run
    nmf_mfcc.run()
    sources = nmf_mfcc.make_audio_signals()
    for i, source in enumerate(sources):
        output_file_name = str(i) + '.wav'
        source.write_audio_to_file(output_file_name)

if __name__ == '__main__':
    main()
