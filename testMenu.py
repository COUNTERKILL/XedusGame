from menu import *



window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")
view = sf.View()
view.reset(sf.Rectangle((100, 100), (640, 480)))
window.view = view

menu = Menu(window)
menu.Start()
while window.is_open:
	window.clear()
	menu.DrawFrame()
	window.display()