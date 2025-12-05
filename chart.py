# chart.py
# email: 24f1002320@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------------------------------------
# Generate synthetic marketing campaign data
# -----------------------------------------------------------

np.random.seed(42)
num_points = 200

# Features: marketing campaign spend and resulting conversion rate
spend = np.random.uniform(1000, 10000, num_points)  # marketing ad spend in $
conversion_rate = 1 + 0.002 * spend + np.random.normal(0, 3, num_points)  # synthetic business relationship

df = pd.DataFrame({
    "Marketing Spend ($)": spend,
    "Conversion Rate (%)": conversion_rate
})

# -----------------------------------------------------------
# Visualization settings (Seaborn best practices)
# -----------------------------------------------------------

sns.set_style("whitegrid")
sns.set_context("talk")

# 512 x 512 = 8 in x 8 in at 64 dpi
fig, ax = plt.subplots(figsize=(8, 8), dpi=64)

# -----------------------------------------------------------
# Scatterplot (use matplotlib scatter to ensure continuous cmap + colorbar)
# -----------------------------------------------------------

sc = ax.scatter(
    df["Marketing Spend ($)"],
    df["Conversion Rate (%)"],
    c=df["Conversion Rate (%)"],
    cmap="viridis",
    edgecolors="black",
    linewidths=0.5,
    s=60,
    alpha=0.9
)

# Add colorbar for the continuous hue
cbar = fig.colorbar(sc, ax=ax)
cbar.set_label("Conversion Rate (%)")

# -----------------------------------------------------------
# Labels and title
# -----------------------------------------------------------

ax.set_title("Marketing Spend vs Conversion Rate")
ax.set_xlabel("Marketing Spend ($)")
ax.set_ylabel("Conversion Rate (%)")

plt.tight_layout()

# -----------------------------------------------------------
# Save chart (exact 512x512 pixels)
# -----------------------------------------------------------

plt.savefig("chart.png", dpi=64, pad_inches=0)
plt.close()
print("Saved chart.png")
