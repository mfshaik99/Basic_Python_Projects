import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Simple Paint App")
screen.setup(width=600, height=600)

# Create turtle for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.width(3)
pen.color("black")
pen.penup()

# Move turtle to where the mouse is and start drawing
def start_draw(x, y):
    pen.goto(x, y)
    pen.pendown()

# Draw as the mouse moves
def draw(x, y):
    pen.goto(x, y)

# Stop drawing when mouse released
def stop_draw(x, y):
    pen.penup()

# Clear screen on pressing 'c'
def clear_screen():
    pen.clear()

# Bind mouse events
screen.onscreenclick(start_draw)         # Start drawing on click
screen.ondrag(draw)                      # Draw when dragging mouse
screen.onrelease(stop_draw)              # Stop drawing on release

# Bind 'c' key to clear screen
screen.listen()
screen.onkey(clear_screen, "c")

screen.mainloop()
