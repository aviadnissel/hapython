import unittest
import os
import codecs
import hapython


class TestParseCode(unittest.TestCase):
    pass


def test_generator(base_filename):
    def test_parse(self):
        with codecs.open("../hpyfiles/" + base_filename + ".hpy", "r", encoding="utf-8") as hpy_file:
            hpy_code = hpy_file.read()
        with codecs.open("../pyfiles/" + base_filename + ".py", "r", encoding="utf-8") as py_file:
            expected_parsed_code = py_file.read()
        actual_parsed_code = hapython.parse_code(hpy_code)
        self.assertEqual(actual_parsed_code, expected_parsed_code)
    return test_parse


if __name__ == '__main__':
    base_filenames = [x.replace(".hpy", "") for x in os.listdir("../hpyfiles")]
    for f in base_filenames:
        test_name = "test_%s" % f
        test = test_generator(f)
        setattr(TestParseCode, test_name, test)
    unittest.main()
