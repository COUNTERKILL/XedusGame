import IniFile
from IniFile import IniFile
import unittest


class Test(unittest.TestCase):
	def testWriteToIni(self):
		iniFile = IniFile("config.ini")
		iniFile.Write("config", "Name", "Oleg")
		self.assertEqual(iniFile.ReadString("config", "Name"), "Oleg")

if __name__ == "__main__":
   unittest.main()