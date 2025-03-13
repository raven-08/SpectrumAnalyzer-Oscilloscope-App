import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt

s_rate1, signal1 = wavfile.read("record1.wav")
s_rate2, signal2 = wavfile.read("record2.wav")
min_length = min(len(signal1), len(signal2))
signal1 = signal1[:min_length]
signal2 = signal2[:min_length]
time = np.linspace(0, min_length / s_rate1, num=min_length)
composite_signal = signal1 + signal2

plt.figure(figsize=(12, 6))
plt.plot(time, signal1, color="purple", linestyle="--", label="Signal 1", alpha=0.6)
plt.plot(time, signal2, color="pink", linestyle=":", label="Signal 2", alpha=1)
plt.plot(time, composite_signal, "skyblue", label="Composite Signal", alpha=0.6)
plt.xlabel("Time (s)", fontsize=12, fontweight="bold")
plt.ylabel("Amplitude", fontsize=12, fontweight="bold")
plt.title(
    "Oscilloscope",
    fontsize=14,
    fontweight="bold",
    color="darkred",
)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()
