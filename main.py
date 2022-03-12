import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle


import numpy as np
import math
import Integrator

step = 0.05


def f(u):
    return math.cos(u)


# This create the integral of f
A = [[a, f(a)] for a in np.arange(0, 50, step)]
B = Integrator.integrate(A, step)


# this is just the integral in function mode
def F(u):
    v = int(u/step)
    return B[v][1]


# delta t of the simulation
dt = 100

# create empty lists for the x and y data
x1, y1 = [], []
x2, y2 = [], []
x3, y3 = [], []

# create the figure and axes objects
fig = plt.figure()

p = fig.subplots(nrows=2, ncols=3)

# eliminate some of them
p[0, 1].axis('off')
p[1, 0].axis('off')
p[1, 2].axis('off')

# these have the functions
# f(x)
p1 = p[0, 0]
p1.set_ylim([-1.1, 1.1])
p1.set_xlabel('f(x)')
# p1.set_xlim([0, 20])
# F(x)
p2 = p[0, 2]
# p2.set_ylim([-1.1, 1.1])
p2.set_xlabel('F(x)')
# p2.set_xlim([0, 20])
p1.grid()
p2.grid()

# this will have the integrator
p3 = p[1, 1]
# the big disk
r = 1
angle = np.linspace(0, 2 * np.pi, 150)
x = r * np.cos(angle)+0.5
y = r * np.sin(angle)
p3.plot(0.5, 0, '.', color='black')  # middle
p3.plot(x, y, color='black')  # circle
# p3.plot([0.5, 0.5], [-1, 1], '-', color='black')  # vertical axis in the middle
# line rotating on the big disk
ln, = p3.plot([], [], '-', color='black')

# the wheel
wheel = Rectangle((0.4, f(0)-0.05), 0.2, 0.1, fc='black')
p3.add_patch(wheel)
# the line moving on the wheel
line, = p3.plot([0.4, 0.4], [1, 0.9], '-', color='white')


# remove the axis
p1.xaxis.set_visible(False)
p1.yaxis.set_visible(False)
p2.xaxis.set_visible(False)
p2.yaxis.set_visible(False)

p3.xaxis.set_visible(False)
p3.yaxis.set_visible(False)
for spine in ['top', 'right', 'left', 'bottom']:
    p3.spines[spine].set_visible(False)


# to generate the frames
def gen():
    h = 0
    while h <= 50:
        yield h
        h += step


# to determine how the point moves horizontally in the wheel
def line_position(h):
    xp = line.get_data()[0][0] - 0.4  # get the previous position
    # add f(h)/30 to move smoothly
    # % 0.2 is to back to the beginning of the wheel
    position = 0.4 + ((xp - f(h)/30) % 0.2)
    return position


def update(h):
    # f(x)
    x1.append(h)
    y1.append(f(h))  # the x and y values

    # p1.clear()  # if commented, stuff gets really psychedelic
    fline, = p1.plot(x1, y1, 'b')  # well... this is plotting

    # F(x)
    x2.append(h)
    y2.append(F(h))  # the x and y values
    # p2.clear()  # if commented, stuff gets really psychedelic
    Fline, = p2.plot(x2, y2, 'r')  # well... this is plotting

    # wheel
    wheel.set_y(f(h)-0.05)

    # line that makes wheel seem like its spinning
    xp = line_position(h)
    line.set_data([xp, xp], [f(h) + 0.04, f(h) - 0.04])

    # line showing that the circle is moving
    X0 = (r - 0.2) * np.cos(-h) + 0.5
    Y0 = (r - 0.2) * np.sin(-h)
    X1 = r * np.cos(-h) + 0.5
    Y1 = r * np.sin(-h)
    ln.set_data([X0, X1], [Y0, Y1])
    return line, ln, fline, Fline, wheel


# run the animation
# blit is to optimize
# interval is the interval between each step of the animation
ani = FuncAnimation(fig, update, gen, blit=True, interval=dt)

plt.show()
