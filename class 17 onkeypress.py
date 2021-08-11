import turtle

turtle.shape("turtle")
turtle.speed(0)
turtle.color("purple")
turtle.width(3)

def orange():
    turtle.color("orange")

def purple():
    turtle.color("purple")

def green():
    turtle.color("green")

go_forward_thismuch = 4
rotate_thisangle = 5

def moveFoward():
    turtle.forward(go_forward_thismuch)
def moveBackward():
    turtle.backward(go_forward_thismuch)
def turnleft():
    turtle.left(rotate_thisangle)
def turnright():
    turtle.right(rotate_thisangle)


turtle.onkeypress(orange, "o")
turtle.onkeypress(purple, "p")
turtle.onkeypress(green, "g")
turtle.onkeypress(moveFoward, "Right")
turtle.onkeypress(moveBackward, "Left")
turtle.onkeypress(turnleft, "Up")
turtle.onkeypress(turnright, "Down")

turtle.listen() #ask python to listen for keyboard events
turtle.done()

                  
