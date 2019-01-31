import unittest
from hpstatus import util

class FromNiceSizeTest(unittest.TestCase):
	def test_kb(self):
		self.assertEqual(util.from_nice_size("3 kB"), 3 * 1000)
	
	def test_mb(self):
		self.assertEqual(util.from_nice_size("7 MB"), 7 * 1000 * 1000)
	
	def test_gb(self):
		self.assertEqual(util.from_nice_size("5 GB"), 5 * 1000 * 1000 * 1000)

	def test_tb(self):
		self.assertEqual(util.from_nice_size("13 TB"), 13 * 1000 * 1000 * 1000 * 1000)

	def test_pb(self):
		self.assertEqual(util.from_nice_size("9 PB"), 9 * 1000 * 1000 * 1000 * 1000 * 1000)
	
	def test_eb(self):
		self.assertEqual(util.from_nice_size("72 EB"), 72 * 1000 * 1000 * 1000 * 1000 *1000 * 1000)

	def test_kib(self):
		self.assertEqual(util.from_nice_size("3 kiB"), 3 * 1024)
	
	def test_mib(self):
		self.assertEqual(util.from_nice_size("7 MiB"), 7 * 1024 * 1024)
	
	def test_gib(self):
		self.assertEqual(util.from_nice_size("5 GiB"), 5 * 1024 * 1024 * 1024)

	def test_tib(self):
		self.assertEqual(util.from_nice_size("13 TiB"), 13 * 1024 * 1024 * 1024 * 1024)

	def test_pib(self):
		self.assertEqual(util.from_nice_size("9 PiB"), 9 * 1024 * 1024 * 1024 * 1024 * 1024)
	
	def test_eib(self):
		self.assertEqual(util.from_nice_size("72 EiB"), 72 * 1024 * 1024 * 1024 * 1024 *1024 * 1024)
	
	def test_kb_iec(self):
		self.assertEqual(util.from_nice_size("3 kB", iec=True), 3 * 1024)
	
	def test_mb_iec(self):
		self.assertEqual(util.from_nice_size("7 MB", iec=True), 7 * 1024 * 1024)
	
	def test_gb_iec(self):
		self.assertEqual(util.from_nice_size("5 GB", iec=True), 5 * 1024 * 1024 * 1024)

	def test_tb_iec(self):
		self.assertEqual(util.from_nice_size("13 TB", iec=True), 13 * 1024 * 1024 * 1024 * 1024)

	def test_pb_iec(self):
		self.assertEqual(util.from_nice_size("9 PB", iec=True), 9 * 1024 * 1024 * 1024 * 1024 * 1024)
	
	def test_eb_iec(self):
		self.assertEqual(util.from_nice_size("72 EB", iec=True), 72 * 1024 * 1024 * 1024 * 1024 *1024 * 1024)
