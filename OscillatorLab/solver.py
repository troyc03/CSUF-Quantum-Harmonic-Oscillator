"""
File name: solver.py
Author name: Troy Chin
Version: 1.0
Status: In development
Purpose: This program solves the Schrodinger Equation and constructs the
Hamiltonian matrix numerically.
"""

import numpy as np
from scipy.linalg import eigh

class QuantumSolver:

    def __init__(self, x_min, x_max, m, num_points, omega, h_bar):
        self.x_min = x_min
        self.x_max = x_max
        self.m = m
        self.num_points = num_points
        self.omega = omega
        self.h_bar = h_bar
        self.x = None
        self.dx = None
        self.H = None

    def construct_hamiltonian(self):
        self.x = np.linspace(self.x_max, self.x_min, self.num_points)
        self.dx = self.x[1] - self.x[0]
        V = 0.5 * self.m * self.omega**2 * self.x**2
        T = self.h_bar**2/(2*self.m*self.dx**2)
        H = np.zeros((self.num_points, self.num_points))

        for i in range(self.num_points):
            H[i,i] = 2 * abs(T) + V[i]

            if i > 0:
                H[i,i-1] = T
            elif i < self.num_points - 1:
                H[i,i+1] = T

        self.H = H

    def solve_hamiltonian(self):
        if self.H is None:
            raise ValueError("ERROR: Hamiltonian matrix is not constructed.")
        eigenvalues, eigenvectors = eigh(self.H)
        return eigenvalues, eigenvectors



