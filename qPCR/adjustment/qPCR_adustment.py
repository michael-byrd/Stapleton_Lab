__title__ = 'qPCR Adjustment'
__author__ = 'Michael Byrd'

import numpy as np
import random, math
import pandas as pd

def qPCR_Adusjutment(xVec, yVec):
    return np.mean(np.subtract.outer(xVec, yVec))

def qPCR_Simulation(n):
    alpha = None
    beta = 2


    # Create Vectors
    # arr = np.empty((0,2*n), int)
    x = np.empty([2*n, 1])
    y = np.empty([2*n, 1])

    # Populate Vectors
    for i in range(-n, n+1):
        print(math.pow(10, i))
        xVal = 1 + beta * math.pow(10, i) + np.random.normal(0, 1)
        yVal = 2 + beta * math.pow(10, i) + np.random.normal(0, 1)

        np.put(x, [i+n-1], [xVal])
        np.put(y, [i+n-1], [yVal])

    return qPCR_Adusjutment(x,y)

def Neill2018_Data_BlockAdju(xInput, yInput):
    for i in range(5):
        temp_x = np.array([xInput[3*i], xInput[3*i + 1], xInput[3*i + 2]])
        temp_y = np.array([yInput[3*i], yInput[3*i + 1], yInput[3*i + 2]])
        print(math.pow(10,2-i) , "Adjustment:", qPCR_Adusjutment(temp_x, temp_y))

def Neill2018_Data():

    data = np.genfromtxt("Neill2018calibrations.csv", dtype=float, delimiter=',', names=True)
    # amount_gblock+ire
    x = []
    y = []
    for i in range(len(data)):
        x.append(data[i][4])
        y.append(data[i][2])

    # all_productsCp1
    x = np.array(x)

    # test1_Cp1
    y = np.array(y)

    Neill2018_Data_BlockAdju(x,y)

    # # 50_50gblocks
    # print('\n' + "50/50")
    #
    # x = []
    # y = []
    # for i in range(len(data)):
    #     x.append(data[i][15])
    #     y.append(data[i][14])
    #
    # # allproductsCp1_50_50
    # x = np.array(x)
    #
    # # test1Cp150_50
    # y = np.array(y)
    #
    # print(Neill2018_Data_UnifromAdju(x, y))
    #
    # Neill2018_Data_BlockAdju(x,y)

Neill2018_Data()
