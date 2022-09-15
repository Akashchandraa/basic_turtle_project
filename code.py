import turtle

akash = turtle.Turtle()
akash.speed(20)
akash.color("orange")

for i in range(100):
	akash.forward(150)
	akash.right(135)
	akash.position()
akash.penup()
akash.forward(300)
akash.pendown()

akash.color("red")

for i in range(100):
	akash.forward(250)
	akash.left(190)
	akash.position()

akash.penup()
akash.forward(300)
akash.pendown()

akash.color("blue")

for i in range(100):

	akash.forward(200)
	akash.left(215)
	akash.position()
akash.penup()
akash.forward(300)
akash.pendown()

akash.color("black")
for i in range(50):
	akash.forward(120)
	akash.left(148)
	akash.position()
turtle.done()