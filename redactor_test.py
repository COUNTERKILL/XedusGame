import sfml as sf
import player
from location import *
from object import Position
import animatedObject 

def RechangeView(window):
	step = sf.Vector2(0, 0)
	mousePos = sf.Mouse.get_position(window) - window.view.viewport.position
	if mousePos.x < 100:
		step.x = -0.3
	if mousePos.y < 100:
		step.y = -0.3
	if mousePos.x > (window.size.x - 100):
		step.x = 0.3
	if mousePos.y > (window.size.y - 100):
		step.y = 0.3
	window.view.center += step

# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")
view = sf.View()
view.reset(sf.Rectangle((0, 0), (640, 480)))
view.zoom(2)
window.view = view
player = player.Player("configs\\player.ini")
loc = Location("locations\\test_loc\\redactor_loc.ini")
# start the game loop
obj=None
a=False
while window.is_open:
	# process events
	for event in window.events:
		# close window: exit
		if type(event) is sf.CloseEvent:
			window.close()
		if sf.Keyboard.is_key_pressed(sf.Keyboard.A):
			obj=AnimatedObject.AnimatedObject("locations\\test_loc\\objects\\test_obj_animated_electra.ini")
			a=True
		if sf.Keyboard.is_key_pressed(sf.Keyboard.RETURN):
			if obj:
				loc.AddObject(obj, 0)
			a=False
			context=False
			obj=None
		if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
			a=False
			obj=None
		if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
			step.x=Player.STEP_SIZE
		if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
			step.y=-1*Player.STEP_SIZE
		if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
			step.y=Player.STEP_SIZE
		if obj:
			position = Position(window.view.center.x, window.view.center.y)
			obj.SetPosition(position)
	RechangeView(window)
	window.clear() # clear screen
	window.draw(loc) # draw the sprite
	if(a): window.draw(obj)
	# set the default view back
	#window.view = window.default_view
	window.display() # update the window
