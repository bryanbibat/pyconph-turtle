import turtle

def draw_f():
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(200)
    turtle.left(90)

def draw_e():
    draw_f()
    turtle.forward(50)

turtle.penup()
turtle.right(180)
turtle.forward(125)
turtle.pendown()
turtle.right(225)
draw_e()
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.exitonclick()
