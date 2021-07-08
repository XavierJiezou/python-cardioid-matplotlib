from example.parametric import cardioid_parametric
from example.polar import cardioid_polar
from example.flat import cardioid_flat
from example.animate import cardioid_animate


def main():
    cardioid_animate(1)
    cardioid_parametric(1)
    cardioid_polar(1)
    cardioid_flat()


if __name__ == '__main__':
    main()
