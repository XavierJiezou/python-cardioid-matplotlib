import matplotlib.pyplot as plt
import numpy as np


def flat():
    t = np.linspace(0, np.pi, 1000)
    x = np.sin(t)
    y = np.cos(t) + np.power(x, 2/3)
    plt.plot(x, y, color='r')
    plt.plot(-x, y, c='r')
    plt.savefig('flat.png')
    plt.show()


if __name__ == '__main__':
    flat()
