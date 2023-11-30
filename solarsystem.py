from turtle import *
import math
import time

LEFT_SHIFT = -500
DISTANCE_MULTIPLIER = 4


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
        self.t.goto(self.distance+LEFT_SHIFT, 0)
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


def set_up_sun():
    sun = Turtle()
    sun.color('yellow')
    sun.shape('circle')
    sun.shapesize(0.6)
    sun.speed(1000)
    sun.penup()
    sun.goto(LEFT_SHIFT, 2)
    sun.stamp()


def create_planets():
    mercury = Planet('gray30', 3.9*DISTANCE_MULTIPLIER, 0.2, 4.15)
    venus = Planet('OrangeRed2', 7.2*DISTANCE_MULTIPLIER, 0.2, 1.62)
    earth = Planet('green', 10*DISTANCE_MULTIPLIER, 0.2, 1)
    mars = Planet('tomato', 15.2*DISTANCE_MULTIPLIER, 0.2, 0.53)
    jupiter = Planet('peru', 52*DISTANCE_MULTIPLIER, 0.5, 0.083)
    saturn = Planet('PeachPuff', 95.4*DISTANCE_MULTIPLIER, 0.5, 0.034)
    uranus = Planet('LightSeaGreen', 192*DISTANCE_MULTIPLIER, 0.5, 0.012)
    neptune = Planet('CornflowerBlue', 300.6*DISTANCE_MULTIPLIER, 0.5, 0.0061)

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    for planet in planets:
        planet.set_up_turtle()

    return planets


def main():
    s = Screen()
    s.bgcolor('black')

    set_up_sun()

    planets = create_planets()

    orbit_planets(planets)
    
    s.exitonclick()

if __name__ == '__main__':
    main()


