import matplotlib.pyplot as plt
import numpy as np


def cardioid(a):
    theta = np.linspace(0, 2*np.pi, 1000)
    x = a*(1-np.cos(theta))*np.sin(theta)
    y = a*(1-np.cos(theta))*np.cos(theta)
    plt.plot(x, y, c='r')
    plt.axis('off')
    plt.savefig('heart.png')
    plt.show()


if __name__ == '__main__':
    cardioid(1)
