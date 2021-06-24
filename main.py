"""imports"""
from configparser import ConfigParser
from collections import Counter
import logging


# pylint: disable=too-few-public-methods
class Testing:
    """Testing"""

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        """read file data"""
        file_data = open(self.filename, 'r')
        return file_data


class PerformManipulation(Testing):
    """Performance"""

    # pylint: disable=useless-super-delegation
    def __init__(self, filename):
        super(PerformManipulation, self).__init__(filename)

    def file_data(self):
        """Add data to the list"""
        lines = self.read_file()
        lines = lines.readlines()
        words_list = []

        for line in lines:
            result_data = line.split(' ')
            words_list.extend(result_data)

        return words_list

    def count_prefix(self):
        """Prefix count"""
        result_data = self.file_data()
        prefix_count = 0
        for i in range(len(result_data)):
            if i != 0:
                if result_data[i - 1] == 'to':
                    prefix_count += 1
        return prefix_count

    def ends_with(self):
        """Ends with ing"""
        result_data = self.file_data()
        end_count = 0
        for i in enumerate(result_data):
            if list(i)[1].endswith("ing"):
                end_count += 1

        return end_count

    def maximum_word(self):
        """Maximum count words"""
        result_data = self.file_data()
        c_data = Counter(result_data)
        return c_data.most_common(1)

    def palindrome_words(self):
        """Palindrome words"""
        result_data = self.file_data()
        str1 = []
        palindrome = 0
        for number, i in enumerate(result_data):
            if (i[::-1]
                    == i):
                palindrome += 1
                str1.append(i)
        str1 = str1.append("No Palindrome") if str1 == [] else str1
        return str1

    def unique_list(self):
        """Generate Unique list"""
        result_data = self.file_data()
        set1 = set(result_data)
        unique_list2 = list(set1)
        return unique_list2

    def dict_index(self):
        """Counter index"""
        result_data = self.file_data()
        word_data = dict()
        count = 0
        for line in result_data:
            words = line.split(" ")
            for word in words:
                word_data[count] = word
                count += 1
        return word_data

    # pylint: disable = too-many-arguments
    @staticmethod
    def display_results(
            prefix,
            end, max1,
            palindrome, unique, dicts):
        """Display results"""
        log_name = CONFIG['logging name']['name1']
        print(type(log_name))
        logging.basicConfig(filename=log_name, level=logging.DEBUG)
        logging.debug(prefix)
        logging.info(end)
        logging.warning(max1)
        logging.critical(palindrome)
        logging.error(unique)
        logging.debug(dicts)

    def __del__(self):
        print("Deleted")


FILE = 'config.ini'
CONFIG = ConfigParser()
CONFIG.read(FILE)
FILE_NAME = CONFIG['filename']['filename']
print(FILE_NAME)

TEST = PerformManipulation(FILE_NAME)
NUM_PREFIX = TEST.count_prefix()
ENDS_WITH = TEST.ends_with()
MAX_COUNT = TEST.maximum_word()
PALINDROME_WORDS = TEST.palindrome_words()
UNIQUE_SET = TEST.unique_list()
DICT_INDEX = TEST.dict_index()
TEST.display_results(
    NUM_PREFIX, ENDS_WITH,
    MAX_COUNT, PALINDROME_WORDS,
    UNIQUE_SET, DICT_INDEX)
del TEST
