import io
import os
from unittest import TestCase
from unittest import main
from unittest.mock import patch    
    
# ======================================================================
# test while loop continue asking input
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[5])
    def test_input_not_illegal(self, _, mock_output):
        with self.assertRaises(StopIteration):
            get_user_choice()

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[5, 1])
    def test_input_not_illegal_print_message(self, _, mock_output):
        get_user_choice()
        expected_message = 'The direction you can choose 0: North, 1: East, 2: South, 3: West\n\n\n'
        expected_message += 'Incorrect input, try again.\n\n'
        expected_message += 'The direction you can choose 0: North, 1: East, 2: South, 3: West\n\n\n'
        self.assertEqual(expected_message, mock_output.getvalue())
        
    
# ======================================================================
# test True / False
class TestIsPalindrome(TestCase):
    def test_empty_str(self):
        self.assertTrue(is_palindrome(''))
    
    def test_not_palindrome_and_len_greater_than_2(self):
        self.assertFalse(is_palindrome('abcdefg'))
        
# ======================================================================
# test file exist or not
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



# ======================================================================
# test call the next function assert_called9)
    def test_call_sum_of_integers(self):
        with unittest.mock.patch('process_reading.sum_of_integers') as mock_sum_of_integers:
            process_readings(self.temp_file_name)
            mock_sum_of_integers.assert_called()
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)