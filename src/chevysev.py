import numpy as np
import matplotlib.pyplot as plt

def chebyshev_grid(n, a=-1, b=None):
    """
    Generate Chebyshev grid points.
    :param n: Number of points - 1 (degree of the polynomial)
    :param a: Lower bound of the interval (default is -1)
    :param b: Upper bound of the interval (default is max(a, 1))
    :return: Array of Chebyshev grid points
    """
    if b is None:
        b = max(a, 1)
    width_over_two = (b - a) / 2

    return np.array([
        width_over_two * (np.cos(i * np.pi / n) + 1) + a
        for i in range(n, -1, -1)
    ])

def barycentric_interpolation_in_chebyshev_points_at_a_point(f_list, x, chebyshev_grid_points=None):
    """
    Perform barycentric interpolation using Chebyshev points at a given point x.
    :param f_list: List of function values at Chebyshev grid points
    :param x: Point to evaluate the interpolation at
    :param chebyshev_grid_points: Optional precomputed Chebyshev grid points
    :return: Interpolated value at x
    """
    n = len(f_list)
    chebyshev_grid = chebyshev_grid_points if chebyshev_grid_points is not None else chebyshev_grid(n - 1)

    x_diff_list = np.zeros(n)
    for i, v in enumerate(chebyshev_grid):
        diff = x - v
        if diff == 0:
            return f_list[i]
        x_diff_list[i] = (-1) ** i / diff

    val_first = 0.5 * x_diff_list[0]
    numerator = f_list[0] * val_first
    denominator = val_first

    for i in range(1, n - 1):
        val = x_diff_list[i]
        numerator += f_list[i] * val
        denominator += val

    val_last = 0.5 * x_diff_list[-1]
    numerator += f_list[-1] * val_last
    denominator += val_last

    return numerator / denominator

# Example usage
if __name__ == "__main__":
    # Define the function to interpolate
    f = lambda x: np.sin(x)

    # Generate Chebyshev grid points and function values
    n =50
    a, b = -10, 10
    chebyshev_points = chebyshev_grid(n, a, b)
    f_values = f(chebyshev_points)

    # Define x values for plotting
    x_vals = np.linspace(a, b, 500)
    interpolated_vals = [barycentric_interpolation_in_chebyshev_points_at_a_point(f_values, x, chebyshev_points) for x in x_vals]

    # Plot the original function and interpolated values
    plt.figure(figsize=(10, 6))

    plt.plot(x_vals, f(x_vals), label="Original Function", linewidth=2)
    plt.plot(x_vals, interpolated_vals, label="Interpolation", linestyle="--")
    plt.scatter(chebyshev_points, f_values, color="red", label="Chebyshev Points")


    plt.title("Barycentric Interpolation in Chebyshev Points")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()
