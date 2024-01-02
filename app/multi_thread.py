import concurrent.futures

import matplotlib.pyplot as plt
import numpy as np


def multi_thread():
    width = height = 1024
    x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5
    max_iter = 50

    xs = np.linspace(x_min, x_max, width)
    ys = np.linspace(y_min, y_max, height)
    zs = np.empty((len(xs), len(ys)))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i, x in enumerate(xs):
            for j, y in enumerate(ys):
                executor.submit(calculate_z_pixel, i, j, x, y, zs, max_iter)
    plt.imshow(zs.T, cmap="bone", extent=(x_min, x_max, y_min, y_max))
    plt.savefig("mandelbrot-multi_thread.png")


def calculate_z_pixel(i, j, x, y, zs, max_iter):
    z = x + y * 1j
    for n in range(max_iter):
        if abs(z) > 2:
            zs[i, j] = n
            break
        z = z * z + x + y * 1j
    else:
        zs[i, j] = max_iter
