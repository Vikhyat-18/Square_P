import turtle
import random
screen = turtle.Screen()

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

for t in [t1, t2, t3]:
    t.shape("turtle")
    t.speed(0)
    t.pensize(2)

# Set different start positions
t1.penup(); t1.goto(-200, 0); t1.pendown()
t2.penup(); t2.goto(0, 0); t2.pendown()
t3.penup(); t3.goto(200, 0); t3.pendown()

# Simulate drawing at the same time
a=random.randint(100,234)
t1.right(90)
t1.forward(a)
t2.right(90)
t2.forward(a)
t3.right(90)
t3,forward(a)
turtle.done()
