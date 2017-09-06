import numpy as np
import random

height_array = 2
width_array = 200
rand_thres = .05
very_rand_thres = .3

X = np.ndarray([height_array, width_array])
y = np.ndarray([height_array, width_array])
y_rand = np.ndarray([height_array, width_array])
y_very_rand = np.ndarray([height_array, width_array])

for i in range(height_array):
    for j in range(width_array):
        rand = random.random()
        rand_2 = random.random()
        if rand < .25:
            X[i, j] = 1
            y[i, j] = 0
            y_rand[i, j] = 0
            y_very_rand[i, j] = 0
            if rand_2 < very_rand_thres:
                y_very_rand[i, j] = 1
                if rand_2 < rand_thres:
                    y_rand[i, j] = 1
        else:
            X[i, j] = 0
            y[i, j] = 1
            y_rand[i, j] = 1
            y_very_rand[i, j] = 1
            if rand_2 < very_rand_thres:
                y_very_rand[i, j] = 0
                if rand_2 < rand_thres:
                    y_rand[i, j] = 0