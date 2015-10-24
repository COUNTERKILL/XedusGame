import os

class IniFile:
	def __init__(self, fileName):
		self._fileName = fileName

	def ReadString(self, sectionName, paramName):
		section='['+sectionName+']'
		sectionFinded = False
		with open(self._fileName,'r') as file:
			for line in file:
				if section in line:
					sectionFinded = True
					continue
				if sectionFinded == True:			
					if line[0]=='[':
						return
					else:
						if paramName in line:
							index_param_start=line.find('=')+1
							value=line[index_param_start:len(line)]
							return value
		
	_fileName=None

	def ReadInt(self,sectionName,paramName):
		value = IniFile.ReadString(self,sectionName,paramName)
		value = int(value)
		return value
		
	def ReadBool(self,sectionName,paramName):
		value = IniFile.ReadString(self,sectionName,paramName)
		value = bool(value)
		return value
		
	def Write(self,sectionName,paramName,paramValue):
		section='['+sectionName+']'
		sectionFinded = False
		copied = False
		with open(self._fileName,'r+') as file:
			with open('Copy_'+self._fileName,'w') as fileCopy:
				for line in file:
					if copied == False:
						if section in line:
							sectionFinded = True
							fileCopy.write(line)
							continue
						if sectionFinded == True:			
							if line[0]=='[':
								fileCopy.write(paramName+'='+paramValue+'\n')
								fileCopy.write(line)
								copied = True
							elif ((paramName+'=') in line) & (paramName[0]==line[0]):
								fileCopy.write(paramName+'='+paramValue+'\n')
								copied = True
								continue
							else:
								fileCopy.write(line)
						else:
							fileCopy.write(line)
							continue		
					else:
						fileCopy.write(line)
				if sectionFinded == False:
					fileCopy.write('\n'+section)
					fileCopy.write('\n'+paramName+'='+paramValue+'\n')
				else:
					if copied == False:
						fileCopy.write('\n'+paramName+'='+paramValue)
		os.remove(fileName)
		os.rename('Copy_'+fileName,fileName)