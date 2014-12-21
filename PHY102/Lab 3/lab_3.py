# lab_2.py
#
# Author:He Bai
# Student ID:997677931
#
# This library was written as part of Physics 102: Computational Laboratory
# in Physics, Fall 2014.

# import required libraries
import math
import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt

S_x = np.mat([[0, 0.5], [0.5, 0]])
S_y = np.mat([[0, -0.5j], [0.5j, 0]])
S_z = np.mat([[0.5, 0], [0, -0.5]])
S_2 = S_x.T*S_x + S_y.T*S_y + S_z.T*S_z

# Exercise 1
def expectation_S_x(s_array):
    """calculates the expectation value of S_x
    Arguments
    =========
    s_arrar = non-normalized two element spinor array [alpha, beta]

    Returns
    ======
    float = expectation value of S_x
    """
    # start your code here
    quotion = math.sqrt(s_array[0]**2 + s_array[1]**2)
    spinor = np.mat([[s_array[0] / quotion], [s_array[1] / quotion]])
    return (spinor.T * S_x * spinor)[0, 0]

def expectation_S_y(s_array):
    """calculates the expectation value of S_y
    Arguments
    =========
    s_arrar = non-normalized two element spinor array [alpha, beta]

    Returns

    Note: up and down do not have to be normalized

    Returns
    ======
    float = expectation value of S_y
    """
    # start your code here
    quotion = math.sqrt(s_array[0]**2 + s_array[1]**2)
    spinor = np.mat([[s_array[0] / quotion], [s_array[1] / quotion]])
    return (spinor.T * S_y * spinor)[0, 0]

def expectation_S_z(s_array):
    """calculates the expectation value of S_z
    Arguments
    =========
    s_arrar = non-normalized two element spinor array [alpha, beta]

    Returns
    ======
    float = expectation value of S_z
    """
    # start your code here
    quotion = math.sqrt(s_array[0]**2 + s_array[1]**2)
    spinor = np.mat([[s_array[0] / quotion], [s_array[1] / quotion]])
    return (spinor.T * S_z * spinor)[0, 0]

def expectation_S_sq(s_array):
    """calculates the expectation value of S_sq
    Arguments
    =========
    s_arrar = non-normalized two element spinor array [alpha, beta]

    Returns

    Note: up and down do not have to be normalized

    Returns
    ======
    float = expectation value of S_sq
    """
    # start your code here
    quotion = math.sqrt(s_array[0]**2 + s_array[1]**2)
    spinor = np.mat([[s_array[0] / quotion], [s_array[1] / quotion]])
    return (spinor.T * S_2 * spinor)[0, 0]

# Exercise 2
def is_chaotic(J):
    """Determines whether the Jacobian matrix is chaotic
    Arguments
    ==========
    J = string, list of lists, array of arrays, or matrix

    Returns
    =======
    bool = True if chaotic, False otherwise
    """
    # start your code here
    margin = 0.0001
    J = np.mat(J)
    eigens = linalg.eigvals(J)
    less = 0
    equal = 0
    more = 0
    for eigen in eigens:
        if (abs(eigen - 1) < margin):
            equal = equal + 1
        else:
            if (eigen < 1):
                less = less + 1
            if (eigen > 1):
                more = more + 1
    if (less == 1 and equal == 1 and more == 1):
        return True
    else:
        return False


# Exercise 3
def make_plot():
    """Makes a plot similar to sample_plot.png and saves it in the
    current directory as "exercise_3.pdf".
    Arguments
    ==========
    None

    Returns
    ======
    None
    """
    # start your code here
    x = np.arange(0, 2, 0.01)

    y1 = np.sin(2 * math.pi * x)
    plt.plot(x, y1, color = 'orange', linewidth = 2, marker = 'o', markeredgewidth = 0, label='_nolegend_')

    y2 = np.exp(-x)
    plt.plot(x, y2, color = 'blue', linewidth = 2, label='_nolegend_')

    y3 = np.sin(2 * math.pi * x) * np.exp(-x)
    plt.plot(x, y3, color = 'red', linewidth = 2, marker = 's', markeredgewidth = 0, label='_nolegend_')

    x1 = np.arange(0, 2, 0.1)
    y4 = np.log(x1 + 1)
    plt.plot(x1, y4, color = 'green', linewidth = 0, marker = 'o', markeredgewidth = 0, label='_nolegend_')

    plt.xlabel('times')
    plt.ylabel('volts')
    plt.title('Damped osillation')
    plt.xlim(0, 2)
    plt.ylim(-1, 1.5)
    plt.grid(color='gray', linestyle='-')
    plt.savefig('exercise_3.pdf')
    return None


