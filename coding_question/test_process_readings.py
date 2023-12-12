import io
import os
import unittest
from unittest import TestCase
from unittest import main
from unittest.mock import patch
from process_reading import process_readings


class TestProcessReadings(TestCase):
    def setUp(self) -> None:
        self.temp_file_name = "temp_test_file.txt"
        with open(self.temp_file_name, 'w') as f:
            f.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n")
    
    def test_reading_file_failed(self):
        process_readings("not_exist.txt")
        self.assertFalse(os.path.isfile("not_exist.txt"))
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)

    def test_reading_file_successful(self):
        process_readings(self.temp_file_name)
        self.assertTrue(os.path.isfile(self.temp_file_name))
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)

    def test_call_sum_of_integers(self):
        with unittest.mock.patch('process_reading.sum_of_integers') as mock_sum_of_integers:
            process_readings(self.temp_file_name)
            mock_sum_of_integers.assert_called()
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)

if __name__ == '__main__':
    main()