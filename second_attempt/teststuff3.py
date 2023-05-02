import numpy as np
from scipy.signal import find_peaks, peak_prominences
import matplotlib.pyplot as plt

# Define the sample points
t = np.linspace(0, 6*np.pi, 1000)

# Generate a test signal
signal = np.sin(t)

# Compute the upper and lower envelopes
window_size = 100
step_size = 50
n_segments = int(np.ceil((len(signal) - window_size) / step_size)) + 1
upper_envelope = np.zeros_like(signal)
lower_envelope = np.zeros_like(signal)
for i in range(n_segments):
    start = i * step_size
    end = start + window_size
    segment = signal[start:end]
    peaks, _ = find_peaks(segment)
    print(peaks)
    if len(peaks)>0:
        prominences = peak_prominences(segment, peaks)[0]
        upper_envelope[start:end] = np.interp(np.arange(start, end), peaks, segment[peaks] - prominences)
        lower_envelope[start:end] = np.interp(np.arange(start, end), peaks, segment[peaks])

# Plot the signal and its envelopes
fig, ax = plt.subplots()
ax.plot(t, signal, label='Signal')
ax.plot(t, upper_envelope, label='Upper envelope')
ax.plot(t, lower_envelope, label='Lower envelope')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.legend()
plt.show()
