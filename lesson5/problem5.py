from turtle import *

moon = Turtle()

moon.color("red")
moon.pensize(6)
moon.speed(8)
moon.shape("classic")

def Drawmoon():
	for x in range(6):
		moon.forward(60)
		moon.left(154)

Drawmoon()

mainloop()
