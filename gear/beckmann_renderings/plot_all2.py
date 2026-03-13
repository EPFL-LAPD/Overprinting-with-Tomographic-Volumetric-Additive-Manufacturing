import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import os

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})

folders = ["0.01", "0.02", "0.03", "0.04", "0.06", "0.1"]
gamma = 0.5

pixel_size_mm = 0.014
img_size_px   = 500
extent_mm     = [0, img_size_px * pixel_size_mm,
                 0, img_size_px * pixel_size_mm]

data = []
for folder in folders:
    arr = np.load(os.path.join(folder, "final.npy"))
    arr = arr / np.max(arr)
    data.append(arr[0, :, :, 0])

vmin = min(d.min() for d in data)
vmax = max(d.max() for d in data)

fig, axes = plt.subplots(2, 3, figsize=(9, 7))
axes = axes.flatten()

norm = mcolors.PowerNorm(gamma=gamma, vmin=vmin, vmax=vmax)

rod_radius_mm = 2.0
cx_mm = img_size_px * pixel_size_mm / 2
cy_mm = img_size_px * pixel_size_mm / 2

ims = []
for i, (ax, folder, d) in enumerate(zip(axes, folders, data)):
    im = ax.imshow(d, norm=norm, cmap="viridis", origin="lower", extent=extent_mm)
    ax.set_title(rf"$\alpha$ = {folder}", fontsize=13)

    if i >= 3:
        ax.set_xlabel(r"$x$ (mm)", fontsize=10)
    if i % 3 == 0:
        ax.set_ylabel(r"$y$ (mm)", fontsize=10)

    ax.tick_params(labelsize=8)
    ims.append(im)

    circle = mpatches.Circle(
        (cx_mm, cy_mm), radius=rod_radius_mm,
        facecolor="gray", edgecolor="none",
        zorder=5,
    )
    ax.add_patch(circle)

    ax.text(
        cx_mm, cy_mm, r"\textbf{rod}",
        color="black", fontsize=20,
        ha="center", va="center", zorder=6,
    )

fig.subplots_adjust(right=0.88, hspace=0.35, wspace=0.25)
cbar_ax = fig.add_axes([0.91, 0.1, 0.025, 0.8])
cbar = fig.colorbar(ims[0], cax=cbar_ax)
cbar.set_label(rf"Value ($\gamma$ = {gamma})", fontsize=12)

plt.savefig("final_grid.pdf", dpi=350, bbox_inches="tight")

