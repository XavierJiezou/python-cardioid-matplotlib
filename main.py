from parametric import cardioid_parametric
from polar import cardioid_polar
from flat import cardioid_flat
from animate import cardioid_animate


def main():
    cardioid_parametric(1)
    cardioid_polar(1)
    cardioid_flat()
    cardioid_animate(1)


if __name__ == '__main__':
    main()
