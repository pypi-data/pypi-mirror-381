# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 13:50:19 2025

@author: TODL
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


def model(parameters, xdata):
    """Compute the curve fitting model y = f(x, params)"""
    a, b = parameters
    return a + b * xdata


def loss(ypred, ydata):
    """Compute the data fit loss."""
    return np.sum(np.abs(ypred - ydata) ** 2)


def optimization_func(parameters, xdata, ydata):
    """Function passed to `minimize`."""
    ypred = model(parameters, xdata)  # Predict
    loss_value = loss(ypred, ydata)  # Score
    return loss_value


# Some dummy data
xdata = np.array([1, 2, 3, 4, 5])
ydata = np.array([1.1, 1.9, 2.9, 4.1, 3])

# Optimize the function
opt_results = sp.optimize.minimize(
    fun=optimization_func, x0=[0, 0], args=(xdata, ydata), method="Nelder-Mead"
)
print(opt_results)

# Plot results
plt.scatter(xdata, ydata)
x_plot = np.linspace(0, 7)
y_plot = model(opt_results.x, x_plot)
plt.plot(x_plot, y_plot)
plt.show()
