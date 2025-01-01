"""
File name: visualization.py
Author name: Troy Chin
Version: 1.1
Status: In development
Purpose: Handles all visualization modules to graphically solve the Schrodinger
Equation.
"""

import matplotlib.pyplot as plt
import numpy as np

class QuantumVisualizer:

    @staticmethod
    def plot_wavefunctions(x, wavefunctions, num_wavefunctions=5):
        """
        Plot the wavefunctions.

        Parameters:
            x (np.ndarray): Grid points.
            wavefunctions (np.ndarray): Normalized wavefunctions.
            num_wavefunctions (int): Number of wavefunctions to plot.
        """
        plt.figure(figsize=(10, 6))
        for i in range(num_wavefunctions):
            plt.plot(x, wavefunctions[:, i], label=f"psi_{i}(x)")
        plt.title("Wavefunctions")
        plt.xlabel("x")
        plt.ylabel("Psi")
        plt.legend()
        plt.grid()
        plt.show()

    @staticmethod
    def plot_energy_levels(eigenvalues, num_levels=5):
        """
        Plot the energy levels.

        Parameters:
            eigenvalues (np.ndarray): Array of eigenvalues (energy levels).
            num_levels (int): Number of energy levels to plot.
        """
        plt.figure(figsize=(10, 6))
        plt.hlines(eigenvalues[:num_levels], xmin=0, xmax=0.5, color='red', linestyles='dashed')
        plt.title("Energy Levels")
        plt.xlabel("")
        plt.ylabel("Energy levels (E)")
        plt.xticks([])
        plt.grid()
        plt.show()
