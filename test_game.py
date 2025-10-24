"""
Unit tests for the `play_once` function in the guessing game module.

With help/inspiration from other repos
Comments in each function detail what correctly tested outputs should be

Contributions welcome! If you add new features to the game, please consider adding corresponding tests here.
"""

import unittest
from guess import play_once

class TestGuessingGame(unittest.TestCase):
    def test_invalid_range_returns_minus_one(self):
        """play_once should return -1 if low > high"""
        result = play_once(low=10, high=5)
        self.assertEqual(result, -1)  # Checks if result and -1 are equal

    def test_valid_range_returns_int(self):
        """play_once should return an int when range is valid"""
        result = play_once(low=1, high=10)
        self.assertIsInstance(result, int)  # Checks if the result is an integer

    def test_easy_difficulty_allows_more_tries(self):
        """play_once with 'easy' difficulty should still return an int"""
        result = play_once(low=1, high=10, difficulty="easy")
        self.assertIsInstance(result, int)

    def test_hard_difficulty_allows_fewer_tries(self):
        """play_once with 'hard' difficulty should still return an int"""
        result = play_once(low=1, high=10, difficulty="hard")
        self.assertIsInstance(result, int)
        
    def test_single_value_range(self):
        """Returns the single value when low == high."""
        result = play_once(low=7, high=7)
        self.assertEqual(result, 7, "Expected result to equal the only valid number in range")

    def test_non_integer_inputs_raise_error(self):
        """Raises TypeError when non-integer inputs are used."""
        with self.assertRaises(TypeError):  # Checks for a TypeError (passes if TypeError is raised)
            play_once(low="a", high="b")

if __name__ == "__main__":
    unittest.main()
