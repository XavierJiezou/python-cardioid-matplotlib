import matplotlib.pyplot as plt
import numpy as np
from animate import animate


def cardioid_rectangular(a):
    theta = np.linspace(0, 2*np.pi, 1000)
    x = a*(1-np.cos(theta))*np.sin(theta)
    y = a*(1-np.cos(theta))*np.cos(theta)
    plt.plot(x, y, c='r')
    plt.axis('off')
    plt.savefig('heart.png')
    plt.show()


def cardioid_polar(a):
    theta = np.linspace(0, 2*np.pi, 1000)
    r = a*(1 - np.sin(theta))
    graph = plt.subplot(111, polar=True)
    graph.plot(theta, r, color='red')
    plt.savefig('heart-polar.png')
    plt.show()


if __name__ == '__main__':
    cardioid_rectangular(1) # draw a cardioid according to the parametric equation
    cardioid_polar(1) # darw a cardioid according to the polar equation
    animate(1) # darw a cardioid dynamically
