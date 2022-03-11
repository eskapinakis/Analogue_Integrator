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


def F(u):
    v = int(u/step)
    return B[v][1]


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
p1 = p[0, 0]
p1.set_ylim([-1.1, 1.1])
p1.set_xlim([0, 20])
p2 = p[0, 2]
p2.set_ylim([-1.1, 1.1])
p2.set_xlim([0, 20])
p1.grid()
p2.grid()
# and this will have the circle
p3 = p[1, 1]
# so it doesn't have axis
p3.xaxis.set_ticklabels([])
p3.yaxis.set_ticklabels([])
# define the circle
r = 1
angle = np.linspace(0, 2 * np.pi, 150)
x = r * np.cos(angle)+0.5
y = r * np.sin(angle)
p3.plot(0.5, 0, '.', color='black')  # middle
p3.plot(x, y, color='black')  # circle
# define the wheel
wheel = Rectangle((0.35, f(0)-0.05), 0.3, 0.1, fc='black')
p3.add_patch(wheel)
# define the point
point, = p3.plot(0.5, f(0), '.', color='red')
# define the line
ln, = p3.plot([], [], '-', color='black')


# to generate the frames
def gen():
    h = 0
    while h <= 50:
        yield h
        h += step


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

    # point
    yp = f(h)  # vertically it's just f(x)
    xp = 0.4 + (h % 1)/5
    point.set_data(np.array([xp, yp]))

    # wheel
    wheel.set_y(f(h)-0.05)

    # line
    X0 = (r - 0.3) * np.cos(h) + 0.5
    Y0 = (r - 0.3) * np.sin(h)
    X1 = r * np.cos(h) + 0.5
    Y1 = r * np.sin(h)
    ln.set_data([X0, X1], [Y0, Y1])
    return point, ln, fline, Fline, wheel


# run the animation
# blit is to optimize
# interval is the interval between each step of the animation
ani4 = FuncAnimation(fig, update, gen, blit=True, interval=40)

plt.show()
