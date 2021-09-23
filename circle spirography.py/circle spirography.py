import turtle
turtle.bgcolor("black")
turtle.pensize(1)
turtle.speed(40)


for i in range(12   ):
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colours)
        turtle.circle(1000)
        turtle.left(10)

turtle.hideturtle()
turtle.done(  )

