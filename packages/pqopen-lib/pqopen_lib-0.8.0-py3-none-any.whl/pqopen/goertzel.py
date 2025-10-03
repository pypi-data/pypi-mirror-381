import numpy as np
try:
    from numba import njit, float32, float64
except ImportError:
    # Dummy-Decorator if numba not available
    def njit(func=None, **kwargs):
        if func is None:
            return lambda f: f
        return func
    float32 = float64 = None

@njit
def calc_single_freq(x: np.array, f_hz: float, fs: float) -> tuple[float, float]:
    """Compute the amplitude and phase of a specific frequency component
    in a signal using the Goertzel algorithm.

    Parameters:
        x: Input signal (time-domain samples).
        f_hz: Target frequency in Hertz (Hz).
        fs: Sampling frequency of the signal in Hertz (Hz).

    Returns:
        tuple:
            amp: Amplitude of the frequency component.
            phase: Phase of the frequency component in radians.
    """
    N = len(x)                  # Number of samples
    k = (f_hz * N) / fs         # Corresponding DFT bin index (can be fractional)
    w = 2 * np.pi * k / N       # Angular frequency for the bin
    cw = np.cos(w)              # Cosine component
    c = 2 * cw                  # Multiplier used in recurrence relation
    sw = np.sin(w)              # Sine component
    z1, z2 = 0, 0               # Initialize state variables

    # Recursive filter loop
    for n in range(N):
        z0 = x[n] + c * z1 - z2  # Apply recurrence relation
        z2 = z1                  # Shift states
        z1 = z0

    # Compute real and imaginary parts of the result
    ip = cw * z1 - z2   # In-phase (real) component
    qp = sw * z1        # Quadrature (imaginary) component

    # Compute amplitude and phase of the frequency component
    amp = np.sqrt((ip**2 + qp**2)/2) / (N / 2)
    phase = np.arctan2(qp, ip)

    return amp, phase

# >>>>>>> Pre-Compile for float32 und float64 <<<<<<<
if float32 is not None and float64 is not None:
    sigs = [
        "(float32[:], float32, float32)",
        "(float64[:], float64, float64)"
    ]
    for sig in sigs:
        calc_single_freq.compile(sig)