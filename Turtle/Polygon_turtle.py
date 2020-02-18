import turtle
polygon = turtle.Turtle()
num_side = int(input("Enter the Number os side: "))
side_length = int(input("Enter the Length of side: "))
angle = 360 / num_side

for i in range(num_side):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()