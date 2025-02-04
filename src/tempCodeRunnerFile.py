plt.plot(x_vals, interpolated_vals, label="Interpolation", linestyle="--")
    plt.scatter(chebyshev_points, f_values, color="red", label="Chebyshev Points")
