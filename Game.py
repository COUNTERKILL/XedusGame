import sfml as sf
from Player import *
from Location import *
from Object import Position
from simulator import Simulator

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
		self._simulator = Simulator(self._location)
		font = sf.Font.from_file("arial.ttf")
		self._gameOverText = sf.Text("Game over!")
		self._gameOverText.font = font
		self._gameOverText.color = sf.Color.WHITE
		self._gameOverText.position = sf.Vector2(self._window.view.center.x - self._window.width*0.7, self._window.view.center.y - self._window.width*0.5)
		self._gameOverText.character_size = 100
		self._music = sf.Music.from_file("garbage_day.ogg")
	def DrawFrame(self):
		if not self._started:
			return
		self.ProcessKey()
		if not self._simulator.IsGameOver():
			self._simulator.ProcessFrame()
		self._window.draw(self._location)
		if self._simulator.IsGameOver():
			self._window.draw(self._gameOverText)
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
		if self._simulator.IsGameOver():
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
		self._music.play()
		self._started = True
	def Stop(self):
		self._music.pause()
		self._started = False
	def SetMenu(self, menu):
		self._menu = menu
	_window = None
	_player = None
	_started = False
	_menu = None
	_initialized = False
	_gameOverText = None
	_music = None
