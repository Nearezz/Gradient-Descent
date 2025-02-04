import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load data
data = np.loadtxt("Data.csv", delimiter=",", dtype="float")  # Use float instead of str

# Extract columns
timeToExpiration = data[:, 0]  # X-axis
strikePrice = data[:, 1]       # Y-axis
IV = data[:, 2]                # Z-axis (Implied Volatility)

# Create a proper 2D meshgrid
X, Y = np.meshgrid(np.unique(timeToExpiration), np.unique(strikePrice))



# Reshape IV (Z-values) to match the (X, Y) grid shape
Z = IV.reshape(X.shape)  # ✅ Now it should work

# Create figure
fig = plt.figure()
ax = plt.axes(projection='3d')

# Plot surface
ax.plot_surface(X, Y, Z, cmap="viridis")

# Labels
ax.set_xlabel("Time to Expiration")
ax.set_ylabel("Strike Price")
ax.set_zlabel("Implied Volatility")
plt.title("IV Surface Plot")

plt.show()

