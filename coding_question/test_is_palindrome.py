import io
import os
from unittest import TestCase
from unittest import main
from unittest.mock import patch
from is_palindrome import is_palindrome


class TestIsPalindrome(TestCase):
    def test_empty_str(self):
        self.assertTrue(is_palindrome(''))

    def test_len_1_str(self):
        self.assertTrue(is_palindrome('a'))

    def test_is_palindrome_and_len_greater_than_2(self):
        self.assertTrue(is_palindrome('abba'))

    def test_not_palindrome_and_len_greater_than_2(self):
        self.assertFalse(is_palindrome('abcdefg'))
        
    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome(
            'a man a plan a canal panama'.replace(' ', '')))


        
if __name__ == '__main__':
    main()
    