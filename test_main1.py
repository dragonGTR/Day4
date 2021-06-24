"""modules"""
import unittest
from configparser import ConfigParser
import pytest
import main2


class TestMain(unittest.TestCase):
    """main file operation"""

    @staticmethod
    def test_filename() -> None:
        """file_name"""
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        filename = config['filename']['filename']
        assert filename == 'py.txt'

    @staticmethod
    @pytest.mark.list
    def test_total() -> None:
        """vowels:list"""
        assert main2.PerformManipulation('py.txt').split_vowels() != []

    @staticmethod
    @pytest.mark.number
    def test_end() -> None:
        """capital_third_character"""
        assert main2.PerformManipulation('py.txt').capital_third_character() != ''

    @staticmethod
    @pytest.mark.list
    def test_maximum() -> None:
        """capital_elements"""
        assert main2.PerformManipulation('py.txt').capital_elements() != []

    @staticmethod
    @pytest.mark.list
    def test_palindrome() -> None:
        """new_line"""
        assert main2.PerformManipulation('py.txt').new_line() != []

    @staticmethod
    @pytest.mark.list
    def test_unique() -> None:
        """semi_colon"""
        assert main2.PerformManipulation('py.txt').semi_colon() != []
