import sfml as sf

from game import *
from menu import *

modes = sf.VideoMode.get_fullscreen_modes()
mode = modes[9]

# create the main window
window = sf.RenderWindow(mode, "pySFML Window", sf.window.Style.TITLEBAR)# sf.window.Style.FULLSCREEN)
view = sf.View()
view.reset(sf.Rectangle((0, 0), (window.size.x, window.size.y)))
view.zoom(2)
window.view = view
window.framerate_limit = 60
#sfml.window.Style.FULLSCREEN

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