#
# This file is for graphing data.
# Ignore it
#
#


import turtle



def letterFreqPlot(List):
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.setworldcoordinates(0,.05,len(List)+1,max(List)+.1)
    print(9)
    t.hideturtle()
    t.speed(0)
    for i in range(len(List)):
        print(i, int(List[i]))
        t.goto(i, int(List[i]))
        t.dot(10)
    print('Click to exit')
    screen.exitonclick()


