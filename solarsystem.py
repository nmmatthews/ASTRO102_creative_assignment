from turtle import *
import math
import time

left_shift = -500


def create_polygon(turtle):
    sides = 8
    angle = 360/sides
    turtle.setheading(90)    # point due north
    for sides in range(sides):  # repeat the indented lines 12 times
        turtle.forward(angle)      # move forward by 40 units
        turtle.right(angle)        # change ?? to the amount to turn

class Planet():
    def __init__(self, color, distance, size, speed):
        self.color = color
        self.distance = distance
        self.size = size
        self.speed = speed
    
    def set_up_turtle(self):
        # init turtle object
        self.t = Turtle()
        # add turtle attributes
        self.t.color(self.color)
        self.t.shape('circle')
        self.t.speed(1000)
        # move to correct location
        self.t.penup()
        self.t.goto(self.distance+left_shift, 0)
        self.t.shapesize(self.size)
        self.t.setheading(90)
        self.t.pendown()


def orbit_planets(planets):
    sides = 90.0
    for _ in range(int(sides)):  # repeat the indented lines 12 times
        # each planet
        for planet in planets:
            d = 2.0*math.pi*planet.distance/(sides/planet.speed)
            angle = 360.0/sides
            planet.t.forward(d)
            planet.t.left(angle*planet.speed)
        


def main():
    s = Screen()
    s.bgcolor('black')

    sun = Turtle()
    sun.color('yellow')
    sun.shape('circle')
    sun.shapesize(0.5)
    sun.penup()
    sun.goto(left_shift, 2)
    sun.stamp()
    
    d_mult = 4
    mercury = Planet('silver', 3.9*d_mult, 0.2, 4.14)
    venus = Planet('gray', 7.2*d_mult, 0.2, 1.62)
    earth = Planet('green', 10*d_mult, 0.2, 1)
    mars = Planet('red', 15.2*d_mult, 0.2, 0.42)
    jupiter = Planet('orange', 52*d_mult, 0.5, 0.08)
    saturn = Planet('brown', 95.4*d_mult, 0.5, 0.03)
    uranus = Planet('blue', 192*d_mult, 0.5, 0.012)
    neptune = Planet('purple', 300.6*d_mult, 0.5, 0.0061)

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    for planet in planets:
        planet.set_up_turtle()

    orbit_planets(planets)
    
    s.exitonclick()

if __name__ == '__main__':
    main()


