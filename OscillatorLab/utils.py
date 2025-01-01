"""
File name: utils.py
Author name: Troy Chin
Version: 1.0
Status: In development
Purpose: Stores all utilities that will be used to perform this lab.
"""

import numpy as np

class QuantumUtils:

    @staticmethod
    def normalize_wavefunctions(eigenvectors, dx):
        """
        Normalize wavefunctions so that their integral over space equals 1.

        Parameters:
            eigenvectors (np.ndarray): Wavefunctions to normalize (each column is a wavefunction).
            dx (float): Spacing between grid points.

        Returns:
            np.ndarray: Normalized wavefunctions.
        """
        normalization_factors = np.sqrt(np.sum(eigenvectors**2, axis=0) * dx)
        return eigenvectors / normalization_factors
