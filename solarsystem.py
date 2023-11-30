"""ASTRO 102: Animated Solar System Relative Distances and Periods."""
import math
from turtle import Turtle
from turtle import Screen
from planet import Planet

X_SHIFT = -700
DISTANCE_MULTIPLIER = 5


def orbit_planets(planets):
    """Animate planet orbits with a tick-based system."""
    # number of ticks for Earth to complete one revolution
    ticks = 90.0

    # pre-compute each planet's orbit info to avoid duplicate work during ticks
    for planet in planets:
        # this math was harder than it should've been
        # compute distance change with fraction of circumference per tick
        delta_d = (2.0*math.pi*planet.distance/ticks)*planet.speed
        # compute angle based on fraction of 360 degrees needed for each tick
        angle = (360.0/ticks)*planet.speed
        # save computed distance change and angle
        planet.set_orbit_info(delta_d, angle)

    # each tick
    for _ in range(int(ticks)):
        # each planet
        for planet in planets:
            # move planet along orbit by one tick
            planet.move_planet()


def set_up_sun():
    """Create sun turtle and stamp shape."""
    sun = Turtle()
    sun.color('yellow')
    sun.shape('circle')
    sun.shapesize(0.6)
    # this speed only affects moving up starting location
    sun.speed(1000)
    sun.penup()
    sun.goto(X_SHIFT, 2)
    sun.stamp()


def create_planets():
    """Create list of planet objects and set up their turtle object."""
    # Planet(
    #   color,
    #   distance to sun (10 = 1 AU),
    #   size (not kept accurate),
    #   speed (1 = 1 Earth year)
    # )
    mercury = Planet('gray30', 3.9*DISTANCE_MULTIPLIER, 0.2, 4.15)
    venus = Planet('OrangeRed2', 7.2*DISTANCE_MULTIPLIER, 0.2, 1.62)
    earth = Planet('green', 10*DISTANCE_MULTIPLIER, 0.2, 1)
    mars = Planet('tomato', 15.2*DISTANCE_MULTIPLIER, 0.2, 0.53)
    jupiter = Planet('peru', 52*DISTANCE_MULTIPLIER, 0.5, 0.083)
    saturn = Planet('PeachPuff', 95.4*DISTANCE_MULTIPLIER, 0.5, 0.034)
    uranus = Planet('LightSeaGreen', 192*DISTANCE_MULTIPLIER, 0.35, 0.012)
    neptune = Planet('CornflowerBlue', 300.6*DISTANCE_MULTIPLIER, 0.35, 0.0061)

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    # set up turtle for each planet
    for planet in planets:
        planet.set_up_turtle()

    return planets


def main():
    """Animate Solar System relative distances and periods."""
    # create empty space for turtle object
    space = Screen()
    space.bgcolor('black')

    # create stationary sun turtle object
    set_up_sun()

    # create planet objects to be animated
    planets = create_planets()

    # animate planet orbits
    orbit_planets(planets)

    # gui waits for click before exiting
    space.exitonclick()


if __name__ == '__main__':
    main()
