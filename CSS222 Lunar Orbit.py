# PROBLEM 3
#
# Modify the below functions acceleration and
# ship_trajectory to plot the trajectory of a
# spacecraft with the given initial position
# and velocity. Use the Forward Euler Method
# to accomplish this.
#
import numpy
from udacityplots import *

h = 1.0 # s
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
    dist2earth = numpy.linalg.norm(spaceship_position)
    vect2earth = - spaceship_position / dist2earth
    earth_comp = gravitational_constant * earth_mass * vect2earth / (dist2earth**2)
    return earth_comp


def plot_me(x,v):
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()

def ship_trajectory00():
    num_steps = 13000
    x = numpy.zeros([num_steps + 1, 2]) #
    v = numpy.zeros([num_steps + 1, 2]) # m / s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    for step in range(num_steps):
        x[step + 1, :] = x[step, :] + h * v[step, :]
        #print x[step,:]
        #print x[step+1,:]
        v[step + 1, :] = v[step, :] + h * acceleration(x[step, :])
        # print v[step,:]
        # print v[step+1:]

    plot_me(x,v)

    return x, v

x, v = ship_trajectory00()
# plot_me()




