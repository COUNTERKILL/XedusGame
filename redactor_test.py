import sfml as sf
import Player
from Location import *
from Object import Position
import AnimatedObject 
# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")
view = sf.View()
view.reset(sf.Rectangle((0, 0), (640, 480)))
view.zoom(2)
window.view = view
player = Player.Player("configs\\player.ini")
loc = Location("locations\\test_loc\\redactor_loc.ini")
# start the game loop
obj=None
a=False
context=False
while window.is_open:
    # process events
    for event in window.events:
        # close window: exit
		if type(event) is sf.CloseEvent:
			window.close()
		if sf.Keyboard.is_key_pressed(sf.Keyboard.A) or context:
			obj=AnimatedObject.AnimatedObject("locations\\test_loc\\objects\\test_obj_animated_electra.ini")
			position=sf.Mouse.get_position()
			obj.SetPosition(Position(position.x,position.y))
			a=True
			context=True
		if sf.Keyboard.is_key_pressed(sf.Keyboard.RETURN):
			if obj:
				loc.AddObject(obj, 0)
			a=False
			context=False
			obj=None
		if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
			a=False
			context=False
			obj=None
		if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
			step.x=Player.STEP_SIZE
		if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
			step.y=-1*Player.STEP_SIZE
		if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
			step.y=Player.STEP_SIZE
    view.center = sf.Mouse.get_position()
    window.clear() # clear screen
    window.draw(loc) # draw the sprite
    if(a): window.draw(obj)
    # set the default view back
    #window.view = window.default_view
    window.display() # update the window
