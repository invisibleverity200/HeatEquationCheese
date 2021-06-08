import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
from matplotlib import cm
from numba import jit

import sys

max_x_y = int(sys.argv[1])
max_color_value = int(sys.argv[2])

color_values = np.ones([max_x_y,max_x_y])
start  = float(sys.argv[3])
end  = float(sys.argv[4])


x2 = np.linspace(start, end, max_x_y)
y2 = np.linspace(start, end,max_x_y)

A, B = np.meshgrid(x2 - 1, y2-1)
C = 2.0 * (A + B * 1j) - 0.5

def calc_color(x,y):
    color_value = 0
    n = 0
    while n < 200 and abs(color_value) < max_color_value:
        color_value = color_value**2 + C[y][x]
        n += 1
    color_values[y][x] = (200 - n - np.log(np.log(color_value) / np.log(4)) / np.log(2))


def step():
    for y in range(0,max_x_y):
        for x in range(0,max_x_y):
            calc_color(x,y)
            print(str(x) +"            "+ str(y))
    #100, vmin=0, vmax = 400

def main():
    step()
    plt.imshow(color_values, cmap=plt.cm.twilight_shifted)
    plt.show()

if __name__ == "__main__":
    main()


            