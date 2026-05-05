import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
from PIL import Image

def add_axes_to_png():
    # Get arguments
    png_path = sys.argv[1]  # input PNG path
    pixel_size_mm = float(sys.argv[2])  # pixel size in mm
    output_path = sys.argv[3]  # output filename

    # Load PNG image and convert to grayscale
    img = Image.open(png_path).convert('L')  # Convert to grayscale
    img_array = np.array(img).astype(np.float32) / 255.0  # Normalize to [0, 1]

    # Setup LaTeX font
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Computer Modern'],
        'text.usetex': True,
        'font.size': 10
    })

    matplotlib.rc('pdf', fonttype=42)

    # Get image dimensions
    height, width = img_array.shape

    # Create coordinate arrays in mm
    x_extent = width * pixel_size_mm
    y_extent = height * pixel_size_mm

    # Calculate figure size to match aspect ratio (base width = 2.5 inches)
    base_width = 2.5
    fig_height = base_width * (y_extent / x_extent)

    # Create figure with correct aspect ratio
    fig, ax = plt.subplots(figsize=(base_width, fig_height))

    # Display image
    im = ax.imshow(img_array[::-1, :], extent=[0, x_extent, 0, y_extent],
                   origin='lower', cmap='viridis', vmin=0, vmax=1)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.3, pad=0.15)
    cbar.ax.tick_params(labelsize=8)

    ax.tick_params(top=True, right=True, labeltop=True, labelright=True)
    ax.tick_params(direction='in', labelsize=9, color='black')

    # Set labels
    ax.set_xlabel('DMD pixel in mm')

    # Set equal aspect ratio
    ax.set_aspect('equal', adjustable='box')

    # Adjust layout and save
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig(output_path, format='pdf', bbox_inches='tight', pad_inches=0.05, dpi=400)
    plt.close()

if __name__ == "__main__":
    add_axes_to_png()

