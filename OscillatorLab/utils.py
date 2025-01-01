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
        return eigenvectors / (np.sum(eigenvectors**2, axis=0) * dx)