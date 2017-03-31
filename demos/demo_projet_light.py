import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)

import nussl
print nussl

mixture = nussl.AudioSignal('../input/panned_mixture_four_sources.wav')

projet = nussl.ProjetLight(mixture, verbose = True, num_iterations = 200, num_sources = 4)
projet.run()
sources = projet.make_audio_signals()

for i,m in enumerate(sources):
    m.write_audio_to_file('output/projet_light_%d.wav' % i)
