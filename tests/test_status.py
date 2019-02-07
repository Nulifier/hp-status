import unittest
from unittest import mock

from tests import mocks
from hpstatus import status

class SystemTest(unittest.TestCase):
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

class StorageTest(unittest.TestCase):
	@mock.patch("hpstatus.status._get_storage_controllers", side_effect=mocks._get_storage_controllers)
	def test_get_storage_controllers(self, mock_get_storage_controllers):
		data = status.get_storage_controllers()
		self.assertIsInstance(data, list)
		self.assertNotEqual(len(data), 0)
		row = data[0]
		self.assertIsInstance(row, dict)
		self.assertIn("id", row)
		self.assertIn("model", row)
		self.assertIn("status", row)
		self.assertIn("cache", row)
		self.assertIn("battery", row)

	@mock.patch("hpstatus.status._get_storage_drives", side_effect=mocks._get_storage_drives)
	def test_get_storage_drives(self, mock_get_storage_drives):
		data = status.get_storage_drives(1)
		self.assertIsInstance(data, list)
		self.assertNotEqual(len(data), 0)
		row = data[0]
		self.assertIsInstance(row, dict)
		self.assertIn("location", row)
		self.assertIn("port", row)
		self.assertIn("box", row)
		self.assertIn("bay", row)
		self.assertIn("size", row)
		self.assertIn("status", row)
	
	@mock.patch("hpstatus.status._get_storage_drives_detail", side_effect=mocks._get_storage_drives_detail)
	def test_get_storage_drives_detail(self, mock_get_storage_drives_detail):
		data = status.get_storage_drives_detail(1)
		self.assertIsInstance(data, list)
		self.assertNotEqual(len(data), 0)
		row = data[0]
		self.assertIsInstance(row, dict)
		self.assertIn("location", row)
		self.assertIn("port", row)
		self.assertIn("box", row)
		self.assertIn("bay", row)
		self.assertIn("size", row)
		self.assertIn("status", row)
		self.assertIn("serial", row)
		self.assertIn("temp", row)
		self.assertIn("max_temp", row)

if __name__ == "__main__":
	unittest.main()
