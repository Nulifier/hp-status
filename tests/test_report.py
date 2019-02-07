import unittest
from unittest import mock

from tests import mocks
from hpstatus import report

class SystemTest(unittest.TestCase):
	def test_FEATURES(self):
		self.assertIsInstance(report.FEATURES, list)
		self.assertIsInstance(report.FEATURES[0], str)

	@mock.patch("hpstatus.status._get_system_feature", side_effect=mocks._get_system_feature)
	def test_get_powermeter(self, mock_get_system_feature):
		text = report.get_report("powermeter", "line", {"prefix": "hp_"})
		self.assertIsInstance(text, str)

if __name__ == "__main__":
	unittest.main()
