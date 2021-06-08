import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
from matplotlib import cm

#time is in weeks
#disctance is in 1/10 AU
#mass in in earth mass
#vel is in 1/10 AU/week


Grav = (6.67408e-12 / ((1/10)*1.496e+11)**3) * 5.972*10**24 * 604800**2 #check me
d_t = 1

pos_framesX = np.zeros([100,3])
pos_framesY = np.zeros([100,3])

old_pos = np.array([(10,10),(20,20),(40,40)])
old_vel = np.array([(0,0),(0,0),(0,0)]) 

new_pos = np.zeros([3,2])
new_vel = np.zeros([3,2])
mass = [1,2,3]

def calc_Fg(m1, m2, r):
    Fg =  (Grav*m1*m2) / (r+0.0000001)**2
    print((Fg* (1/10)*1.496e+11 * 5.972*10**24)  / 604800**2)
    return Fg

def calcForceVec(p):
    F_vec = np.array([0,0])
    for x in range(2):
        if x != p: 
            vec = old_pos[x] - old_pos[p]
            m1 = mass[x]
            m2 = mass[p]
            Fg = calc_Fg(m1,m2,np.linalg.norm(vec))
            unit_vec = vec / (np.linalg.norm(vec)+0.0000001)
            
            F_vec = F_vec + np.array(unit_vec)*Fg
            print(np.linalg.norm(F_vec))
    return F_vec



def calcAccVec(p, F_vec):
    acc = np.linalg.norm(F_vec) / mass[p] 
    unit_vec =  F_vec / np.linalg.norm(F_vec)
    acc__vec = acc*unit_vec


    return acc__vec

def calcVelVec(p,A_vec):
       new_vel[p] = old_vel[p][0]+A_vec[0]*d_t,old_vel[p][1]+A_vec[1]*d_t
       return new_vel[p]

def calcNewPos(p):
    F_vec = calcForceVec(p)
    A_vec = calcAccVec(p,F_vec)
    V_vec = calcVelVec(p,A_vec)
    new_pos[p] = old_pos[p][0]+V_vec[0]*d_t,old_pos[p][1]+V_vec[1]*d_t


def copyArray(a,b):
    for x in range(len(a)):
        a[x] = b[x]
    

def step(idx):
    for p in range(2):
        calcNewPos(p)
        pos_framesX[idx][p] = new_pos[p][0] #check 
        pos_framesY[idx][p] = new_pos[p][1]
        idx = idx + 1
    
    copyArray(old_pos,new_pos)
    copyArray(old_vel,new_vel)

def animate(i):
    plt.gca().clear()
    ad = plt.gca().scatter(pos_framesX[i], pos_framesY[i])
    #plt.gcf().colorbar(ad,cmap = my_cmap,vmin=0, vmax = 400)

    return plt.gcf(),


def main():
    for idx in range(99):
        step(idx)
    



if __name__ == "__main__":
    main()


ani = animation.FuncAnimation(plt.gcf(), animate,
                               frames=100, interval=50)
ani.save('test.gif',writer='pillow',fps=10)