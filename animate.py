import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

figure = plt.figure()
line1, = plt.axes(xlim=(-1.5, 1.5), ylim=(-2.2, 0.45)).plot([], [], c='r')
line2, = plt.axes(xlim=(-1.5, 1.5), ylim=(-2.2, 0.45)).plot([], [], c='r')


def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2


def update(i):
    theta = np.linspace(0, i/np.pi, 100)
    x = 1*(1-np.cos(theta))*np.sin(theta)
    y = 1*(1-np.cos(theta))*np.cos(theta)
    line1.set_data(x, y)
    line2.set_data(-x, y)
    return line1, line2


def animate():
    ani = animation.FuncAnimation(figure, update, init_func=init, frames=11)
    plt.axis('off')
    ani.save('heart.gif')
    plt.show()


if __name__ == '__main__':
    animate()
