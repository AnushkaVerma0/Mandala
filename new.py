import turtle

def draw_mandala():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10000)
    turtle.bgcolor("black")  
    pen.pensize(2)

    initial_size = 30  

    for i in range(150):
        pen.color(colors[i % 6])
        pen.left(61)
        pen.forward(initial_size + i)
        pen.right(61)
        pen.circle((i)//6)
        pen.left(61)
    pen.hideturtle()


draw_mandala()

turtle.done()
