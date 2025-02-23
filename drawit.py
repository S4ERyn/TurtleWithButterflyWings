import turtle

# Set up the window and the turtle
win = turtle.Screen()
win.bgcolor("white")
win.title("Butterfly Wing Fractal")
fractal_turtle = turtle.Turtle()
fractal_turtle.speed(0)

def draw_branch(turtle, branch_length, level):
    if level == 0:
        return
    
    # Draw the main branch
    turtle.forward(branch_length)
    
    # Draw the first branch
    turtle.left(45)
    draw_branch(turtle, branch_length / 2, level - 1)
    
    # Draw the second branch
    turtle.right(90)
    draw_branch(turtle, branch_length / 2, level - 1)
    
    # Return to the main branch
    turtle.left(45)
    turtle.backward(branch_length)

def draw_wing(turtle, branch_length, level):
    # Draw the first half of the wing
    draw_branch(turtle, branch_length, level)
    
    # Reflect and draw the second half of the wing
    turtle.right(180)
    draw_branch(turtle, branch_length, level)

# Move the turtle to starting position
fractal_turtle.penup()
fractal_turtle.goto(0, -200)
fractal_turtle.pendown()

# Draw the butterfly wing fractal
draw_wing(fractal_turtle, 100, 4)

# Hide the turtle and display the window
fractal_turtle.hideturtle()
turtle.done()