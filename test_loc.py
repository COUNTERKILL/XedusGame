import sfml as sf
from location import * 

# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")
view = sf.View()
view.reset(sf.Rectangle((100, 100), (640, 480)))
window.view = view
try:
	# create some graphical text to display
	font = sf.Font.from_file("airborne.ttf")
	text = sf.Text("Hello SFML", font, 50)

except IOError:
	print("Error")
	exit(1)
loc = Location("locations\\test_loc\\location.ini")


# start the game loop
while window.is_open:
	# process events
	for event in window.events:
		# close window: exit
		if type(event) is sf.CloseEvent:
			window.close()
		if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
			view.move(-1, 0)
		if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
			view.move(1, 0)
		if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
			view.move(0, -1)
		if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
			view.move(0, 1)
	window.clear() # clear screen
	window.draw(loc)
	window.draw(text) # draw the string
	# set the default view back
	#window.view = window.default_view
	window.display() # update the window