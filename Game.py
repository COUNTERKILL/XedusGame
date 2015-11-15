import sfml as sf
from Player import *
from Location import *
from Object import Position

class Game:
	def __init__(self, window, menu = None):
		if menu:
			self._menu = menu
			menu.SetGame(self)
		self._window = window
		self._initialized = True
		self._player = Player.Player("configs\\player.ini")
		self._location = Location("locations\\test_loc\\location.ini")
		self._location.AddObject(self._player, 0)
		self._player.SetPosition(self._location.GetPlayerStartPosition())
	def DrawFrame(self):
		if not self._started:
			return
		self.ProcessKey()
		self._window.draw(self._location)
	def ProcessKey(self):
		step = Position(0, 0)
		for event in self._window.events:
			# close window: exit
			if type(event) is sf.CloseEvent:
				self._window.close()
		if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
			self.Stop()
			self._menu.Start()
			return
		if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
			step.x=-1*STEP_SIZE
		if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
			step.x=STEP_SIZE
		if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
			step.y=-1*STEP_SIZE
		if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
			step.y=STEP_SIZE
		self._player.Move(step)
		self._window.view.center = sf.Vector2(self._player._position.x, self._player._position.y)
	def Start(self):
		self._window.view.center = sf.Vector2(self._player._position.x, self._player._position.y)
		self._started = True
	def Stop(self):
		self._started = False
	def SetMenu(self, menu):
		self._menu = menu
	_window = None
	_player = None
	_started = False
	_menu = None
	_initialized = False