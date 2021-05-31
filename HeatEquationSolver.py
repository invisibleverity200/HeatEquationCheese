import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
from matplotlib import cm

state_matrix_temp, state_matrix_boundary = np.meshgrid(np.linspace(0,100,100),np.linspace(0,100,100))
bool_array = np.zeros([100,100])
old_temp = np.zeros([100,100])
new_temp = np.zeros([100,100])

D = 1.55e-7
heat_stack = np.zeros([1000,100,100])
delta_x = 1
my_cmap = plt.get_cmap('inferno')
origin = 'lower'

x = 0.5
delta_x = 0.5/100
delta_t = 20

gamma = (D * delta_t) / (delta_x ** 2)


def initBoundary():
        for i in range(0,100):
                 for x  in range(0,100):
                    if (i> 75 or i < 50) or (x > 75 or x < 50):
                            old_temp[i][x] = 400
                            old_temp[i][x] = 400
                            bool_array[i][x] = 1
def step():
    for j in range(0,100):
        for i in range(0,100):
            if i >= 1 and j >= 1 and i <= 98 and j <= 98 and bool_array[j][i] != 1: 
                new_temp[j][i] = old_temp[j][i] + gamma * (old_temp[j+1][i] + old_temp[j-1][i] + old_temp[j][i+1] + old_temp[j][i-1] - 4*old_temp[j][i])
            elif bool_array[j][i] == 1:
                new_temp[j][i] = old_temp[j][i]
    
def copy():
    for i in range(0, len(new_temp)):    
        old_temp[i] = new_temp[i];     

def nextFrame(i):
    plt.gca().clear()
    ad = plt.gca().contourf(heat_stack[i*10], 100, vmin=0, vmax = 400)
    #plt.gcf().colorbar(ad,cmap = my_cmap,vmin=0, vmax = 400)

    return plt.gcf(),


def main():
    initBoundary()
    CS = plt.contourf(old_temp)
          
    plt.colorbar(CS)
    plt.show()
    idx = 0
    while(idx < 1000):
        step()
        copy()
        heat_stack[idx] = new_temp
        idx += 1
        print(idx)


    CS = plt.contourf(heat_stack[99])
          
    plt.colorbar(CS)
    plt.show()

if __name__ == "__main__":
    main()


ani = animation.FuncAnimation(plt.gcf(), nextFrame,
                               frames=100, interval=50)
ani.save('test.gif',writer='pillow',fps=10)