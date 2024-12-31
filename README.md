# Quantum Harmonic Oscillator Lab

## Table of Contents
- [Project Description](#project-description)
- [Tools and Technologies](#tools-and-technologies)
- [Key Concepts](#key-concepts)
- [Installation](#installation)
- [Diagrams](#diagrams)
- [Known Issues](#known-issues)
- [To-Do Items](#to-do-items)

## Project Description
This lab delves into the quantum harmonic oscillator, a foundational concept in quantum mechanics. Using both Python and MATLAB, the lab explores numerical solutions to the Schrödinger equation, energy eigenvalues, and wavefunctions. By leveraging numerical methods and visualizations, we aim to provide a clear understanding of the system's quantum behavior.

## Tools and Technologies

- **Python**: Primary language for numerical computation and visualization.
- **MATLAB**: Utilized for symbolic computation and alternative visualizations.
- **Anaconda**: Environment for Python package management.
- **Spyder**: IDE for Python, supporting scientific computation.

## Key Concepts

- **Quantum Mechanics**: Study of physical phenomena at microscopic scales, focusing on wavefunctions and probabilities.
- **Schrödinger Equation**: Fundamental equation describing quantum systems.
- **Numerical Analysis**: Techniques like finite difference methods to approximate solutions to the Schrödinger equation.
- **Eigenvalue Problems**: Determining energy levels of the quantum harmonic oscillator.

## Installation

1. **Install Anaconda**: Download and install [Anaconda](https://www.anaconda.com/products/distribution).
2. **Install MATLAB**: Obtain [MATLAB](https://www.mathworks.com/products/matlab.html) for symbolic computations.
3. **Install Required Libraries**:
   - Using Conda:
     ```bash
     conda install numpy scipy matplotlib
     ```
   - Using pip:
     ```bash
     pip install numpy scipy matplotlib
     ```
4. **Launch Spyder**:
   ```bash
   spyder
   ```

## Diagrams

### UML Class Diagram
```bash
+----------------------------+
| QuantumHarmonicOscillator |
+----------------------------+
| - mass: float             |
| - frequency: float        |
| - potential: callable     |
| - grid_points: int        |
+----------------------------+
| + __init__()              |
| + solve_schrodinger()     |
| + calculate_wavefunction()|
| + calculate_energy_levels()|
+----------------------------+
```

### UML Sequence Diagram
```bash
User              System                NumericalMethods
 |                   |                           |
 |--- Define Parameters ->                    |
 |                   |--- solve_schrodinger()  |
 |                   |--- calculate_energy_levels()|
 |                   |<-- Eigenvalues, Wavefunctions|
 |--- Visualize ->                              |
 |                   |--- plot_wavefunctions() |
 |                   |<-- Display Graph       |
```

## Known Issues

- **Boundary Condition Sensitivity**: Numerical solutions depend on carefully chosen grid boundaries.
- **MATLAB Integration**: Compatibility issues might arise when transferring data between Python and MATLAB.

## To-Do Items

- Add unit tests for numerical methods.
- Improve visualization for higher energy states.
- Explore advanced numerical solvers for enhanced accuracy.

## Credits

Troy Chin (Lab Developer and Documentation Lead)

## License

This project is licensed under the GNU General Public License v3.0. For more details, visit [GNU License](https://www.gnu.org/licenses/gpl-3.0.en.html).
