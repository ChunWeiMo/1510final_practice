import io
import os
from unittest import TestCase
from unittest import main
from unittest.mock import patch
from caeser import caesar


class TestCaesar(TestCase):
    def test_file_not_exist(self):
        filename = 'not_exist.txt'
        shift = 1
        caesar(filename, shift)
        self.assertFalse(os.path.isfile(filename))
        

if __name__ == '__main__':
    main()