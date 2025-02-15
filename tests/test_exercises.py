import unittest
import src
from src import exercises


class TestExercise(unittest.TestCase):

    def setUp(self):
        pass  # Do initial common setup here, if needed

    def test_reverse_list(self):
        expected = [5, 4, 3, 2, 1]
        actual = exercises.reverse_list([1, 2, 3, 4, 5])
        self.assertEqual(expected, actual)

        expected = [6, 5, 4, 3, 2, 1]
        actual = exercises.reverse_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(expected, actual) 

    def test_count_digits(self):
        number = 123
        expected = 3
        actual = exercises.count_digits(number)
        self.assertEqual(expected, actual)

    def tearDown(self):
        pass   # If needed, do final unstubbing/unmocking here, like calling unittest.unstub()


if __name__ == '__main__':
    unittest.main()