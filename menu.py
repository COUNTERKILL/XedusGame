import xml.etree.ElementTree as ET
import sys
import sfml as sf
from game import Game

class MenuItem:
	def __init__(self, window, infoPortion, action, text, position):
		self._window = window
		self._infoPortion = infoPortion
		self._action = action
		self._position = position
		self._text = text
		font = sf.Font.from_file("PhageRoughKG.ttf")
		self._textObj = sf.Text(self.GetText())
		self._textObj.font = font
		self._textObj.color = sf.Color.WHITE
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
	def __init__(self, window, game = None):
		if game:
			self._game = game
			game.SetMenu(self)
		self._window = window
		self._oldWindowSize = window.size
		tree = ET.parse('configs\\menu.xml')
		root = tree.getroot()
		if root.tag != "menu":
			sys.exit("Menu file is incorrect")
		backgroundImageName = root.attrib.get("background")
		self._backgroundImage = sf.Sprite(sf.Texture.from_file("images\\" + backgroundImageName))
		startPosition_x = self._window.width/2.6
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
		if self._game and self._game._simulator.IsGameOver():
			del self._game
		self.ProcessKey()
		self._window.draw(self._backgroundImage)
		for item in self._items:
			if self.CheckInfoPortion(item.GetInfoPortion()):
				text = item.GetTextObject()
				self._window.draw(text)
	def ProcessKey(self):
		for event in self._window.events:
			# close window: exit
			if type(event) is sf.CloseEvent:
				self._window.close()
			if type(event) is sf.ResizeEvent:
				#self._backgroundImage.scale((self._window.size.x/float(self._oldWindowSize.x), self._window.size.y/float(self._oldWindowSize.y)))
				self._oldWindowSize = self._window.size
				startPosition_x = self._window.width/2.6
				startPosition_y = self._window.height/3
				dY = 0
				for item in self._items:
					position = sf.Vector2(startPosition_x, startPosition_y + dY)
					dY += 50
					item._position = position
					item._width = item._textObj.local_bounds.width
					item.height = item._textObj.local_bounds.height
					#item._textObj.position = position
		if sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
			for item in self._items:
				if self.CheckInfoPortion(item.GetInfoPortion()) and item.UnderMouse():
					self.DoAction(item.GetAction())
	def Start(self):
		self._view = self._window.view
		self._window.view.reset(sf.Rectangle((0, 0), (self._window.size.x, self._window.size.y)))
		self._started = True
	def Stop(self):
		self._started = False
		self._window.view = self._view
	def Started(self):
		return self._started
	def CheckInfoPortion(self, infoPortion):
		if infoPortion==None:
			return True
		if infoPortion=="GameStarted":
			if self._game:
				return self._game._initialized
			return False
		return False
	def DoAction(self, action):
		if action=="Exit":
			exit(0)
		if action=="Return":
			self.Stop()
			self._game.Start()
		if action=="NewGame":
			self.Stop()
			self._game = Game(self._window, self)
			self._game.Start()
	def SetGame(self, game):
		self._game = game
	_items = []
	_started = None
	_window = None
	_game = None
	_view = None
	_backgroundImage = None
	_oldWindowSize = None
