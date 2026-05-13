
import turtle
p=turtle.Turtle()
s=turtle.Screen()
p.speed(99999999999999999999999999999999999999999999999999)
p.width(10)
p.penup()
p.goto(125,45)
p.left(90)
p.pendown()
p.fillcolor("yellow")
p.begin_fill()
p.forward(65)
for i in range(180):
    p.forward(2.1)
    p.left(1)
p.forward(190)
for i in range(180):
    p.forward(2.1)
    p.left(1)
p.forward(125)
p.end_fill()


#goggle
p.penup()
p.width(15)
p.color("grey")
p.goto(60,90)
p.pendown()
p.fillcolor("white")
p.begin_fill()
for i in range(740):
    p.forward(0.5)
    p.left(0.5)
p.end_fill()
p.penup()
p.goto(70,90)
p.pendown()
p.width(20)
p.color("black")
p.right(100)
p.forward(50)
p.penup()
p.goto(-65,90)
p.pendown()
p.width(20)
p.color("black")
p.left(180)
p.forward(45)


#pupil
p.penup()
p.goto(5,90)
p.pendown()
p.width(50)
p.color("brown")
p.forward(0.2)
p.width(30)
p.color("black")
p.forward(0.02)
p.penup()
p.goto(15,100)
p.pendown()
p.width(10)
p.color("white")
p.forward(0.02)


#laugh
p.penup()
p.goto(-50,5)
p.width(5)
p.color("black")
p.left(90)
p.pendown()
p.fillcolor("red")
p.begin_fill()
for i in range(180):
    p.forward(1)
    p.left(1)
p.left(90)
p.goto(-50,5)
p.end_fill()
p.penup()
p.goto(-40,5)
p.width(3)
p.color("black")
p.pendown()
p.right(90)
p.fillcolor("white")
p.begin_fill()
for i in range(2):
    p.left(180)
    p.forward(20)
    p.left(90)
    p.forward(50)
    p.left(90)
    p.forward(20)
p.left(90)
p.goto(-45,5)
p.end_fill()


#jeans
p.penup()
p.goto(120,40)
p.width(5)
p.pendown()
p.left(90)
p.fillcolor("blue")
p.begin_fill()
for i in range(180):
    p.forward(2.05)
    p.right(1)
p.left(180)
p.forward(100)
p.left(90)
for i in range(310):
    p.forward(0.3)
    p.right(0.5)
p.left(90)
for i in range(130):
    p.forward(2)
    p.left(1)
p.left(90)
for i in range(310):
    p.forward(0.3)
    p.right(0.5)
p.left(90)
p.forward(100)
p.end_fill()
p.penup()
p.goto(-50,-100)
p.width(2)
p.color("white")
for i in range(4):
    p.pendown()
    p.forward(-10)
    p.penup()
    p.forward(-5)
p.left(90)
for i in range(7):
    p.pendown()
    p.forward(-10)
    p.penup()
    p.forward(-5)
p.left(90)
for i in range(4):
    p.pendown()
    p.forward(-10)
    p.penup()
    p.forward(-5)
p.left(90)
p.width(4)
p.pendown()
p.goto(-50,-100)


#wings
p.penup()
p.goto(125,-62)
p.color("black")
p.width(10)
p.pendown()
p.fillcolor('white')
p.begin_fill()
for i in range(100):
    p.forward(3)
    p.left(1)
p.right(90)
a=1
b=1
for i in range(8):
    p.forward(150-a)
    for i in range(370):
        p.forward(0.2)
        p.right(0.5)
    p.forward(100-b)
    a+=20
    b+=10
    p.left(180)
p.right(140)
for i in range(31):
    p.forward(8)
    p.right(1)
for i in range(310):
    p.forward(0.3)
    p.right(0.5)
p.end_fill()
p.penup()
p.goto(-124,-62)
p.left(180)
p.pendown()
p.fillcolor("white")
p.begin_fill()
for i in range(100):
    p.forward(3)
    p.right(1)
p.left(90)
a=1
b=1
for i in range(8):
    p.forward(150-a)
    for i in range(370):
        p.forward(0.2)
        p.left(0.5)
    p.forward(100-b)
    a+=20
    b+=10
    p.left(180)
p.left(140)
for i in range(32):
    p.forward(8)
    p.left(1)
for i in range(310):
    p.forward(0.3)
    p.left(0.5)
p.end_fill()

turtle.done()
