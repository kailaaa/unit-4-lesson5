from turtle import *

boogie = Turtle()

boogie.color("pink")
boogie.pensize(6)
boogie.speed(8)
boogie.shape("turtle")

def DrawHex():
	for x in range(6):
		me.forward(100)
		me.left(40)

DrawHex()

mainloop()
