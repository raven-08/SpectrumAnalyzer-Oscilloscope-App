# plt.plot(
#     self.freqs[: len(self.FFT1) // 2],
#     self.FFT1[: len(self.FFT1) // 2],
#     label="Signal 1",
#     color="blue",
#     alpha=1,
# )
# plt.plot(
#     self.freqs[: len(self.FFT2) // 2],
#     self.FFT2[: len(self.FFT2) // 2],
#     label="Signal 2",
#     color="green",
#     alpha=1,
# )
# plt.plot(
#     self.freqs[: len(self.FFT_composite) // 2],
#     self.FFT_composite[: len(self.FFT_composite) // 2],
#     label="Composite Signal",
#     color="purple",
#     alpha=0.6,
# )

# plt.xlabel("Frequency (Hz)", fontsize=12, fontweight="bold")
# plt.ylabel("Amplitude", fontsize=12, fontweight="bold")
# plt.title("Spectrum Analyzer", fontsize=14, fontweight="bold", color="darkred")
# plt.grid(True, linestyle="--", alpha=0.6)
# plt.legend()
# plt.show()


# plt.figure(figsize=(12, 6))
# plt.plot(time, self.signal1, color="purple", linestyle="--", label="Signal 1", alpha=0.6)
# plt.plot(time, self.signal2, color="pink", linestyle=":", label="Signal 2", alpha=1)
# plt.plot(time, composite_signal, "skyblue", label="Composite Signal", alpha=0.6)
# plt.xlabel("Time (s)", fontsize=12, fontweight="bold")
# plt.ylabel("Amplitude", fontsize=12, fontweight="bold")
# plt.title(
#     "Oscilloscope",
#     fontsize=14,
#     fontweight="bold",
#     color="darkred",
# )
# plt.grid(True, linestyle="--", alpha=0.6)
# plt.legend()
# plt.show()


# Before
# def showPlot(self):
#     self.tabview.place(x=240, y=50)  # Make tabview visible
#     self.plotRecording()

# def plotRecording(self):
#     # Destroy previous plots
#     self.hero.destroy()
#     for widget in self.plot_frame.winfo_children():
#         widget.destroy()

#     # Get spectrum figure from recorder
#     spectrum_fig = self.recorder.plotSpectrum()

#     if spectrum_fig:
#         # Embed figure into the tabview's plot_frame
#         canvas = FigureCanvasTkAgg(spectrum_fig, master=self.plot_frame)
#         canvas.draw()
#         canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

#         # Add toolbar for navigation
#         toolbar = NavigationToolbar2Tk(canvas, self.plot_frame)
#         toolbar.update()
#         toolbar.pack(fill=ctk.BOTH, expand=True)

#         # Ensure the plot frame is packed
#         self.plot_frame.pack(fill=ctk.BOTH, expand=True)
