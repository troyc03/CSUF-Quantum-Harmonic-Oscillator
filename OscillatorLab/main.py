from solver import QuantumSolver


def main():
    # Constants
    m = 1.0  # Mass of particle
    omega = 1.0  # Angular frequency
    h_bar = 1.0  # Reduced Planck's constant
    x_min, x_max = -5.0, 5.0
    num_points = 1000

    solver = QuantumSolver(x_min, x_max, num_points, m, omega, h_bar)

    result = solver.construct_hamiltonian(x_min, x_max, num_points, m, omega, h_bar)

    pass

if __name__ == "__main__":
    main()
