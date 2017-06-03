import turtle

def rectangular():
    window = turtle.Screen()
    window.bgcolor("red")

    b = turtle.Turtle()
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)

    window.exitonclick()

rectangular()
