import xml.etree.ElementTree as ET
import sys

class Menu:
	def __init__(self):
		root = tree.getroot()
		if root.tag != "menu":
			sys.exit("Τΰιλ μενώ νεβεπεν")
	def DrawFrame(self):
		
	def Started(self):
		return self._started
	_items = None
	_started = None