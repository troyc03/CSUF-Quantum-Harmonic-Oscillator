"""
File name: main.py
Author name: Troy Chin
Version: 1.2
Status: In development
Purpose: Main entry of program.
"""

from solver import QuantumSolver
from utils import QuantumUtils
from visualization import QuantumVisualizer

def main():
    # Constants
    m = 1.0  # Mass of particle
    omega = 1.0  # Angular frequency
    hbar = 1.0  # Reduced Planck's constant
    x_min, x_max = -5.0, 5.0
    num_points = 1000

    # Create solver instance
    solver = QuantumSolver(x_min, x_max, num_points, m, omega, hbar)

    # Construct Hamiltonian
    solver.construct_hamiltonian()

    # Solve Hamiltonian
    eigenvalues, eigenvectors = solver.solve_hamiltonian()
    dx = solver.dx

    # Normalize wavefunctions
    wavefunctions = QuantumUtils.normalize_wavefunctions(eigenvectors, dx)

    #Plot results
    QuantumVisualizer.plot_wavefunctions(solver.x, wavefunctions)
    QuantumVisualizer.plot_energy_levels(eigenvalues)

    # Print results
    print(f"Eigenvalues: {eigenvalues}")
    print(f"First normalized wavefunction: {wavefunctions[:, 0]}")


if __name__ == "__main__":
    main()
