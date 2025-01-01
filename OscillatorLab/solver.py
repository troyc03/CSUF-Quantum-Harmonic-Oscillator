"""
File name: solver.py
Author name: Troy Chin
Version: 1.1
Status: In development
Purpose: Solves the Hamiltonian matrix and the Schrodinger equation to compute the
eigenstates of a quantum harmonic system.
"""

import numpy as np
from scipy.linalg import eigh

class QuantumSolver:
    def __init__(self, x_min, x_max, num_points, m, omega, hbar):
        """
        Initialize the quantum solver with system parameters.

        Parameters:
            x_min (float): Minimum x-value in the grid.
            x_max (float): Maximum x-value in the grid.
            num_points (int): Number of grid points.
            m (float): Mass of the particle.
            omega (float): Angular frequency.
            hbar (float): Reduced Planck's constant.
        """
        self.x_min = x_min
        self.x_max = x_max
        self.num_points = num_points
        self.m = m
        self.omega = omega
        self.hbar = hbar
        self.H = None
        self.x = None
        self.dx = None

    def construct_hamiltonian(self):
        """
        Construct the Hamiltonian matrix.
        """
        self.x = np.linspace(self.x_min, self.x_max, self.num_points)
        self.dx = self.x[1] - self.x[0]

        # Potential energy term
        V = 0.5 * self.m * self.omega**2 * self.x**2

        # Kinetic energy coefficient
        kinetic_coeff = -self.hbar**2 / (2 * self.m * self.dx**2)

        # Initialize Hamiltonian matrix
        H = np.zeros((self.num_points, self.num_points))

        # Fill Hamiltonian matrix
        for i in range(self.num_points):
            # Diagonal elements
            H[i, i] = 2 * abs(kinetic_coeff) + V[i]

            # Off-diagonal elements
            if i > 0:
                H[i, i - 1] = kinetic_coeff
            if i < self.num_points - 1:
                H[i, i + 1] = kinetic_coeff

        self.H = H

    def solve_hamiltonian(self):
        """
        Solve the eigenvalue problem for the Hamiltonian matrix.

        Returns:
            tuple: (eigenvalues, eigenvectors)
        """
        if self.H is None:
            raise ValueError("Hamiltonian matrix is not constructed.")
        eigenvalues, eigenvectors = eigh(self.H)
        return eigenvalues, eigenvectors
