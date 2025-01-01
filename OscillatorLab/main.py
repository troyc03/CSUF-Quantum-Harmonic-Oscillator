"""
File name: main.py
Author name: Troy Chin
Version: 1.0
Status: In development
Purpose: Main entry of the lab.
"""

from solver import QuantumSolver

def main():
    m = 1.0
    omega = 1.0
    h_bar = 1.054e-34
    x_min, x_max = -5.0, 5.0
    num_points = 1000

    solver = QuantumSolver(x_min, x_max, m, num_points, omega, h_bar)
    sol = solver.construct_hamiltonian()

    eigenvalues, eigenvectors = solver.solve_hamiltonian()
    return eigenvalues, eigenvectors, sol

if __name__ == '__main__':
    main()
