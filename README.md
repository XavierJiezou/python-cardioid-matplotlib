English | [简体中文](/README.zh.md)
# Introduction
Make a cardioid by using python's matplotlib library.
# Demo
| Heart | Heart-Poloar |
|:---:|:---:|
| ![heart.png](./img/heart.png) | ![heart-poloar.png](./img/heart-polar.png) |
| **Heart-Flat** | **Heart-Gif** |
| ![heart-flat.png](./img/heart-flat.png) | ![header.gif](./img/heart.gif) |
# Install
```
pip install matplotlib
```
# Equations
## Parametric Equation
<img src="https://latex.codecogs.com/svg.image?\left\{\begin{matrix}x(\theta&space;)=a\left(1-cos\theta&space;\right)&space;sin\theta&space;\\y(\theta&space;)=a\left(1-cos\theta&space;\right)&space;cos\theta&space;\end{matrix}\right." title="Parametric Equation" />

## Polar Equation
![Polar Equation](https://latex.codecogs.com/svg.image?r=&space;a\left(1-sin\theta&space;\right))
# Usage
1. Git clone
```
git clone https://github.com/XavierJiezou/python-cardioid-matplotlib.git
cd python-cardioid-matplotlib
```
2. Draw a cardioid according to the parametric equation.
```
python .\example\parametric.py
```
3. Draw a cardioid according to the poloar equation.
```
python .\example\polar.py
```
4. Draw a flat cardioid.
```
python .\example\flat.py 
```
5. Draw a cardioid dynamicly.
```
python .\example\animate.py 
```
6. Run all that from 2 to 5.
```
python .\main.py
```
# Reference
> [https://en.wikipedia.org/wiki/Cardioid](https://en.wikipedia.org/wiki/Cardioid)
> 
> [https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.animation.FuncAnimation.html](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.animation.FuncAnimation.html)
> 
> [https://zhuanlan.zhihu.com/p/32380300](https://zhuanlan.zhihu.com/p/32380300)