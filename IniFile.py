class IniFile:
	def __init__(self, fileName):
		self._fileName = fileName
	def ReadString(self, sectionName, paramName):
		X=sectionName
		Y=paramName
		stroka='['+X+']'
		file=open(self._fileName,'r')
		sectionFinded = False
		for line in file:
			if stroka in line:
				sectionFinded = True
				continue
			if sectionFinded == True:			
				if line[0]=='[':
					return
				else:
					if Y in line:
						index_res_start=line.find('=')+1
						result=line[index_res_start:len(line)]
						return result					
	_fileName=None