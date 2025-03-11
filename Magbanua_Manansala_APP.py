import pyaudio
import wave
import numpy as np
from matplotlib.figure import Figure
import time
import threading


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

    def recordSignal(self, seconds=5.0, sample_rate= 44100):
        self.is_recording = True
        self.is_paused = False
        self.frames = []
        self.recording_finished_event.clear()
        self.sample_rate = sample_rate

        def recordingFunc(seconds):
            self.stream = self.pa.open(
                format=self.format,
                channels=self.channels,
                rate=self.sample_rate,
                input=True,
                frames_per_buffer=self.frames_per_buffer,
            )
            print("Recording started")
            second_tracking = 0
            second_count = 0
            try:
                while self.is_recording and second_count < seconds:
                    if not self.is_paused:
                        data = self.stream.read(self.frames_per_buffer)
                        self.frames.append(data)
                        second_tracking += 1
                        if second_tracking == int(self.rate / self.frames_per_buffer):
                            second_count += 1
                            second_tracking = 0
                            print(f"Time Left: {seconds + - second_count} seconds")
                    else:
                        time.sleep(0.1)
                print("Recording finished, time limit reached")

            except Exception as e:
                print(f"Error during recording: {e}")
            finally:
                self.stream.stop_stream()
                self.stream.close()
                self.stream = None
                self.recording_finished_event.set()
                self.is_recording = False

        self.record_thread = threading.Thread(target=recordingFunc, args=(seconds,))
        self.record_thread.daemon = True
        self.record_thread.start()

    def saveRecording0ne(self, filename="record1.wav"):
        print("Recording 1 saved.")
        obj = wave.open(filename, "wb")
        obj.setnchannels(self.channels)
        obj.setsampwidth(self.pa.get_sample_size(self.format))
        obj.setframerate(self.rate)
        obj.writeframes(b"".join(self.frames))
        obj.close()

    def saveRecordingTwo(self, filename="record2.wav"):
        print("Recording 2 saved.")
        obj = wave.open(filename, "wb")
        obj.setnchannels(self.channels)
        obj.setsampwidth(self.pa.get_sample_size(self.format))
        obj.setframerate(self.rate)
        obj.writeframes(b"".join(self.frames))
        obj.close()
        
    def readWavfile(self, filename):
        obj = wave.open(filename, "rb")
        data = obj.readframes(obj.getnframes())
        obj.close()
        return data

    def __del__(self):
        self.pa.terminate()
