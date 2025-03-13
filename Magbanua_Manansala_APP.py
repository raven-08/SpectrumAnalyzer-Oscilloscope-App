import pyaudio
import wave
import numpy as np
from matplotlib.figure import Figure
import time
import threading
import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpk
import os


class VoiceRecorder:
    def __init__(
        self,
        frames_per_buffer=44100,
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
    ):
        self.frames_per_buffer = frames_per_buffer
        self.format = format
        self.channels = channels
        self.rate = rate
        self.pa = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.is_recording = False
        self.is_paused = False
        self.record_thread = None
        self.recording_finished_event = threading.Event()

    def recordSignal(self, duration=5.0, sample_rate=44100):
        self.is_recording = True
        self.is_paused = False
        self.frames = []
        self.recording_finished_event.clear()
        self.sample_rate = sample_rate

        def recordingFunc(duration):
            self.stream = self.pa.open(
                format=self.format,
                channels=self.channels,
                rate=self.sample_rate,
                input=True,
                frames_per_buffer=self.frames_per_buffer,
            )
            # print("Recording started")
            print("\033[96m" + "Recording started." + "\033[0m")
            second_tracking = 0
            second_count = 0
            try:
                while self.is_recording and second_count < duration:
                    if not self.is_paused:
                        data = self.stream.read(self.frames_per_buffer)
                        self.frames.append(data)
                        second_tracking += 1
                        if second_tracking == int(self.rate / self.frames_per_buffer):
                            second_count += 1
                            second_tracking = 0
                            print(f"Time Left: {duration + - second_count} seconds")
                    else:
                        time.sleep(0.1)
                print("Recording finished, time limit reached.")

            except Exception as e:
                print(f"Error during recording: {e}")
            finally:
                self.stream.stop_stream()
                self.stream.close()
                self.stream = None
                self.recording_finished_event.set()
                self.is_recording = False

        self.record_thread = threading.Thread(target=recordingFunc, args=(duration,))
        self.record_thread.daemon = True
        self.record_thread.start()

    def saveRecording0ne(self, filename="record1.wav"):
        # print("Recording 1 saved.")
        print("\033[91m" + "Recording 1 saved." + "\033[0m")
        obj = wave.open(filename, "wb")
        obj.setnchannels(self.channels)
        obj.setsampwidth(self.pa.get_sample_size(self.format))
        obj.setframerate(self.rate)
        obj.writeframes(b"".join(self.frames))
        obj.close()

    def saveRecordingTwo(self, filename="record2.wav"):
        # print("Recording 2 saved.")
        print("\033[91m" + "Recording 2 saved." + "\033[0m")
        obj = wave.open(filename, "wb")
        obj.setnchannels(self.channels)
        obj.setsampwidth(self.pa.get_sample_size(self.format))
        obj.setframerate(self.rate)
        obj.writeframes(b"".join(self.frames))
        obj.close()

    def readWavfiles(self, filename1="record1.wav", filename2="record2.wav"):
        self.s_rate1, self.signal1 = wavfile.read(filename1)
        self.s_rate2, self.signal2 = wavfile.read(filename2)
        self.min_length = min(len(self.signal1), len(self.signal2))
        self.signal1 = self.signal1[: self.min_length]
        self.signal2 = self.signal2[: self.min_length]

    def computeFFT(self, sample_rate=None):
        self.composite_signal = self.signal1 + self.signal2

        self.FFT1 = abs(fftpk.fft(self.signal1))
        self.FFT2 = abs(fftpk.fft(self.signal2))
        self.FFT_composite = abs(fftpk.fft(self.composite_signal))

        if sample_rate is None:
            sample_rate = self.s_rate1
        self.freqs = fftpk.fftfreq(len(self.FFT1), (1.0 / sample_rate))

    def plotSpectrum(self):
        self.readWavfiles()
        self.computeFFT()
        spectum = Figure(figsize=(7, 5), dpi=100)
        subplot = spectum.add_subplot(111)
        subplot.plot(
            self.freqs[: len(self.FFT1) // 2],
            self.FFT1[: len(self.FFT1) // 2],
            label="Signal 1",
            color="blue",
            alpha=1,
        )
        subplot.plot(
            self.freqs[: len(self.FFT2) // 2],
            self.FFT2[: len(self.FFT2) // 2],
            label="Signal 2",
            color="green",
            alpha=1,
        )
        subplot.plot(
            self.freqs[: len(self.FFT_composite) // 2],
            self.FFT_composite[: len(self.FFT_composite) // 2],
            label="Composite Signal",
            color="purple",
            alpha=0.6,
        )
        subplot.set_xlabel("Frequency (Hz)", fontsize=10, fontweight="bold")
        subplot.set_ylabel("Amplitude", fontsize=10, fontweight="bold")
        subplot.set_title(
            "Spectrum Analyzer", fontsize=12, fontweight="bold", color="darkred"
        )
        subplot.grid(True, linestyle="--", alpha=0.6)
        subplot.legend(fontsize=8)
        return spectum

    def plotOscilloscope(self):
        self.readWavfiles()
        time = np.linspace(0, self.min_length / self.s_rate1, num=self.min_length)
        composite_signal = self.signal1 + self.signal2
        oscilloscope = Figure(figsize=(7, 5), dpi=100)
        subplot = oscilloscope.add_subplot(111)
        subplot.plot(
            time,
            self.signal1,
            color="purple",
            linestyle="--",
            label="Signal 1",
            alpha=0.6,
        )
        subplot.plot(
            time,
            self.signal2,
            color="pink",
            linestyle=":",
            label="Signal 2",
            alpha=1,
        )
        subplot.plot(
            time,
            composite_signal,
            "skyblue",
            label="Sum",
            alpha=1,
        )
        subplot.set_xlabel(
            "Time (s)",
            fontsize=10,
            fontweight="bold",
        )
        subplot.set_ylabel(
            "Amplitude",
            fontsize=10,
            fontweight="bold",
        )
        subplot.set_title(
            "Oscilloscope",
            fontsize=12,
            fontweight="bold",
            color="darkred",
        )
        subplot.grid(True, linestyle="--", alpha=0.6)
        subplot.legend(fontsize=8)
        return oscilloscope

    def saveSpectrumGraph(self, filename="spectrum.jpg"):
        spectrum_figure = self.plotSpectrum()
        spectrum_figure.savefig(filename, format="jpeg")
        print(f"Spectrum graph saved as {filename}")

    def saveOscilloscopeGraph(self, filename="oscilloscope.jpg"):
        oscilloscope_figure = self.plotOscilloscope()
        oscilloscope_figure.savefig(filename, format="jpeg")
        print(f"Oscilloscope graph saved as {filename}")

    def readAndPlotWAV(self, filename1, filename2, sample_rate=None):
        self.s_rate1, self.signal1 = wavfile.read(filename1)
        self.s_rate2, self.signal2 = wavfile.read(filename2)
        self.min_length = min(len(self.signal1), len(self.signal2))
        self.signal1 = self.signal1[: self.min_length]
        self.signal2 = self.signal2[: self.min_length]

        self.composite_signal = self.signal1 + self.signal2

        self.FFT1 = abs(fftpk.fft(self.signal1))
        self.FFT2 = abs(fftpk.fft(self.signal2))
        self.FFT_composite = abs(fftpk.fft(self.composite_signal))

        if sample_rate is None:
            sample_rate = self.s_rate1
        self.freqs = fftpk.fftfreq(len(self.FFT1), (1.0 / sample_rate))

    def __del__(self):
        self.pa.terminate()
