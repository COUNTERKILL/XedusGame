import sfml as sf


# create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")
view = sf.View()
view.reset(sf.Rectangle((100, 100), (640, 480)))
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
	window.draw(sprite) # draw the sprite
	window.draw(text) # draw the string
	# set the default view back
	#window.view = window.default_view
	window.display() # update the window