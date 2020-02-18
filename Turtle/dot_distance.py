import turtle
im = turtle.Turtle()

dot_distance = int(input("Enter the distance of dot: "))
width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

im.penup()

for i in range(height):
    for j in range(width):
        im.dot()
        im.forward(dot_distance)
    im.backward(dot_distance*width)
    im.right(90)
    im.forward(dot_distance)
    im.left(90)

turtle.done()
