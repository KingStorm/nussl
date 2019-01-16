#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for nussl/utils.py
"""

import unittest
import nussl
import numpy as np
import os
import librosa

class TestUtils(unittest.TestCase):
    """

    """

    def test_find_peak_indices(self):
        array = np.arange(0, 100)
        peak = nussl.utils.find_peak_indices(array, 1)[0]
        assert peak == 99

        array = np.arange(0, 100).reshape(10, 10)
        peak = nussl.utils.find_peak_indices(array, 3, min_dist=0)
        assert peak == [[9, 9], [9, 8], [9, 7]]

    def test_find_peak_values(self):
        array = np.arange(0, 100)
        peak = nussl.utils.find_peak_values(array, 1)[0]
        assert peak == 99

        array = np.arange(0, 100).reshape(10, 10)
        peak = nussl.utils.find_peak_values(array, 3, min_dist=0)
        assert peak == [99, 98, 97]

    def test_add_mismatched_arrays(self):
        long_array = np.ones((20,))
        short_array = np.arange(10)
        expected_result = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=float)

        # Test basic cases
        result = nussl.utils.add_mismatched_arrays(long_array, short_array)
        assert all(np.equal(result, expected_result))

        result = nussl.utils.add_mismatched_arrays(short_array, long_array)
        assert all(np.equal(result, expected_result))

        expected_result = expected_result[:len(short_array)]

        result = nussl.utils.add_mismatched_arrays(long_array, short_array, truncate=True)
        assert all(np.equal(result, expected_result))

        result = nussl.utils.add_mismatched_arrays(short_array, long_array, truncate=True)
        assert all(np.equal(result, expected_result))

        # Test complex casting
        short_array = np.arange(10, dtype=complex)
        expected_result = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=complex)

        result = nussl.utils.add_mismatched_arrays(long_array, short_array)
        assert all(np.equal(result, expected_result))

        result = nussl.utils.add_mismatched_arrays(short_array, long_array)
        assert all(np.equal(result, expected_result))

        expected_result = expected_result[:len(short_array)]

        result = nussl.utils.add_mismatched_arrays(long_array, short_array, truncate=True)
        assert all(np.equal(result, expected_result))

        result = nussl.utils.add_mismatched_arrays(short_array, long_array, truncate=True)
        assert all(np.equal(result, expected_result))

        # Test case where arrays are equal length
        short_array = np.ones((15,))
        expected_result = short_array * 2

        result = nussl.utils.add_mismatched_arrays(short_array, short_array)
        assert all(np.equal(result, expected_result))

        result = nussl.utils.add_mismatched_arrays(short_array, short_array, truncate=True)
        assert all(np.equal(result, expected_result))

    def test_musdb_track(self):
        signal = nussl.AudioSignal(librosa.util.example_audio_file())

        repet = nussl.Repet(signal)
        repet.run()

        bg, fg = repet.make_audio_signals()

        src_dict = {'vocals': fg, 'accompaniment': bg}
        target = nussl.core.constants.STEM_TARGET_DICT
        track = nussl.utils.audio_signals_to_musdb_track(signal, src_dict, target)

        i = 0

    def test_all_algorithms(self):
        l = len(nussl.separation.all_separation_algorithms)
        i = 0
