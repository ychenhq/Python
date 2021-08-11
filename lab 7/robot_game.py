#Done by CHEN, Yu-zhen STD 20734188

# The following line imports the game function library and map into
# this main program
from game_lib import *

# This is the only 'memory' of the robot that you can use to store things
#
# You are expected to use it to store only a string, which indicates the
# current 'state' of the robot
stateForTask1 = "Go up"
stateForTask2 = "Go up"
stateForTask3 = "Go up"
stateForTask4 = "Find wall"
stateForTask5 = "Find wall"

# These functions helps the robot to make the decision about what it needs
# to do in order to get to the exit of the map
# 
# The function should return one of the following:
#     "UP"     which means the robot decides to go up
#     "LEFT"   which means the robot decides to go left
#     "RIGHT"  which means the robot decides to go right
#     "DOWN"   which means the robot decides to go down
#     "NONE"   which means the robot decides to stay in the same place

# Your task is to help the robot to make a decision on what to do next.
#
# A collection of functions that you will find very useful here:
#
#    leftIsWall()   returns True if the robot detects that the left side is blocked, otherwise it returns False
#    rightIsWall()	returns True if the robot detects that the right side is blocked, otherwise it returns False
#    upIsWall()	returns True if the robot detects that the up side is blocked, otherwise it returns False
#    downIsWall()	returns True if the robot detects that the down side is blocked, otherwise it returns False


# This is the function for task 0
def makeDecisionForTask0():
    return "UP"

# This is the function for task 1
def makeDecisionForTask1():
    global stateForTask1
    
    # When robot is in Go up state
    if stateForTask1 == "Go up":
        if upIsWall():   #If the wall is met
            stateForTask1 = "Go right"
            return "NONE"
        else:   #Keep moving up otherwise
            return "UP"
        #When the robot is in the go up state
    elif stateForTask1 == "Go right":
        #Keep moving right
        if not upIsWall():   #If there is no wall at the top
            stateForTask1 = "Go up"
            return "NONE"
        else:   #Keep moving up otherwise
            return "RIGHT"
    




# This is the function for task 2
def makeDecisionForTask2():
    global stateForTask2

    # The program has to handle cases when the exit can be on the left hand and right hand side
    # When robot is in Go up state
    if stateForTask2 == "Go up":
        if upIsWall():   #If the wall is met
            stateForTask2 = "Go right"
            return "NONE"
        else:   #Keep moving up otherwise
            return "UP"
        #When the robot is in the go RIGHT state
    elif stateForTask2 == "Go right":
        #Keep moving right
        if not upIsWall():   #If there is no wall at the top
            stateForTask2 = "Go up"
            return "NONE"
        if upIsWall() and rightIsWall():
            stateForTask2 = "Go left"
            return "NONE"
        else:   #Keep moving up otherwise
            return "RIGHT"
    elif stateForTask2 == "Go left":
        #Keep moving left
        if not upIsWall():   #If there is no wall at the top
            stateForTask2 = "Go up"
            return "NONE"
        else:   #Keep moving up otherwise
            return "LEFT"

# This is the function for task 3
def makeDecisionForTask3():
    global stateForTask3

    # There will be walls
    # When robot is in Go up state
    if stateForTask3 == "Go up":
        if upIsWall():   #If the wall is met
            stateForTask3 = "Go right"
            return "NONE"
        else:   #Keep moving up otherwise
            return "UP"
        #When the robot is in the go RIGHT state
    elif stateForTask3 == "Go right":
        #Keep moving right
        if not upIsWall():   #If there is no wall at the top
            stateForTask3 = "Go up"
            return "NONE"
        if upIsWall() and rightIsWall():
            stateForTask3 = "Go left"
            return "NONE"
        else:   #Keep moving up otherwise
            return "RIGHT"
    elif stateForTask3 == "Go left":
        #Keep moving left
        if not upIsWall():   #If there is no wall at the top
            stateForTask3 = "Go up"
            return "NONE"
        else:   #Keep moving up otherwise
            return "LEFT"



# This is the function for task 4
def makeDecisionForTask4():
    global stateForTask4

    if stateForTask4 == "Find wall":
        if upIsWall():
            stateForTask4 = "Go left"
            return "NONE"
        else:
            return "UP"

    elif stateForTask4 == "Go left":
        if not upIsWall():
            stateForTask4 = "Go up"
            return "UP"
        if leftIsWall():
            stateForTask4 = "Go down"
            return "NONE"
        else:
            return "LEFT"
    
    elif stateForTask4 == "Go right":
        if not downIsWall():
            stateForTask4 = "Go down"
            return "DOWN"
            
        if rightIsWall():
            stateForTask4 = "Go up"
            return "NONE"
        else:
            return "RIGHT"


    elif stateForTask4 == "Go up":
        if not rightIsWall():
            stateForTask4 = "Go right"
            return "RIGHT"
        if upIsWall():
            stateForTask4 = "Go left"
            return "NONE"
        else:
            return "UP"
    
    elif stateForTask4 == "Go down":
        if not leftIsWall():
            stateForTask4 = "Go left"
            return "LEFT"
        if downIsWall():
            stateForTask4 = "Go right"
            return "NONE"
        else:
            return "DOWN"


    # This is the function for task 5
def makeDecisionForTask5():
    global stateForTask5

    if stateForTask5 == "Find wall":
        if upIsWall():
            stateForTask5 = "Go left"
            return "NONE"
        else:
            return "UP"

    elif stateForTask5 == "Go left":
        if not upIsWall():
            stateForTask5 = "Go up"
            return "UP"
        if leftIsWall():
            stateForTask5 = "Go down"
            return "NONE"
        else:
            return "LEFT"
    
    elif stateForTask5 == "Go right":
        if not downIsWall():
            stateForTask5 = "Go down"
            return "DOWN"
            
        if rightIsWall():
            stateForTask5 = "Go up"
            return "NONE"
        else:
            return "RIGHT"


    elif stateForTask5 == "Go up":
        if not rightIsWall():
            stateForTask5 = "Go right"
            return "RIGHT"
        if upIsWall():
            stateForTask5 = "Go left"
            return "NONE"
        else:
            return "UP"
    
    elif stateForTask5 == "Go down":
        if not leftIsWall():
            stateForTask5 = "Go left"
            return "LEFT"
        if downIsWall():
            stateForTask5 = "Go right"
            return "NONE"
        else:
            return "DOWN"
        
# The following line of code chooses the map of the game before it starts
# 
# You can change the map of the game by changing the parameters:
# 
# - Parameter 1 can be either:
#   - "task0", "task1", "task2", "task3", "task4" or "task5"
#     which mean the predefined maps from the task that you want to work on
#
#   - "custom"
#     which means any customized map(s) that you can add in game_map.py
#
# - Parameter 2 is a number representing the map you want to use
chooseGameMap("custom", 0)

#####
#
# !!! You DO NOT need to change anything from this point onwards
#
#####

# Using the makeDecision function to set the Decision function used in each of the tasks
setDecisionFuncForTask0(makeDecisionForTask0)
setDecisionFuncForTask1(makeDecisionForTask1)
setDecisionFuncForTask2(makeDecisionForTask2)
setDecisionFuncForTask3(makeDecisionForTask3)
setDecisionFuncForTask4(makeDecisionForTask4)
setDecisionFuncForTask5(makeDecisionForTask5)

# Start the game
startGame()
