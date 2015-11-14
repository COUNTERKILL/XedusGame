import sfml as sf
import Player
from Location import *
from Object import Position

# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")
view = sf.View()
view.reset(sf.Rectangle((0, 0), (640, 480)))
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

	# load music to play
	music = sf.Music.from_file("garbage_day.ogg")

except IOError:
	print("Error")
	exit(1)

# play the music
music.play()
player = Player.Player("configs\\player.ini")
loc = Location("locations\\test_loc\\location.ini")
loc.AddObject(player, 0)
player.SetPosition(Position(10, 10))
# start the game loop
while window.is_open:
	# process events
	step = Position(0, 0)
	for event in window.events:
		# close window: exit
		if type(event) is sf.CloseEvent:
			window.close()
		if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
			step.x=-1*Player.STEP_SIZE
		if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
			step.x=Player.STEP_SIZE
		if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
			step.y=-1*Player.STEP_SIZE
		if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
			step.y=Player.STEP_SIZE
	player.Move(step)
	view.center = sf.Vector2(player._position.x, player._position.y)
	window.clear() # clear screen
	window.draw(loc) # draw the sprite
	
	# set the default view back
	#window.view = window.default_view
	window.display() # update the window