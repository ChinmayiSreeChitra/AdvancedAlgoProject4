import numpy as np
import matplotlib.pyplot as plt
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def matrix_plot(matrix, title="Matrix", ax=None):
    """
    Plot the matrix using matplotlib
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))
    ax.clear()  # Clear the content of the axis
    cax = ax.matshow(matrix, cmap="viridis")

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, str(round(matrix[i, j], 2)), va='center', ha='center', color='white', fontsize=12, fontweight='bold')

    ax.set_title(title)


def pivot(N, B, A, b, c, v, l, e):
    m, n = A.shape
    A_hat = np.zeros((m, n))
    b_hat = np.zeros(m)

    fig, ax = plt.subplots(figsize=(6, 6))
    matrix_plot(np.zeros((m, n)), "Initializing A_hat and b_hat to zeros", ax)
    plt.pause(2)

    b_hat[l] = b[l] / A[l, e]
    matrix_plot(np.diag(b_hat), f"Computing b_hat[{l}] = {b[l]} / {A[l, e]} = {b_hat[l]}", ax)
    plt.pause(2)

    for j in range(n):
        if j != e:
            A_hat[l, j] = A[l, j] / A[l, e]
            matrix_plot(A_hat, f"Computing A_hat[{l}, {j}] = {A[l, j]} / {A[l, e]} = {A_hat[l, j]}", ax)
            plt.pause(2)
    A_hat[l, e] = 1 / A[l, e]
    matrix_plot(A_hat, f"Computing A_hat[{l}, {e}] = 1 / {A[l, e]} = {A_hat[l, e]}", ax)
    plt.pause(2)

    for i in range(m):
        if i != l:
            b_hat[i] = b[i] - A[i, e] * b_hat[l]
            matrix_plot(np.diag(b_hat), f"Computing b_hat[{i}] = {b[i]} - {A[i, e]} * {b_hat[l]} = {b_hat[i]}", ax)
            plt.pause(2)
            for j in range(n):
                if j != e:
                    A_hat[i, j] = A[i, j] - A[i, e] * A_hat[l, j]
                    matrix_plot(A_hat, f"Computing A_hat[{i}, {j}] = {A[i, j]} - {A[i, e]} * {A_hat[l, j]} = {A_hat[i, j]}", ax)
                    plt.pause(2)
            A_hat[i, e] = -A[i, e] * A_hat[l, e]
            matrix_plot(A_hat, f"Computing A_hat[{i}, {e}] = -{A[i, e]} * {A_hat[l, e]} = {A_hat[i, e]}", ax)
            plt.pause(2)

    v_hat = v + c[e] * b_hat[l]
    matrix_plot(np.array([[v_hat]]), f"Computing v_hat = {v} + {c[e]} * {b_hat[l]} = {v_hat}", ax)
    plt.pause(2)
    c_hat = np.copy(c)

    for j in range(n):
        if j != e:
            c_hat[j] = c[j] - c[e] * A_hat[l, j]
            matrix_plot(np.reshape(c_hat, (1, -1)), f"Computing c_hat[{j}] = {c[j]} - {c[e]} * {A_hat[l, j]} = {c_hat[j]}", ax)
            plt.pause(2)
    c_hat[e] = -c[e] * A_hat[l, e]
    matrix_plot(np.reshape(c_hat, (1, -1)), f"Computing c_hat[{e}] = -{c[e]} * {A_hat[l, e]} = {c_hat[e]}", ax)
    plt.pause(2)

    return A_hat, b_hat, c_hat, v_hat


# Sample input data for the example
A = np.array([
    [2, 1],
    [1, 3]
])
b = np.array([8, 6])
c = np.array([5, 4])
v = 0
l = 0  # Index for the pivot row
e = 0  # Index for the pivot column

A_hat, b_hat, c_hat, v_hat = pivot(set(), set(), A, b, c, v, l, e)
