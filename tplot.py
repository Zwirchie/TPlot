import turtle

# Create turtle
t = turtle.Turtle()

# Get values
speed: int = input("speed:")
steps: float = input("step_size:")
square: int = input("square:")
max_x: float = input("max_x:")
dot_size: int = input("dot_size:")

min_x: float = max_x * -1

# Make cross
t.speed(10000)
    
t.setpos(min_x * 1.5, 0)
t.setpos(max_x * 1.5, 0)
t.penup()

t.setpos(0, min_x * 2)
t.pendown()
t.setpos(0, max_x * 2)


# Setup turtle
    
t.speed(speed)
t.penup()
t.setpos(min_x, 0)

# While loop
while t.xcor() < max_x:
    t.forward(steps)

    y = pow(t.xcor(), square) / 100
    if y > max_x:
        continue
    
    t.setpos(t.xcor(), y)
    
    print(pow(t.xcor(), square))
    
    t.pendown()
    t.dot(dot_size)
    t.penup()

input()