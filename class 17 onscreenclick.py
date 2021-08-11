import turtle


turtle.color("blue")
turtle.shape("circle")
turtle.fillcolor("")  #make the circle hollow
turtle.shapesize(1,1,3)  #make the outline thicker
turtle.pensize(3)
turtle.width(5)
turtle.speed(0)
def jump(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

turtle.ondrag(turtle.goto)
turtle.onscreenclick(jump)

turtle.done()
