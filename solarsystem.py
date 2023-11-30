"""ASTRO 102 CREATIVE ASSIGNMENT: Animated Solar System Relative Distances and Periods."""
import math
from turtle import Turtle
from turtle import Screen
from planet import Planet

X_SHIFT = -700
DISTANCE_MULTIPLIER = 5


def orbit_planets(planets):
    """Animate planet orbits with a tick-based system."""
    sides = 90.0
    for _ in range(int(sides)):  # repeat the indented lines 12 times
        # each planet
        for planet in planets:
            # this math was harder than it should've been
            delta_d = 2.0*math.pi*planet.distance/(sides/planet.speed)
            angle = (360.0/sides)*planet.speed
            planet.move_planet(delta_d, angle)


def set_up_sun():
    """Create sun turtle and stamp shape."""
    sun = Turtle()
    sun.color('yellow')
    sun.shape('circle')
    sun.shapesize(0.6)
    sun.speed(1000)
    sun.penup()
    sun.goto(X_SHIFT, 2)
    sun.stamp()


def create_planets():
    """Create list of planet objects and set up their turtle object."""
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
    """Animate Solar System relative distances and periods."""
    space = Screen()
    space.bgcolor('black')

    set_up_sun()

    planets = create_planets()

    orbit_planets(planets)

    space.exitonclick()


if __name__ == '__main__':
    main()
