# import scipy.io.wavfile as wavfile
# import scipy.fftpack as fftpk
# import numpy as np
# import matplotlib.pyplot as plt

# s_rate1, signal1 = wavfile.read("record1.wav")
# s_rate2, signal2 = wavfile.read("record2.wav")
# min_length = min(len(signal1), len(signal2))
# signal1 = signal1[:min_length]
# signal2 = signal2[:min_length]
# composite_signal = signal1 + signal2
# FFT1 = abs(fftpk.fft(signal1))
# FFT2 = abs(fftpk.fft(signal2))
# FFT_composite = abs(fftpk.fft(composite_signal))
# freqs = fftpk.fftfreq(len(FFT1), (1.0 / s_rate1))

# plt.plot(freqs[:len(FFT1)//2], FFT1[:len(FFT1)//2], label="Signal 1", color="blue", alpha=1)
# plt.plot(freqs[:len(FFT2)//2], FFT2[:len(FFT2)//2], label="Signal 2", color="green", alpha=1)
# plt.plot(freqs[:len(FFT_composite)//2], FFT_composite[:len(FFT_composite)//2],  label="Composite Signal", color="purple", alpha=0.6)
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Amplitude")
# plt.title("Spectrum Analyzer")
# plt.legend()
# plt.show()

import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpk
import numpy as np
import matplotlib.pyplot as plt

s_rate1, signal1 = wavfile.read("record1.wav")
s_rate2, signal2 = wavfile.read("record2.wav")
min_length = min(len(signal1), len(signal2))
signal1 = signal1[:min_length]
signal2 = signal2[:min_length]
composite_signal = signal1 + signal2
FFT1 = abs(fftpk.fft(signal1))
FFT2 = abs(fftpk.fft(signal2))
FFT_composite = abs(fftpk.fft(composite_signal))
freqs = fftpk.fftfreq(len(FFT1), (1.0 / s_rate1))

plt.figure(figsize=(12, 6))
plt.plot(freqs[:len(FFT1)//2], FFT1[:len(FFT1)//2], label="Signal 1", color="blue", alpha=1)
plt.plot(freqs[:len(FFT2)//2], FFT2[:len(FFT2)//2], label="Signal 2", color="green", alpha=1)
plt.plot(freqs[:len(FFT_composite)//2], FFT_composite[:len(FFT_composite)//2],  label="Composite Signal", color="purple", alpha=0.6)
plt.xlabel("Frequency (Hz)", fontsize=12, fontweight="bold")
plt.ylabel("Amplitude", fontsize=12, fontweight="bold")
plt.title(
            "Spectrum Analyzer",
            fontsize=14,
            fontweight="bold",
            color="darkred",
        )
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()