import numpy as np
import matplotlib.pyplot as plt
import sys

def save_histogram():
    # Get paths from command line arguments
    vol_path = sys.argv[1]  # final.npy path
    target_path = sys.argv[2]  # target.npy path
    filename = sys.argv[3]  # output filename

    # Load data
    vol = np.load(vol_path)
    target = np.load(target_path)

    # Setup LaTeX font
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Computer Modern'],
        'text.usetex': True,
        'font.size': 14
    })

    # Create very compact figure
    fig, ax = plt.subplots(figsize=(2.5, 1.9))

    obj_mask = target.flatten() > 0
    voxels_final = vol.flatten()


    import matplotlib
    # Get viridis colormap min and max colors
    viridis = matplotlib.colormaps['viridis']
    color_min = viridis(1.0)  # Minimum value color (dark purple)
    color_max = viridis(0.8)  # Maximum value color (bright yellow)

    # Plot histograms
    bins = np.linspace(0, 1.3, 100)
    ax.hist(voxels_final[obj_mask], bins=bins, label="object voxels", alpha=0.7, color=color_min, edgecolor="black", linewidth=0.2)
    ax.hist(voxels_final[~obj_mask], bins=bins, label="void voxels", alpha=0.6, color=color_max, edgecolor="black", linewidth=0.2)

    # Minimal formatting
    ax.set_xlim([0, 1.3])
    ax.set_yscale('log')
    ax.set_ylabel("voxel count")
    ax.set_xlabel("simulated dose")
    ax.legend(frameon=False, loc='upper left', fontsize=9)

    # Remove spines and minimize margins
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(labelsize=9)

    plt.tight_layout(pad=0.2)
    plt.savefig(filename, format='pdf', bbox_inches='tight', pad_inches=0.05, dpi=100)
    plt.close()

if __name__ == "__main__":
    save_histogram()

