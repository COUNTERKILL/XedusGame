import sfml as sf

from game import *
from menu import *

# create the main window
window = sf.RenderWindow(sf.VideoMode(1024, 768), "pySFML Window")
view = sf.View()
view.reset(sf.Rectangle((0, 0), (1024, 768)))
view.zoom(2)
window.view = view
try:
	# load a sprite to display
	texture = sf.Texture.from_file("tex.jpg", sf.Rectangle((0, 0), (200, 120)))
	sprite = sf.Sprite(texture)
	sprite.texture_rectangle = sf.Rectangle((0, 0), (100, 80))
	sprite.color = sf.Color(255, 255, 255, 200)
	sprite.position = sf.Vector2(400, 400)

	# create some graphical text to display
	font = sf.Font.from_file("airborne.ttf")
	text = sf.Text("Hello SFML", font, 50)

except IOError:
	print("Error")
	exit(1)
menu = Menu(window)
menu.Start()
# start the game loop
game = None
while window.is_open:
	window.clear() # clear screen
	game = menu._game
	menu.DrawFrame()
	if game!=None:
		game.DrawFrame()
	
	# set the default view back
	#window.view = window.default_view
	window.display() # update the window