#Done by CHEN, Yu Zhen STD:20734188
import turtle

turtle.setup(800,600)    # Set the width and height be 800 x 600

number_of_divisions = 8  # The number of subdivisions around the centre
turtle_width = 3         # The width of the turtles

# Don't show the animation
turtle.tracer(False)

# Draw the background lines

backgroundTurtle = turtle.Turtle()

backgroundTurtle.width(1)

backgroundTurtle.down()
backgroundTurtle.color("gray88") # Draw the centered line
for i in range(number_of_divisions):
    backgroundTurtle.forward(500)
    backgroundTurtle.backward(500)
    backgroundTurtle.left(360 / number_of_divisions)

backgroundTurtle.up()

# Show the instructions
backgroundTurtle.color("purple")
backgroundTurtle.goto(-turtle.window_width()/2+50, 100)
backgroundTurtle.write("""s - change a colour for one of the colour buttons
m - all 8 drawing turtles go to middle
c - clear all drawings made by the 8 drawing turtles
""", font=("Arial", 14, "normal"))

backgroundTurtle.hideturtle()

# Set up a turtle for handling message on the turtle screen
messageTurtle = turtle.Turtle()
# This sets the colour of the text to red
messageTurtle.color("red")
# We do not want it to show/draw anything, except the message text
messageTurtle.up() 
# Set it the be at center, near the colour selections
messageTurtle.goto(0, -200)
# We do not want to show it on the screen
messageTurtle.hideturtle()


# Part 2 Preparing the drawing turtles

# The drawing turtles are put in a list
allDrawingTurtles = [] 

# Part 2.1 Add the 8 turtles in the list
for i in range(number_of_divisions):
    newTurtle=turtle.Turtle()

    #setups
    newTurtle.speed(0)
    newTurtle.width(turtle_width)
    newTurtle.hideturtle()


    allDrawingTurtles.append(newTurtle)
    
# Part 2.2 Set up the first turtle for drawing
dragTurtle = allDrawingTurtles[0]
dragTurtle.showturtle()
dragTurtle.shape("circle")
dragTurtle.shapesize(2,2)

# Part 3 Preparing the basic drawing system
# Set up the ondrag event
def draw(x,y):
    dragTurtle.ondrag(None)
    turtle.tracer(False) #To pause the update of screen
    messageTurtle.clear() # Added in Part 5.1 for clearing the message from messageTurtle
    dragTurtle.goto(x,y)
    dragTurtle.ondrag(draw)
    x_transform = [1, 1, -1, -1, 1, 1, -1, -1] # This represents + + - - + + - -
    y_transform = [1, -1, 1, -1, 1, -1, 1, -1] # This represents + - + - + - + -

    for i in range(1, number_of_divisions):
        if i<4:
            new_x = x * x_transform[i] # x with sign change
            new_y = y * y_transform[i] # y with sign change

        else:
            new_x = y * y_transform[i]
            new_y = x * x_transform[i]

        allDrawingTurtles[i].goto(new_x,new_y)
        
    turtle.tracer(True) #To resume the update of the screen
    dragTurtle.ondrag(draw)
    
dragTurtle.ondrag(draw)

# Part 5.2 clear all drawings made by the 8 drawing turtles
def clearDrawing():
    # Please finish this part
    for drawingTurtle in allDrawingTurtles:
        drawingTurtle.clear()
    messageTurtle.clear()
    messageTurtle.write("The screen is cleared",
                    align="center", font=("Arial",15,"bold"))

turtle.onkeypress(clearDrawing, 'c')

# Part 5.3 all 8 drawing turtles go to middle
def goToMiddle():
    # Please finish this part
    for allTurtles in allDrawingTurtles:
        allTurtles.up()
        allTurtles.goto(0,0)
        allTurtles.down()
    messageTurtle.clear()
    messageTurtle.write("All 8 turtles returned to middle",
                    align="center", font=("Arial",15,"bold"))
    
turtle.onkeypress(goToMiddle, 'm')

# Part 4 handling the colour selection
# Make the colour selection turtles
# Here is the list of colours
colours = ["black", "orange red", "lawn green", "medium purple", "light sky blue", "orchid", "gold"]

# Part 4.2 Set up the onclick event
def handleColourChange(x,y):
    for thisTurtle in allDrawingTurtles:
        if x <= -130:
            thisTurtle.color(colours[0])
        elif x <= -80:
            thisTurtle.color(colours[1])
        elif x <= -30:
            thisTurtle.color(colours[2])
        elif x <= 20:
            thisTurtle.color(colours[3])
        elif x <= 70:
            thisTurtle.color(colours[4])
        elif x <= 120:
            thisTurtle.color(colours[5])
        elif x <= 170:
            thisTurtle.color(colours[6])
        
        

# Part 5.4 change a colour in the colour selection
def changeColour():
    # Please finish this part
    index_of_the_colour_selection=turtle.textinput("Change color",
                     prompt=("Please type the index for the turtle:(0-6)"))
    
    integer=1
    if index_of_the_colour_selection!= None:
        index_of_the_colour_selection=int(index_of_the_colour_selection)
        while index_of_the_colour_selection <=6 and integer==1:
            color_choice = turtle.textinput("Change color",
                                prompt=("Please type the color you want to use e.g.LightBlue2:"))
            if color_choice !=None:
                
                colours[index_of_the_colour_selection]=color_choice
                count=0
                for newTurtleColor in colourSelectionTurtles:
                    for newTurtle in range(len(colourSelectionTurtles)):
                        if count==index_of_the_colour_selection & newTurtle==index_of_the_colour_selection:
                            newTurtleColor.color(color_choice)
                    count=count+1
                       
                        
                messageTurtle.clear()
                messageTurtle.write("The colour for that button has been changed, click on that button to use it",
                                align="center", font=("Arial",15,"bold"))
            integer=integer+1
    
        while (index_of_the_colour_selection>6 or index_of_the_colour_selection<0) and integer==1:
            correction_message = turtle.textinput("Change color",
                         prompt=("Please enter a correct index number:(0-6)"))
            correction_message = int(correction_message)
            if correction_message!= None:
                color_choice = turtle.textinput("Change color",
                                    prompt=("Please type the color you want to use e.g.LightBlue2:"))
                if color_choice !=None:
                    correction_message=int(correction_message)
                    colours[correction_message]=color_choice
                    count=0
                    for newTurtleColor in colourSelectionTurtles:
                        for newTurtle in range(len(colourSelectionTurtles)):
                            if count==correction_message & newTurtle==correction_message:
                                newTurtleColor.color(color_choice)
                        count=count+1
                       
                        
                    messageTurtle.clear()
                    messageTurtle.write("The colour for that button has been changed, click on that button to use it",
                                    align="center", font=("Arial",15,"bold"))
            integer=integer+1

    
    turtle.listen()   

turtle.onkeypress(changeColour, 's')

# Part 4.1 Make the colour selection turtles
colourSelectionTurtles = []
# Please finish this part

for i in range(len(colours)):
    t=turtle.Turtle()
    t.shape("square")
    t.shapesize(2,2)
    t.up()
    t.color(colours[i])
    t.goto(-150 + 50*i, -250)
    t.onclick(handleColourChange)

    colourSelectionTurtles.append(t)

turtle.tracer(True)
turtle.listen()

turtle.done()

