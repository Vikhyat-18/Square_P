import turtle
n=int(input("ent no :-__-:"))
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
pen = turtle.Turtle()
pen.color("white")
pen.pensize(1)
pen.speed(6)
for i in range(1,n+1):
    pen.forward(i)
    pen.right(90)
    pen.forward(i+1)
    pen.right(90)
    pen.forward(i+4)
    pen.right(90)

