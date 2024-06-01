#!/usr/bin/env python3
"""
 Update the weights and biases of a neural network
 using gradient descent with L2 regularization
"""


import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
    Updates the weights and biases of a neural network
    using gradient descent with L2 regularization
    """
    m = Y.shape[1]
    dz = cache["A" + str(L)] - Y
    for i in range(L, 0, -1):
        A_prev = cache["A" + str(i - 1)]
        W = weights["W" + str(i)]
        b = weights["b" + str(i)]

        dw = (1 / m) * np.matmul(dz, A_prev.T) + (lambtha / m) * W
        db = (1 / m) * np.sum(dz, axis=1, keepdims=True)

        if i > 1:  # For hidden layers, apply tanh derivative
            dz = np.matmul(W.T, dz) * (1 - A_prev ** 2)

        # Update weights and biases
        weights["W" + str(i)] -= alpha * dw
        weights["b" + str(i)] -= alpha * db
