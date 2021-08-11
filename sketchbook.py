# COMP1021 Lab 2 Python sketchbook

import turtle       # Import the turtle module for the program

turtle.width(4)
turtle.speed(10)     #0 fastest,10 very very fast , 5 normal, 1 slow

print("Welcome to the Python sketchbook!")


##### While loop to repeat the main menu

# Initialize the option to empty in order to enter the while loop
option = ""
fill_color ="none"


while option != "q": # While the option is not "q"
    print()
    print("Please choose one of the following options:")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    print("l - Draw a line")
    print("r - Draw a rectangle")
    print("c - Draw a circle")
    print("p - Change the pen colour of the turtle")
    print("g - Draw the generated flower")
    print("f - Change the fill colour of the turtle")
    print("e - Draw the explosion")
    print("a - Draw the author's information")
    print("q - Quit the program")
    print()

    option = input("Please input your option: ")

    ##### Handle the move option
    if option == "m":
        print()

        # Ask the user for the x and y location
        x = input("Please enter the x location: ")
        x = int(x)
        y = input("Please enter the y location: ")
        y = int(y)

        # Move the turtle without drawing anything
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    ##### Handle the rotate option
    if option == "t":
        print()

        #
        # Please put your code here
        #
        rotate_angle = input("Please enter the rotate angle?")
        rotate_angle = int(rotate_angle)
        
        turtle.left(rotate_angle)
        

    ##### Handle the line option
    if option == "l":
        print()

        # Ask the user for the x and y location
        x = input("Please enter the x location: ")
        x = int(x)
        y = input("Please enter the y location: ")
        y = int(y)

        # Move the turtle and draw a line
        turtle.goto(x, y)

    ##### Handle the rectangle option
    if option == "r":
        print()

        #
        # Please put your code here
        #ask the user for the width and height
        rectangle_width = input("Please enter the width of the rectangle:")
        rectangle_height = input("Please enter the height of the rectangle:")
        rectangle_width = int(rectangle_width )
        rectangle_height = int(rectangle_height)

        if fill_color!= "none":
            turtle.begin_fill()
        turtle.forward(rectangle_width)
        turtle.left(90)
        turtle.forward(rectangle_height)
        turtle.left(90)
        turtle.forward(rectangle_width)
        turtle.left(90)
        turtle.forward(rectangle_height)
        if fill_color!="none":
            turtle.end_fill()

    ##### Handle the circle option
    if option == "c":
        print()

        #
        # Please put your code here
        #ask the user for the radius of the circle
        radius = input("Please enter the radius of the circle:")
        radius = int(radius)
        
        if fill_color!= "none":
            turtle.begin_fill()
        turtle.circle(radius)
        if fill_color!= "none":
            turtle.end_fill()

    ##### Handle the pen colour option
    if option == "p":
        print()

        #
        # Please put your code here
        #ask the user for the color
        pen_color = input("What is your pen color?")

        turtle.pencolor(pen_color)

    ##### Handle the fill colour option
    if option == "f":
        print()

        #
        # Please put your code here
        #ask the color for the fill color
        fill_color = input("What color do you want to fill(Type none to clear the color)?")
        
        if fill_color != "none":
            turtle.fillcolor(fill_color)

    ###Draw the generated flower
    if option =="g":
        print()

        #
        #Please put your code here
        #
        #Ask for the the radius
        radius = input("Please enter the radius of the flower petal:")
        radius = int(radius)
        
        if turtle!="none":
            turtle.begin_fill()
        for j in range(20):
            for i in range (0,4,1):
                turtle.circle(radius,180)
                turtle.left(90)
            turtle.left(18)
        if turtle !="none":
            turtle.end_fill()

    ###Draw the explostion
    if option =="e":
        print()

        #
        #Please put your code here
        #
        #Ask the user for the radius
        size = input("Please enter the size of the explosion (>150):")
        size = int(size)

        for thiscolor in ["MediumPurple", "OrangeRed", "GoldenRod","yellow"]:
            for i in range(1,5):
                thistimeColor = thiscolor+str(i)
                turtle.color(thistimeColor)
                turtle.dot(size)
                size = size - 10

      ###Draw the author's surname
    if option =="a":
        print()

        #Writing down the surname
  
 
        choice = input("Do you want the surname to be English or Chinese, if English type 1, if Chinese type 2:")
        choice = int(choice)
       
        
        if choice == 1:
            turtle.up()
            turtle.goto(-200,-50)
            turtle.down()               #move the turtle to the right starting position
            turtle.speed(5)
            turtle.left(180)   
            goForward=100            #for the tutle to move to another letter
            short_line = 50
            count=0
            start=1
            x_position = -50        #used in the word E          
            y_position = 50
            x__position = 50        #used in the N word
            y__position = 50
            x___position = 50
            
            if start ==1:
                for colors in ["red","orange","LightSalmon","yellow","khaki","SpringGreen","DarkOliveGreen", "slate blue"]:
                    count=count+1
                    if count==1:
                
                            for i in range(1,4):
                                thiscolor = colors + str(i)
                                turtle.color(thiscolor)
                                                                #color red
                                turtle.circle(-50,60)              #writing the word C
                                count=count+1
                                                
                    
                     
                    elif count ==5 :
                        
                             for i in range(1,3): #move to the second letter H
                                turtle.up()
                                turtle.forward(goForward)     #write the 1 1 of the the word H
                                turtle.down()
                                turtle.right(90)
                                thiscolor = colors + str(i)
                                turtle.color(thiscolor)
                                        
                                turtle.forward(100)           #color orange
                                turtle.right(90)
                                goForward = goForward - 50
                                count=count+1
                                
                    elif count == 8:
                            for i in range (2,3):
                                
                                turtle.right(90)
                                turtle.forward(short_line)      #write the - of the letter H
                                
                                turtle.left(90)                 #color lightsalmon
                                thiscolor = colors + str(i)
                                turtle.color(thiscolor)
                                        
                                turtle.forward(short_line)
                                count = count+1
                                
                    elif count == 10:                      #draw the 三 of E
                            for i in range (1,4):            #yellow
                                
                                turtle.up()
                                turtle.goto(x_position,y_position)
                                turtle.down()
                                
                                thiscolor = colors + str(i)
                                turtle.color(thiscolor)
                                turtle.forward(short_line)
                                y_position = y_position - 50
                                count=count+1
                                
                    elif count == 14:                       #draw the 1 of E
                            for i in range (1,2):                 #khaki
                                turtle.up()
                                turtle.goto(-50,50)
                                turtle.down()
                                thiscolor = colors + str(i)
                                turtle.color(thiscolor)
                                turtle.right(90)
                                turtle.forward(100)
                                count=count+1
                                

                    elif count == 16:
                            for i in range (1,3):
                                turtle.up()
                                turtle.goto(x__position,y__position)
                                turtle.down()
                                thiscolor = colors + str(i)
                                turtle.color(thiscolor)
                                
                                turtle.forward(100)
                                x__position = x__position + 50
                                count = count+1
                    elif count ==19:
                            for i in range(1,2):
                                turtle.up()
                                turtle.goto(x___position,y__position)
                                turtle.down()
                                thiscolor = colors + str(i)
                                turtle.color(thiscolor)
                                turtle.left(27)
                                turtle.forward(111.8)
                                
        elif choice == 2:        #I wanted to write my name according to the correct strokes, so I won't be using loops when writing it
            count=0
            turtle.speed(2)
            turtle.width(10)
            for colors in ["red","orange","LightSalmon","khaki","mistyrose","aquamarine","DarkOliveGreen","LightBlue","cyan","DeepSkyBlue","DodgerBlue","RoyalBlue", "slate blue","MediumOrchid","MediumPurple","NavyBlue"]:
                count=count+1
                
                if count==1:                      #making different colors in the strokes
                    turtle.up()
                    turtle.goto(-200,200)
                    turtle.down()
                    turtle.right(90)
                    for i in range(1,5):               #red
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(100)
                        
                        count=count+1
                        
                elif count == 6:
                    turtle.up()             
                    turtle.goto(-200,200)
                    turtle.down()
                    turtle.left(90)
                    
                    for i in range (1,3):                #making the small line on top orange 
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(37.5)
                        count=count+1
                        
                elif count == 10:                          #making the small half semi circle light Salmon
                    turtle.color(colors) 
                    turtle.right(90)
                    turtle.circle(-75,75)
                    turtle.left(145)
                    count= count+1

                elif count == 12:                         #making the big semi circle as well as the small line in a loop
                    turtle.color(colors)
                    turtle.circle(-120,120)             #color khaki
                    turtle.right(110)
                    thiscolor = colors + str(i)
                    turtle.color(thiscolor)
                    turtle.forward(50)
                    count=count+1

                elif count == 14:                #writing the right hand side of my surname in Chinese
                    turtle.up()
                    turtle.goto(-50,200)       #making the color aquamarine
                    turtle.down()
                    turtle.right(110)
                    for i in range (1,4):
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(50)
                        count=count+1
                        
                elif count == 18:                #start writing the box like strokes in my surname
                
                    turtle.up()                 #color Dark olive green
                    turtle.goto(-50,150)
                    turtle.right(90)
                    turtle.down()
                    for i in range(1,4):
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(50)
                        count=count+1
                         
                elif count == 22:                     #color light blue
                    turtle.up()
                    turtle.goto(-50,150)
                    turtle.left(90)
                    turtle.down()
                    for i in range(1,4):
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(50)
                        count=count+1

                elif count == 26:            #color cyan
                    turtle.right(90)
                    for i in range(1,4):
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(50)
                        count=count+1

                elif count == 30:           #color deep sky blue
                    
                    turtle.up()
                    turtle.goto(-50,75)
                    turtle.left(90)
                    turtle.down()
                    for i in range(1,4):
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(50)
                        count=count+1
                elif count == 34:               #color royal blue
                    turtle.up()
                    turtle.goto(-50,0)
                    turtle.down()
                    for i in range(1,4):
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(50)
                        count=count+1

                        
                elif count == 38:
                   
                    turtle.up()             #color state blue
                    turtle.goto(25,220)           
                    turtle.down()
                    turtle.right(90)
                    for i in range(1,4):
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(135)
                        count=count+1

                elif count == 42:
                    turtle.up()
                    turtle.goto(25,0)
                    turtle.down()
                    turtle.right(30)
                    for i in range(1,4):
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(65.6)
                        count=count+1
                        
                elif count == 46:
                    turtle.up()
                    turtle.goto(25,0)
                    turtle.down()
                    turtle.left(60)
                    for i in range(1,4):
                        thiscolor = colors + str(i)
                        turtle.color(thiscolor)
                        turtle.forward(65.6)
                        count=count+1
                    
                    
                elif count == 50:
                    turtle.left(60)
                    turtle.width(4)
                    
                    for i in range(5):
                        thiscolor = colors
                        turtle.color(thiscolor)
                        
                        turtle.forward(30)
                        turtle.right(144)
                        
                    count= count+1
                    
                elif count == 52:
                    turtle.up()
                    turtle.goto(300,-250)
                    turtle.down()
                    turtle.write("陳 = CHEN"
                                 ,font=("Arial",30,"bold"))
                        
                            
        
        
                        
        

turtle.done()
