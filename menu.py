import xml.etree.ElementTree as ET
import sys
import sfml as sf

class MenuItem:
	def __init__(self, window, infoPortion, action, text, position):
		self._window = window
		self._infoPortion = infoPortion
		self._action = action
		self._position = position
		self._text = text
		font = sf.Font.from_file("arial.ttf")
		self._textObj = sf.Text(self.GetText())
		self._textObj.font = font
		self._textObj.color = sf.Color.GREEN
		self._textObj.position = position
		self._textObj.character_size = 24
		self._width = self._textObj.local_bounds.width
		self.height = self._textObj.local_bounds.height
	def GetText(self):
		return self._text
	def GetTextObject(self):
		if self.UnderMouse():
			self._textObj.style = sf.Text.UNDERLINED
		else:
			self._textObj.style = sf.Text.REGULAR
		return self._textObj
	def GetAction(self):
		return self._action
	def GetInfoPortion(self):
		return self._infoPortion
	def UnderMouse(self):
		mousePos = sf.Mouse.get_position(self._window) - self._window.view.viewport.position
		#mousePos = self._window.convert_coords(mousePos)
		#print(mousePos)
		if (mousePos.x > self._position.x) and (mousePos.x < (self._position.x + self._width)) and (mousePos.y > self._position.y) and (mousePos.y < (self._position.y + self.height)):
			return True
		return False
	_infoPortion = None
	_action = None
	_text = None
	_width = None
	_height = None
	_position = None
	_textObj = None
	_window = None

class Menu:
	def __init__(self, window):
		self._window = window
		tree = ET.parse('configs\\menu.xml')
		root = tree.getroot()
		if root.tag != "menu":
			sys.exit("Menu file is incorrect")
		startPosition_x = self._window.width/2.5
		startPosition_y = self._window.height/3
		dY = 0
		for child in root:
			infoPortion = child.attrib.get("infoPortion")
			action = child.attrib["action"]
			text = child.text
			position = sf.Vector2(startPosition_x, startPosition_y + dY)
			dY = dY + 30
			item = MenuItem(self._window, infoPortion, action, text, position)
			self._items.append(item)
		self._started = False
	def DrawFrame(self):
		if not self._started:
			return
		self.ProcessKey()
		for item in self._items:
			text = item.GetTextObject()
			self._window.draw(text)
	def ProcessKey(self):
		for event in self._window.events:
			# close window: exit
			if type(event) is sf.CloseEvent:
				self._window.close()
		sf.Mouse.get_position()
	def Start(self):
		self.view = self._window.view
		self._window.view.reset(sf.Rectangle((0, 0), (640, 480)))
		self._started = True
	def Stop(self):
		self._started = False
		self._window.view = self._view
	def Started(self):
		return self._started
	_items = []
	_started = None
	_window = None
