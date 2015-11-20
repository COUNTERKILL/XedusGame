import sfml as sf

class Hud(sf.Drawable):
	def __init__(self, window, logicPlayer):
		self._player = logicPlayer
		self._window = window
		self._health = logicPlayer.GetHealth()
		self._backgroundSprite = sf.Sprite(sf.Texture.from_file("images\\hud_background.png"))
		self._width = self._backgroundSprite.texture.width
		self._height = self._backgroundSprite.texture.height
		self._healthSprite = sf.RectangleShape()
		self._healthSprite.size = (self._width - 35, 20)
		self._healthSprite.fill_color = sf.Color(255, 0, 0, 200)
	def draw(self, target, state):
		self._health = self._player.GetHealth()
		self._backgroundSprite.position = self._window.view.center + sf.Vector2(self._window.view.size.x/2, self._window.view.size.y/2) - sf.Vector2(self._width, self._height)
		self._healthSprite.position = sf.Vector2(self._backgroundSprite.position.x + 20, self._backgroundSprite.position.y + 20)
		self._healthSprite.size = ((self._width - 35) * self._health/100, 20)
		target.draw(self._backgroundSprite, state)
		target.draw(self._healthSprite, state)
		
	_window = None
	_player = None
	_backgroundSprite = None
	_healthSprite = None
	_width = None
	_height = None
	_health = None
