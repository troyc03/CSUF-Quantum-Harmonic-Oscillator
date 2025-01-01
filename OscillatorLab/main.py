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
    """
    Main entry point of the program. Initializes constants, solves the
    Schrodinger equation for a quantum harmonic oscillator, and visualizes results.
    """
    # Constants
    m = 1.0  # Mass of particle
    omega = 1.0  # Angular frequency
    hbar = 1.0  # Reduced Planck's constant
    x_min, x_max = -5.0, 5.0  # Range of x
    num_points = 1000  # Number of grid points

    # Step 1: Create a solver instance
    solver = QuantumSolver(x_min, x_max, num_points, m, omega, hbar)

    # Step 2: Construct the Hamiltonian
    solver.construct_hamiltonian()

    # Step 3: Solve for eigenvalues and eigenvectors
    eigenvalues, eigenvectors = solver.solve_hamiltonian()

    # Step 4: Normalize wavefunctions
    dx = solver.dx
    wavefunctions = QuantumUtils.normalize_wavefunctions(eigenvectors, dx)

    # Step 5: Visualize results
    QuantumVisualizer.plot_wavefunctions(solver.x, wavefunctions)
    QuantumVisualizer.plot_energy_levels(eigenvalues)

    # Step 6: Print key results
    print("Eigenvalues (Energy Levels):")
    print(eigenvalues[:5])  # Print the first 5 eigenvalues
    print("\nFirst Normalized Wavefunction (Psi_0):")
    print(wavefunctions[:, 0])  # Print the first wavefunction

if __name__ == "__main__":
    main()
