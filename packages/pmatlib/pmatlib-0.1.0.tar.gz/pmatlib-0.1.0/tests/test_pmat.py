import numpy as np
import matplotlib.pyplot as plt
from pmatlib import pmat


def test_pmat_directions():
    # 1D sinusoid with an artificial peak
    t = np.linspace(0, 4 * np.pi, 200)
    sig = np.sin(t)
    sig[100] += 2.5  # add a peak in the middle

    max_window = 20

    # Compute PMAT for all directions
    M_left = pmat(sig, max_window=max_window, direction="Left")
    M_right = pmat(sig, max_window=max_window, direction="Right")
    M_center = pmat(sig, max_window=max_window, direction="Center")

    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Original signal
    axes[0, 0].plot(t, sig, label="Signal with peak")
    axes[0, 0].set_title("Original 1D Signal")
    axes[0, 0].set_xlabel("Time")
    axes[0, 0].set_ylabel("Amplitude")
    axes[0, 0].legend()
    axes[0, 0].grid(True)

    # PMAT Left
    im1 = axes[0, 1].imshow(
        M_left,
        aspect="auto",
        cmap="viridis",
        origin="lower",
        extent=[0, len(sig), 1, max_window],
    )
    axes[0, 1].set_title("PMAT Heatmap (Left Padding)")
    axes[0, 1].set_xlabel("Time index")
    axes[0, 1].set_ylabel("Window size")
    fig.colorbar(im1, ax=axes[0, 1])

    # PMAT Right
    im2 = axes[1, 0].imshow(
        M_right,
        aspect="auto",
        cmap="viridis",
        origin="lower",
        extent=[0, len(sig), 1, max_window],
    )
    axes[1, 0].set_title("PMAT Heatmap (Right Padding)")
    axes[1, 0].set_xlabel("Time index")
    axes[1, 0].set_ylabel("Window size")
    fig.colorbar(im2, ax=axes[1, 0])

    # PMAT Center
    im3 = axes[1, 1].imshow(
        M_center,
        aspect="auto",
        cmap="viridis",
        origin="lower",
        extent=[0, len(sig), 1, max_window],
    )
    axes[1, 1].set_title("PMAT Heatmap (Center Padding)")
    axes[1, 1].set_xlabel("Time index")
    axes[1, 1].set_ylabel("Window size")
    fig.colorbar(im3, ax=axes[1, 1])

    # Adjust layout
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    test_pmat_directions()