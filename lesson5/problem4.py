from turtle import *

boogie = Turtle()

boogie.color("pink")
boogie.pensize(6)
boogie.speed(8)
boogie.shape("turtle")

def DrawHex(side):
	for x in range(6):
		boogie.forward(side)
		boogie.left(60)

DrawHex(50)
DrawHex(75)
DrawHex(100)
DrawHex(145)
DrawHex(150)
DrawHex(155)






mainloop()
