"""
File name: test.py
Author name: Troy Chin
Version: 1.2
Status: In development
Purpose: Runs all integration or unit tests to test core functionality of the program.
"""

import unittest
import numpy as np
from solver import QuantumSolver
from utils import QuantumUtils

class TestQuantumSolver(unittest.TestCase):

    def setUp(self):
        """
        Set up all common variables for the tests.
        """
        self.x_min = -5.0
        self.x_max = 5.0
        self.num_points = 1000
        self.m = 1.0
        self.omega = 1.0
        self.hbar = 1.054e-34
        self.solver = QuantumSolver(self.x_min, self.x_max, self.num_points, self.m, self.omega, self.hbar)
        self.solver.construct_hamiltonian()

    def test_hamiltonian_shape(self):
        """
        Test if the Hamiltonian has the correct shape.
        """
        H = self.solver.H
        self.assertEqual(H.shape, (self.num_points, self.num_points))

    def test_hamiltonian_symmetry(self):
        """
        Test if the Hamiltonian matrix is symmetric.
        """
        H = self.solver.H
        self.assertTrue(np.allclose(H, H.T), "Hamiltonian is not symmetric.")

    def test_wavefunction_normalization(self):
        """
        Test if the wavefunctions are normalized.
        """
        _, eigenvectors = self.solver.solve_hamiltonian()
        normalized = QuantumUtils.normalize_wavefunctions(eigenvectors, self.solver.dx)
        norms = np.sum(normalized**2, axis=0) * self.solver.dx
        self.assertTrue(np.allclose(norms, 1.0), "Wavefunctions are not normalized.")

if __name__ == "__main__":
    unittest.main()
