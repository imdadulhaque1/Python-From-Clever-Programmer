import turtle
im = turtle.Turtle()

n=int(input("Enter the speed: "))
im.speed(n)

r = int(input("Enter the range of the Loop: "))
for i in range(r):
    im.forward(100)
    im.right(30)

    im.forward(20)
    im.left(60)

    im.forward(50)
    im.right(30)

    im.penup()
    im.setposition(0,0)
    im.pendown()

    im.right(2)
turtle.done()