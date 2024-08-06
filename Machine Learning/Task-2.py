import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv('./Iris Species/Iris.csv')
columns_to_plot = [col for col in df.columns if col not in ['Species', 'Id']]

# Determine grid size
num_plots = len(columns_to_plot)
num_rows = int(np.ceil(num_plots / 2))  # Adjust for 2 plots per row

# Create subplots
fig, axes = plt.subplots(num_rows, 2, figsize=(12, 5 * num_rows))
axes = axes.flatten()

# Plot each histogram with KDE
for i, col in enumerate(columns_to_plot):
    sns.histplot(df[col], kde=True, ax=axes[i], bins=20, color='skyblue', edgecolor='black')
    axes[i].set_title(f'{col} (mean={df[col].mean():.2f}, std={df[col].std():.2f})')

# Remove any unused subplots
for i in range(num_plots, len(axes)):
    fig.delaxes(axes[i])

plt.tight_layout()
plt.show()
