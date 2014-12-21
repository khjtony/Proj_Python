# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

# define constants
g = 9.8
l = 1.5

# difine the system of differential equations
def diff_sys(variables, t):
    theta = variables[0]
    v_theta = variables[1]
    return (v_theta, -g/l*np.sin(theta))

# define the initial conditions
init_cond = (np.pi/2.0, 0) # theta=pi/2, v_theta=0

# create a time array
times = np.linspace(0, 20, 1500)

# calculate solutions
sols = integrate.odeint(diff_sys, init_cond, times)

# convert theta to x and y
x = l*np.sin(sols[:,0])
y = -l*np.cos(sols[:,0])

# create a plot
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()
ax.set_aspect('equal')
line, = ax.plot([], [], 'o-', lw=4, zorder=0, markeredgecolor='b')
circle = plt.Circle((x[0], y[0]),.2,color='none', zorder=1)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    ax.add_patch(circle)
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    circle.set_color('blue')
    line.set_data([0, x[i]], [0, y[i]])
    time_text.set_text('time = {0:.1f}s'.format(times[i]))
    circle.center = (x[i], y[i])
    return circle, line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
    interval=33, blit=True, init_func=init)

#ani.save('double_pendulum.mp4', fps=15)
plt.show()
 
