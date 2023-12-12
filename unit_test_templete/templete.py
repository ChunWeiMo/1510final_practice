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