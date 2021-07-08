import matplotlib.pyplot as plt
import numpy as np


def cardioid_polar(a):
    theta = np.linspace(0, 2*np.pi, 1000)
    r = a*(1 - np.sin(theta))
    graph = plt.subplot(111, polar=True)
    graph.plot(theta, r, color='red')
    plt.savefig('./img/heart-polar.png')
    plt.show()


if __name__ == '__main__':
    cardioid_polar(1)
