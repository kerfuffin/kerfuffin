import numba
import numpy as np

@numba.jit(nopython=True)
def gen_ticks(length):
    ticks = []
    for i in range(0, length, 1):
        ticks.append(i)
    return ticks


def gen_average(data_x, data_y, step):
    temp = [[] for i in range(2)]
    n = 1
    left = 0
    for i in range(len(data_y)):
        if(i>n*step and left<i):
            temp[1].append(np.average(data_y[left:(i-1)]))
            temp[0].append(data_x[int((i+left)/2)])
            left = i
            n = n+1
    return temp
        
