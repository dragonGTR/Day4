"""modules"""
import re
import random
import string
import logging
from configparser import ConfigParser


class Testing:
    """Testing"""

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        """Read File Data"""
        file_data = open(self.filename, 'r')
        return file_data

    @staticmethod
    def write_file(filename, str1):
        """Write File Date"""
        file_name = open(filename.lower() + '.txt', "a")
        file_name.write(str(str1))
        file_name.close()


class PerformManipulation(Testing):
    """PerformanceManipulation"""

    # pylint:disable=useless-super-delegation
    def __init__(self, filename):
        super().__init__(filename)

    def file_data(self):
        """Read Data"""
        lines = self.read_file()
        line = lines.readlines()
        file_list = []

        for lines in line:
            result_data = lines.split(' ')
            file_list.extend(result_data)
        return file_list

    def line_data(self):
        """Read Line"""
        lines = self.read_file()
        line = lines.readlines()
        return line

    @staticmethod
    def generate_name():
        """Generate Name"""
        length = 5
        file_name = ''.join([random.choice(string.ascii_letters) for _ in range(length)])
        return file_name

    @staticmethod
    def write_result(str1):
        """Write into txt File"""
        log_name = CONFIG['logging name']['name2']
        logging.basicConfig(filename=log_name, level=logging.DEBUG)
        logging.debug(str1)
        name = PerformManipulation.generate_name()
        PerformManipulation.write_file(name, str1)

    def split_vowels(self):
        """Split Vowels"""
        vowels_list = []
        words = self.file_data()
        for i in enumerate(words):
            word1 = list(i)[1]
            result = re.split('a|e|i|o|u', word1)
            vowels_list.append(result)

        PerformManipulation.write_result(vowels_list)
        return vowels_list

    def capital_third_character(self):
        """3rd Capital Word"""
        str1 = ''
        words = self.file_data()
        for word in words:
            if len(word) >= 3:
                str1 += word[:2] \
                        + word[2].upper() \
                        + word[2 + 1:] + ' '
            else:
                str1 += word + ' '
        PerformManipulation.write_result(str1)
        return str1

    def capital_elements(self):
        """Fifth Capital Letter"""
        capital_list = []
        words = self.file_data()
        for num, element in enumerate(words):
            if num % 5 == 4:
                capital_list.append(element.upper())
            else:
                capital_list.append(element)
        PerformManipulation.write_result(capital_list)
        return capital_list

    def new_line(self):
        """new Line"""
        words = self.file_data()
        emp_list = []
        str_name = ''
        for i in enumerate(words):
            str_name += (''.join(list(i)[1] + '-'))
        emp_list.append(str_name)

        PerformManipulation.write_result(emp_list)
        return emp_list

    def semi_colon(self):
        """Semi-Colon"""
        list4 = []
        lines = self.line_data()
        for num, i in enumerate(lines):
            if len(lines) > 1:
                if num != len(lines) - 1:
                    list4.append(str(i) + ";")
                else:
                    list4.append(i)

        list4 = list4 if len(list4) != 0 else list4.append(lines)
        PerformManipulation.write_result(list4)
        return list4

    def __del__(self):
        print("Deleted")


FILE = 'config.ini'
CONFIG = ConfigParser()
CONFIG.read(FILE)
FILENAME = CONFIG['filename']['filename']
TEST = PerformManipulation(FILENAME)
TEST.split_vowels()
TEST.capital_third_character()
TEST.capital_elements()
TEST.new_line()
TEST.semi_colon()
del TEST
