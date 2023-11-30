"""Holds planet class."""
from turtle import Turtle

X_SHIFT = -700


class Planet():
    """Holds planet information and turtle object."""

    def __init__(self, color, distance, size, speed):
        """Set up planet information."""
        self.color = color
        self.distance = distance
        self.size = size
        self.speed = speed
        # init turtle object
        self.turtle = Turtle()

    def set_up_turtle(self):
        """Set up planet turtle object."""
        # add turtle attributes
        self.turtle.color(self.color)
        self.turtle.shape('circle')
        # this speed only affects moving up starting location
        self.turtle.speed(1000)
        # move to correct location
        self.turtle.penup()
        self.turtle.goto(self.distance+X_SHIFT, 0)
        self.turtle.shapesize(self.size)
        self.turtle.setheading(90)
        self.turtle.pendown()

    def move_planet(self, delta_d, angle):
        """Move planet with specified distance and angle."""
        self.turtle.forward(delta_d)
        self.turtle.left(angle)
