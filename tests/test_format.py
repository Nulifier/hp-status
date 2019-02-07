import unittest
from unittest import mock

from tests import mocks
from hpstatus import format

class FormatTest(unittest.TestCase):
    TEST_DATA = [
        {'id': 1, 'present': True, 'redundant': True, 'condition': 'Ok', 'hotplug': 'Supported', 'reading': 60.0},
        {'id': 2, 'present': True, 'redundant': True, 'condition': 'Ok', 'hotplug': 'Supported', 'reading': 60.0}
    ]

    TAGS = [
        "id"
    ]

    CSV_OUTPUT = [
        '1,True,True,Ok,Supported,60.0',
        '2,True,True,Ok,Supported,60.0'
    ]
    JSON_OUTPUT = '[{"id":1,"present":true,"redundant":true,"condition":"Ok","hotplug":"Supported","reading":60.0},{"id":2,"present":true,"redundant":true,"condition":"Ok","hotplug":"Supported","reading":60.0}]'

    def test_FORMATS(self):
        self.assertIsInstance(format.FORMATS, list)
        self.assertIsInstance(format.FORMATS[0], str)
    
    def test_to_line(self):
        string = format.to_line(self.TEST_DATA, "powersupply", self.TAGS, "hp_")
        self.assertIsInstance(string, str)
        lines = string.splitlines()
        self.assertEqual(len(lines), 2)
        # hp_powersupply,id=1i present=True,redundant=True,condition="Ok",hotplug="Supported",reading=60.0
        # hp_powersupply,id=2i present=True,redundant=True,condition="Ok",hotplug="Supported",reading=60.0
        for i in range(2):
            self.assertRegex(lines[i], r"^hp_powersupply")
            self.assertRegex(lines[i], r"^\S+id={}i".format(i+1))
            self.assertRegex(lines[i], r"^\S+ \S*present=True")
            self.assertRegex(lines[i], r"^\S+ \S*redundant=True")
            self.assertRegex(lines[i], r'^\S+ \S*condition="Ok"')
            self.assertRegex(lines[i], r'^\S+ \S*hotplug="Supported"')
            self.assertRegex(lines[i], r"^\S+ \S*reading=60.0")
    
    def test_to_csv(self):
        string = format.to_csv(self.TEST_DATA, header=False)
        self.assertIsInstance(string, str)
        lines = string.splitlines()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], self.CSV_OUTPUT[0])
        self.assertEqual(lines[1], self.CSV_OUTPUT[1])
    
    def test_to_json(self):
        string = format.to_json(self.TEST_DATA)
        self.assertEqual(string, self.JSON_OUTPUT)

if __name__ == "__main__":
    unittest.main()
