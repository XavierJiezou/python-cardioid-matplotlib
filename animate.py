import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


figure = plt.figure()
line1, = plt.axes(xlim=(-1.5, 1.5), ylim=(-2.2, 0.45)).plot([], [], c='r')
line2, = plt.axes(xlim=(-1.5, 1.5), ylim=(-2.2, 0.45)).plot([], [], c='r')


def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2


def update(i, a):
    theta = np.linspace(0, i/np.pi, 100)
    x = a*(1-np.cos(theta))*np.sin(theta)
    y = a*(1-np.cos(theta))*np.cos(theta)
    line1.set_data(x, y)
    line2.set_data(-x, y)
    return line1, line2


def animate(a):
    ani = animation.FuncAnimation(figure, update, init_func=init, frames=11, fargs=(a,), blit=True)
    plt.axis('off')
    ani.save('heart.gif')
    plt.show()


if __name__ == '__main__':
    animate(1)
