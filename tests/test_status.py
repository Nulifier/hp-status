import unittest
from unittest import mock

from tests import mocks
from hpstatus import status

class StatusTest(unittest.TestCase):
	def test_FEATURES(self):
		self.assertIsInstance(status.FEATURES, list)
		self.assertIsInstance(status.FEATURES[0], str)
	
	@mock.patch("hpstatus.status._get_system_feature", side_effect=mocks._get_system_feature)
	def test_get_fans(self, mock_get_system_feature):
		data = status.get_fans()
		self.assertIsInstance(data, list)
		self.assertNotEqual(len(data), 0)
		row = data[0]
		self.assertIsInstance(row, dict)
		self.assertIn("id", row)
		self.assertIn("location", row)
		self.assertIn("present", row)
		self.assertIn("speed", row)
		self.assertIn("percentage", row)
		self.assertIn("redundant", row)
		self.assertIn("partner", row)
		self.assertIn("hot_pluggable", row)
	
	@mock.patch("hpstatus.status._get_system_feature", side_effect=mocks._get_system_feature)
	def test_get_powermeter(self, mock_get_system_feature):
		data = status.get_powermeter()
		self.assertIsInstance(data, list)
		self.assertNotEqual(len(data), 0)
		row = data[0]
		self.assertIsInstance(row, dict)
		self.assertIn("id", row)
		self.assertIn("reading", row)
	
	@mock.patch("hpstatus.status._get_system_feature", side_effect=mocks._get_system_feature)
	def test_get_powersupply(self, mock_get_system_feature):
		data = status.get_powersupply()
		self.assertIsInstance(data, list)
		self.assertNotEqual(len(data), 0)
		row = data[0]
		self.assertIsInstance(row, dict)
		self.assertIn("id", row)
		self.assertIn("present", row)
		self.assertIn("redundant", row)
		self.assertIn("condition", row)
		self.assertIn("hotplug", row)
		self.assertIn("reading", row)
	
	@mock.patch("hpstatus.status._get_system_feature", side_effect=mocks._get_system_feature)
	def test_get_temp(self, mock_get_system_feature):
		data = status.get_temp()
		self.assertIsInstance(data, list)
		self.assertNotEqual(len(data), 0)
		row = data[0]
		self.assertIsInstance(row, dict)
		self.assertIn("id", row)
		self.assertIn("location", row)
		self.assertIn("temp", row)
		self.assertIn("threshold", row)

if __name__ == "__main__":
	unittest.main()
