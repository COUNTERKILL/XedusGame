import IniFile
from IniFile import IniFile
import unittest

class Test(unittest.TestCase):
	def testWriteToIni(self):
		iniFile = IniFile('test_config.ini')
		#создание нового параметра в конце файла
		iniFile.Write('config', 'Name', 'Oleg')
		self.assertEqual(iniFile.ReadString('config', 'Name'), 'Oleg')
		#изменение существующего параметра в конце файла
		iniFile.Write('config','Name','Stepan')
		self.assertEqual(iniFile.ReadString('config', 'Name'), 'Stepan')
		#добавление нового параметра в существующую секцию в конце файла
		iniFile.Write('config','SecondName','Prikazchikov')
		self.assertEqual(iniFile.ReadString('config', 'SecondName'), 'Prikazchikov')
		#создание новой секции и добавление нового параметра
		iniFile.Write('stats','Age','21')
		self.assertEqual(iniFile.ReadString('stats', 'Age'), '21')
		self.assertEqual(iniFile.ReadInt('stats', 'Age'), 21)
		#добавление нового параметра в существующую секцию в конце файла
		iniFile.Write('stats','Level','80')
		self.assertEqual(iniFile.ReadInt('stats', 'Level'), 80)
		#добавление нового параметра в существующую секцию в конце файла
		iniFile.Write('stats','Expierence','123456789')
		self.assertEqual(iniFile.ReadInt('stats', 'Expierence'), 123456789)
		#изменение существующего параметра в конце файла
		iniFile.Write('stats','Expierence','987654321')
		self.assertEqual(iniFile.ReadInt('stats', 'Expierence'), 987654321)
		#изменение существующего параметра в середине файла в начале секции
		iniFile.Write('config','Name','Oleg')
		self.assertEqual(iniFile.ReadString('config', 'Name'), 'Oleg')
		#добавление нового параметра в существующую секцию в середине файла
		iniFile.Write('config','LastName','Unknown')
		self.assertEqual(iniFile.ReadString('config', 'LastName'), 'Unknown')	
		#изменение существующего параметра в середине файла в середине секции
		iniFile.Write('config','SecondName','Kobyak')
		self.assertEqual(iniFile.ReadString('config', 'SecondName'), 'Kobyak')
		#изменение существующего параметра в середине файла в конце секции
		iniFile.Write('config','LastName','Yurevich')
		self.assertEqual(iniFile.ReadString('config', 'LastName'), 'Yurevich')
		#добавление параметра float
		iniFile.Write('test','Float','123.456')
		self.assertEqual(iniFile.ReadFloat('test', 'Float'), 123.456)
		#преобразование float в int
		iniFile.Write('test','IntFloat','123.456')
		self.assertEqual(iniFile.ReadInt('test', 'IntFloat'), 123)
		#добавление параметра bool
		iniFile.Write('test','Cheater','True')
		self.assertEqual(iniFile.ReadBool('test', 'Cheater'), True)
		#проверка всего файла
		self.assertEqual(iniFile.ReadString('config', 'Name'), 'Oleg')
		self.assertEqual(iniFile.ReadString('config', 'SecondName'), 'Kobyak')
		self.assertEqual(iniFile.ReadString('config', 'LastName'), 'Yurevich')
		self.assertEqual(iniFile.ReadInt('stats', 'Age'), 21)
		self.assertEqual(iniFile.ReadInt('stats', 'Level'), 80)
		self.assertEqual(iniFile.ReadInt('stats', 'Expierence'), 987654321)
		self.assertEqual(iniFile.ReadFloat('test', 'Float'), 123.456)
		self.assertEqual(iniFile.ReadInt('test', 'IntFloat'), 123)
		self.assertEqual(iniFile.ReadBool('test', 'Cheater'), True)
		
if __name__ == "__main__":
   unittest.main()  