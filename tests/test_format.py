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

    CSV_HEADERS = [
        "id",
        "present",
        "redundant",
        "condition",
        "hotplug",
        "reading"
    ]

    CSV_VALUES = {
        "present": "True",
        "redundant": "True",
        "condition": "Ok",
        "hotplug": "Supported",
        "reading": "60.0"
    }

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
        string = format.to_csv(self.TEST_DATA, header=True)
        self.assertIsInstance(string, str)
        lines = string.splitlines()
        # id,present,redundant,condition,hotplug,reading
        # '1,True,True,Ok,Supported,60.0',
        # '2,True,True,Ok,Supported,60.0'

        self.assertEqual(len(lines), 3)
        
        # Determine that all the headers are present and record their indices
        headers = lines[0].split(",")
        header_index = {}
        for header in self.CSV_HEADERS:
            header_index[header] = headers.index(header)

        for i in range(1, 2):
            values = lines[i].split(",")
            self.assertEqual(values[header_index["id"]], str(i))
            for header, value in self.CSV_VALUES.items():
                self.assertEqual(values[header_index[header]], value)
    
    def test_to_json(self):
        string = format.to_json(self.TEST_DATA)
        # [
        #   {"id":1,"present":true,"redundant":true,"condition":"Ok","hotplug":"Supported","reading":60.0},
        #   {"id":2,"present":true,"redundant":true,"condition":"Ok","hotplug":"Supported","reading":60.0}
        # ]
        for i in range(2):
            self.assertRegex(string, r'\[.*{.*\"id\": ?' + str(i+1) + r'.*?}.*\]')
            self.assertRegex(string, r'\[.*{.*\"present\": ?true.*?}.*\]')
            self.assertRegex(string, r'\[.*{.*\"redundant\": ?true.*?}.*\]')
            self.assertRegex(string, r'\[.*{.*\"condition\": ?\"Ok\".*?}.*\]')
            self.assertRegex(string, r'\[.*{.*\"hotplug\": ?\"Supported\".*?}.*\]')
            self.assertRegex(string, r'\[.*{.*\"reading\": ?60\.0.*?}.*\]')

if __name__ == "__main__":
    unittest.main()
