import turtle


# def draw_square():
#     window = turtle.Screen()
#     window.bgcolor('red')
#
#     brad = turtle.Turtle()
#     brad.shape('turtle')
#     brad.color('yellow')
#     brad.speed(2)
#     brad.forward(100)
#     brad.right(90)
#     brad.forward(100)
#     brad.right(90)
#     brad.forward(100)
#     brad.right(90)
#     brad.forward(100)
#     brad.right(90)
#
#     angie = turtle.Turtle()
#     angie.shape('arrow')
#     angie.color('blue')
#     angie.circle(100)
#
#
#     window.exitonclick()

def draw_shape():
    window = turtle.Screen()
    window.bgcolor('red')

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()


def draw_square():
    square = turtle.Turtle()

    square.shape('turtle')
    square.color('yellow')
    square.speed(2)

    i = 0
    while i < 4:
        square.forward(100)
        square.right(90)
        i = i + 1

def draw_circle():
    circ = turtle.Turtle()

    circ.shape('arrow')
    circ.color('blue')

    circ.circle(100)


def draw_triangle():
    tri = turtle.Turtle()

    tri.color('green')
    tri.speed(2)

    tri.left(180)
    tri.forward(200)

    i = 0
    while i < 2:
        tri.right(120)
        tri.forward(200)
        i += 1






if __name__ == '__main__':
    # draw_square()
    draw_shape()
