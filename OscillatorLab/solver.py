import numpy as np
from scipy.linalg import eigh

class QuantumSolver():

    def __init__(self, x_min, x_max, num_points, m, omega, h_bar):
        self.x_min = x_min
        self.x_max = x_max
        self.num_points = num_points
        self.m = m
        self.omega = omega
        self.h_bar = h_bar
        self.H = None
        self.x = None
        self.dx = None

    def construct_hamiltonian(self, x_min, x_max, num_points, m, omega, dx, h_bar):
        x = np.linspace(x_min, x_max, num_points)
        dx =  x[1] - x[0]
        V = 1/2 * m * omega**2 * x**2
        T = -h_bar**2 / (2 * m * dx**2)
        H = np.zeros((num_points, num_points))

        for i in range(num_points):
            H[i,i] = 2 * abs(T) + V[i]

            if i > 0:
                H[i,i-1] = T
            elif i < num_points - 1:
                H[i,i+1] = T

        return H, x, dx

    def solve_hamiltonian(self, H):
        eigenvalues, eigenvectors = eigh(H)
        return eigenvalues, eigenvectors





