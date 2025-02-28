import turtle

def draw_koch_segment(t, length, level):
    """
    Function to draw one segment of a Koch snowflake
    :param t: turtle object
    :param length: line length
    :param level: recursion level
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)
        t.right(120)
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)

def draw_koch_snowflake(t, length, level):
    """
    Function for drawing Koch snowflakes
    :param t: turtle object
    :param length: length of the side of the snowflake
    :param level: recursion level
    """
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    level = int(input("Specify the recursion level (0 or more): "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    draw_koch_snowflake(t, 400, level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()