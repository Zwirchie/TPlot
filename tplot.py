import turtle

# VARIABLES
axis_x: float = 500.0

# FUNCTIONS

# Create a cross for coordinates
def cross(max_x: float, max_y: float):
    # Create the "Cross Turtle" and set it up
    ct = turtle.Turtle()
    ct.speed(10000)
    
    # Draw x-Axis
    min_x = max_x * -1

    ct.setpos(min_x * 1.5, 0)
    ct.setpos(max_x * 1.5, 0)
    ct.penup()

    # Draw y-Axis
    min_y = max_y * -1
    ct.setpos(0, min_y * 1.5)
    ct.pendown()
    ct.setpos(0, max_y * 1.5)

    # Delete turtle
    ct.hideturtle()

# PROCESS

# Create cross
cross(axis_x, axis_x)

# EXIT
input()