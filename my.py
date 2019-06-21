import turtle
my_turtle=turtle.Turtle()

for i in range(36):
    if(i>18):
        my_turtle.color("Blue")
        my_turtle.circle(100)
        my_turtle.right(10)
    else:
        my_turtle.color("Red")
        my_turtle.circle(100)
        my_turtle.right(10)
