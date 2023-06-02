import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

# Draw a circle
def draw_circle():
    t.circle(50)

# Draw a triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.right(120)

# GUI Controls
def setup_gui():
    screen = turtle.Screen()
    screen.title("Shapes and GUI Controls")
    
    # Square button
    square_button = turtle.Turtle()
    square_button.shape("square")
    square_button.shapesize(2, 2)
    square_button.penup()
    square_button.goto(-150, 0)
    square_button.onclick(draw_square)

    # Circle button
    circle_button = turtle.Turtle()
    circle_button.shape("circle")
    circle_button.shapesize(2, 2)
    circle_button.penup()
    circle_button.goto(0, 0)
    circle_button.onclick(draw_circle)

    # Triangle button
    triangle_button = turtle.Turtle()
    triangle_button.shape("triangle")
    triangle_button.shapesize(2, 2)
    triangle_button.penup()
    triangle_button.goto(150, 0)
    triangle_button.onclick(draw_triangle)

    turtle.done()

# Setup the GUI
setup_gui()
