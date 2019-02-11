from turtle import *

boogie = Turtle()

boogie.color("pink")
boogie.pensize(6)
boogie.speed(8)
boogie.shape("turtle")

def Drawleaf():
	for x in range(4):
		me.forward(200)
		me.left(140)

def Drawcircle():
	for x in range(12):
		Drawleaf()
		me.left(30)

Drawcircle()




mainloop()
