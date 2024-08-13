import matplotlib.pyplot as plt
import numpy as np

# Sample data array
data = np.array([12, 10, 11, 14, 76, 103, 13,15,12,16,17,11,16,25, 110, 20, 23, 27,19, 18,10,13,78, 15,14,20,28,32,87, 23,25,19,22,28,17,27,80,15, 18, 22, 20,25,82,27,21,12,15,18,90,108,28,150])

# Create a boxplot
plt.boxplot(data)

# Display the plot
plt.show()

# Get boxplot statistics
boxplot_stats = plt.boxplot(data, patch_artist=True)

# Extract outliers from the plot
outliers = boxplot_stats['fliers'][0].get_ydata()

print(f"Outliers: {outliers}")
