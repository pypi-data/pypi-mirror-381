import numpy as np


def _moving_average(sig, window: int) -> np.ndarray:
    """Internal moving average function (not public)."""
    weights = np.repeat(1.0, window) / window
    return np.convolve(sig, weights, 'valid')


def pmat(sig, max_window: int, direction: str = 'Left') -> np.ndarray:
    """
    Progressive Moving Average Transform (PMAT).

    Parameters
    ----------
    sig : array-like
        Input 1D signal.
    max_window : int
        Maximum moving average window size (must be <= length of signal).
    direction : str, optional
        'Left', 'Right', or 'Center' (default 'Left').

    Returns
    -------
    M : ndarray
        Matrix of moving averages for windows from 1 to max_window.

    Raises
    ------
    ValueError
        If max_window > length of signal.
        If direction is invalid.
    """
    sig = np.asarray(sig)
    N = len(sig)

    if max_window > N:
        raise ValueError(f"max_window ({max_window}) must be <= length of signal ({N}).")

    if direction not in ("Left", "Right", "Center"):
        raise ValueError("direction must be 'Left', 'Right', or 'Center'.")

    if direction == 'Center':
        M_left = pmat(sig, max_window, direction='Left')
        M_right = pmat(sig, max_window, direction='Right')
        return (M_left + M_right) / 2

    M = np.ndarray(shape=(max_window, N))
    padded_sig = np.concatenate((np.ones(N) * sig[0], sig, np.ones(N) * sig[-1]))

    for w in range(1, max_window + 1):
        if direction == 'Left':
            M[w - 1] = _moving_average(padded_sig[N - w : 2 * N - 1], window=w)
        elif direction == 'Right':
            M[w - 1] = _moving_average(padded_sig[N : 2 * N - 1 + w], window=w)

    return M


__all__ = ["pmat"]
