import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# =========================================================
# Data
# =========================================================

methods = ["HNSW", "IVF", "IVFPQ", "Flat"]

latency = np.array([
    0.120,
    0.349,
    0.730,
    0.731
])

precision = np.array([
    0.9170,
    0.9193,
    0.9150,
    0.9198
])

# =========================================================
# Figure style
# =========================================================

plt.rcParams.update({
    "font.family": "Times New Roman",
    "font.size": 12,
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12
})

fig, ax = plt.subplots(figsize=(8, 6))

colors = [
    "#4C8EDA",  # HNSW
    "#39A852",  # IVF
    "#F28E2B",  # IVFPQ
    "#CC4938"   # Flat
]

markers = ["o", "s", "^", "D"]

# =========================================================
# Scatter points
# =========================================================

for i, method in enumerate(methods):
    ax.scatter(
        latency[i],
        precision[i],
        s=170,
        color=colors[i],
        marker=markers[i],
        edgecolor="black",
        linewidth=0.9,
        zorder=5
    )

# =========================================================
# Method labels directly above markers
# =========================================================

label_offsets = {
    "HNSW": (0, 12),
    "IVF": (0, 12),
    "IVFPQ": (0, -30),  # placed below because of upper boundary/overlap
    "Flat": (0, 14)
}

for x, y, method in zip(latency, precision, methods):

    dx, dy = label_offsets[method]

    ax.annotate(
        method,
        xy=(x, y),
        xytext=(dx, dy),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontsize=12,
        zorder=6
    )

# =========================================================
# Pareto frontier
# =========================================================

pareto_x = np.array([0.120, 0.349, 0.731])
pareto_y = np.array([0.9170, 0.9193, 0.9198])

ax.plot(
    pareto_x,
    pareto_y,
    color="black",
    linewidth=1.7,
    zorder=3
)

# Label connected directly to Pareto line
# ax.annotate(
#     "Pareto frontier",
#     xy=(0.56, 0.91960),       # point on the IVF--Flat frontier segment
#     xytext=(0.56, 0.92005),   # label directly above the line
#     fontsize=11,
#     ha="center",
#     va="bottom",
#     arrowprops=dict(
#         arrowstyle="-",
#         color="black",
#         linewidth=0.9,
#         shrinkA=2,
#         shrinkB=2
#     ),
#     zorder=6
# )

# =========================================================
# Preferred region as a cloud-like highlighted area
# =========================================================

cloud_color = "#B9DDF4"

cloud_parts = [
    (0.105, 0.92055, 0.075, 0.00042),
    (0.145, 0.92062, 0.090, 0.00050),
    (0.190, 0.92056, 0.085, 0.00043),
    (0.135, 0.92038, 0.130, 0.00045)
]

for cx, cy, width, height in cloud_parts:
    cloud = Ellipse(
        (cx, cy),
        width=width,
        height=height,
        facecolor=cloud_color,
        edgecolor="none",
        alpha=0.48,
        zorder=1
    )
    ax.add_patch(cloud)

# Short arrow located close to the highlighted region
ax.annotate(
    "Preferred\nregion",
    xy=(0.165, 0.92052),
    xytext=(0.255, 0.92052),
    fontsize=11,
    ha="center",
    va="center",
    arrowprops=dict(
        arrowstyle="->",
        color="black",
        linewidth=1.2,
        shrinkA=3,
        shrinkB=3
    ),
    zorder=4
)

# =========================================================
# Axes and grid
# =========================================================

ax.set_xlabel("Average Query Latency (ms)")
ax.set_ylabel("Average Precision@1")

ax.set_xlim(0.05, 0.80)
ax.set_ylim(0.914, 0.921)

ax.set_xticks(np.arange(0.1, 0.81, 0.1))
ax.set_yticks(np.arange(0.914, 0.9211, 0.001))

ax.grid(
    linestyle="--",
    linewidth=0.8,
    alpha=0.32,
    zorder=0
)

for spine in ax.spines.values():
    spine.set_linewidth(1.0)

plt.tight_layout()

# =========================================================
# Export
# =========================================================

plt.savefig(
    "effectiveness_efficiency_tradeoff.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "effectiveness_efficiency_tradeoff.pdf",
    bbox_inches="tight"
)

plt.savefig(
    "effectiveness_efficiency_tradeoff.svg",
    bbox_inches="tight"
)

plt.show()