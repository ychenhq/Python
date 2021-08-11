def savePositions():
    filename = turtle.textinput("Save turtle positions",
                                "What is the filname you want to create?")
    newfile = open(filename, "wt")

    for thisTurtle in allTurtles:
        #Make a string for one turtle, in the right 
        one_line = str(thisTurtle.xcor()) + "\t" +str(thisTurtle.ycor())+ "\n"


        turtle.listen()


def loadPositions():
    global allTurtles
    filename = turtle.textinput("Load turtle positions",
                                "What is the filename you want to load?")
    myfile = open (filename, "r")
    turtleIndex = 0
    for line in myfile:
        #Read each line as a single rule
        line = line.rstrip() #strip means remove things
        print("line is", line)

        items = line.split("\t")
        print("line is", line)

        x = float(
