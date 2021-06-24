"""modules"""
import unittest
from configparser import ConfigParser
import pytest
import main


class TestMain(unittest.TestCase):
    """main file operation"""

    @staticmethod
    def test_filename():
        """file_name"""
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        filename = config['filename']['filename']
        assert filename == 'py.txt'
        return filename

    @staticmethod
    @pytest.mark.number
    def test_total():
        """prefix_count"""
        assert TestMain.test_filename() == "py.txt"
        assert main.PerformManipulation(TestMain.test_filename()).count_prefix() >= 0

    @staticmethod
    @pytest.mark.number
    def test_end() -> None:
        """ends_count"""
        assert TestMain.test_filename() == 'py.txt'
        assert main.PerformManipulation(TestMain.test_filename()).ends_with() >= 0

    @staticmethod
    @pytest.mark.list
    def test_maximum() -> None:
        """maximum word"""
        assert TestMain.test_filename() == 'py.txt'
        assert main.PerformManipulation(TestMain.test_filename()).maximum_word() != []

    @staticmethod
    @pytest.mark.list
    def test_palindrome() -> None:
        """palindrome words"""
        assert TestMain.test_filename() == 'py.txt'
        assert main.PerformManipulation(TestMain.test_filename()).palindrome_words() != []

    @staticmethod
    @pytest.mark.list
    def test_unique() -> None:
        """unique list"""
        assert TestMain.test_filename() == 'py.txt'
        assert main.PerformManipulation(TestMain.test_filename()).unique_list() != []

    @staticmethod
    @pytest.mark.number
    def test_dict() -> None:
        """dict result"""
        assert TestMain.test_filename() == 'py.txt'
        dicts = main.PerformManipulation(TestMain.test_filename()).dict_index()
        assert len(dicts) != 0
