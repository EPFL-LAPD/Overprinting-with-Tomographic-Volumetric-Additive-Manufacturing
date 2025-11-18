import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from pathlib import Path

# Set up matplotlib to use Computer Modern font
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Computer Modern Roman']
plt.rcParams['text.usetex'] = True

# Define alpha values and corresponding folders
alphas = [0.00, 0.02, 0.04, 0.06, 0.1, 0.3]
folders = [f"gear_{alpha:.2f}" for alpha in alphas]

# Pixel size in mm
pixel_size = 0.014
gamma = 0.2

# Load and normalize images
images = []
for folder in folders:
    img = np.load(f"{folder}/final.npy")[0, :, :, 0]  # Remove batch and channel dims
    img_normalized = img / np.max(img)  # Normalize to max intensity of 1
    img_gamma = np.power(img_normalized, gamma)  # Apply gamma correction
    images.append(img_gamma)

# Create 2x3 grid plot with increased vertical spacing
fig, axes = plt.subplots(2, 3, figsize=(13, 8))
axes = axes.flatten()

# Calculate extent in mm
height, width = images[0].shape
extent = [0, width * pixel_size, height * pixel_size, 0]

# Circle parameters
circle_diameter_pixels = 178.5
circle_radius_mm = (circle_diameter_pixels / 2) * pixel_size
center_x_mm = (width / 2) * pixel_size
center_y_mm = (height / 2) * pixel_size

for idx, (ax, img, alpha) in enumerate(zip(axes, images, alphas)):
    im = ax.imshow(img, cmap='viridis', vmin=0, vmax=1, extent=extent)
    ax.set_title(f"{chr(97+idx)}) $\\alpha = {alpha:.2f}$", fontsize=14)
    ax.set_xlabel('mm', fontsize=12)
    ax.set_ylabel('mm', fontsize=12)

    # Add gray circle
    circle = Circle((center_x_mm, center_y_mm), circle_radius_mm,
                    color='gray', fill=True, alpha=0.5, zorder=10)
    ax.add_patch(circle)

# Adjust spacing between rows
plt.subplots_adjust(right=0.92, hspace=0.35)

# Add single colorbar on the right
cbar_ax = fig.add_axes([0.94, 0.15, 0.02, 0.7])
cbar = fig.colorbar(im, cax=cbar_ax)
cbar.set_label('Gamma factor of $\\gamma=0.2$ applied to the intensity', fontsize=12)

plt.savefig('gear_comparison.pdf', format='pdf', bbox_inches='tight', dpi=300)
plt.close()

print("PDF saved as 'gear_comparison.pdf'")

