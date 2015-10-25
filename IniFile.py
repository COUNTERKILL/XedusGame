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
						return "Default"
					else:
						if paramName in line:
							index_param_start=line.find('=')+1
							value=line[index_param_start:len(line)]
							if '\n' in value:
								value = value[0:-1]
							return value
		return "Default"
	_fileName=None

	def ReadInt(self,sectionName,paramName):
		value = IniFile.ReadString(self,sectionName,paramName)
		value = float(value)
		value = int(value)
		return value
		
	def ReadBool(self,sectionName,paramName):
		value = IniFile.ReadString(self,sectionName,paramName)
		value = bool(value)
		return value
	
	def ReadFloat(self,sectionName,paramName):
		value = IniFile.ReadString(self,sectionName,paramName)
		value = float(value)
		return value
		
	def Write(self,sectionName,paramName,paramValue):
		section='['+sectionName+']'
		sectionFinded = False
		copied = False
		newFile = False
		try: 
			file=open(self._fileName,'r+')
		except (OSError, IOError) as e:
			file=open(self._fileName,'w')
			newFile=True
			file.close()
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
					if newFile == False:
						fileCopy.write('\n'+section)
					else:
						fileCopy.write(section)
					fileCopy.write('\n'+paramName+'='+paramValue+'\n')
				else:
					if copied == False:
						fileCopy.write('\n'+paramName+'='+paramValue)
		os.remove(self._fileName)
		os.rename('Copy_'+self._fileName,self._fileName)