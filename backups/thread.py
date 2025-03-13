# def startRecordingOne(self):
    #     self.record_btn1.configure(state="disabled")  # Disable button during recording
    #     self.recorder.recordSignal()
    #     mb(title="Start", message="Recording 1 has started.")
    #     if not self.gif_running:
    #         self.gif_running = True
    #         self.animateWave()
    #     self.animateWave()
    #     threading.Thread(target=self.enableRecordButtonTwo).start()

    # def enableRecordButtonTwo(self):
    #     self.recorder.recording_finished_event.wait()  # Wait for recording to finish
    #     self.record_btn2.configure(state="normal")

    # def startRecordingTwo(self):
    #     self.recorder.recordSignal()
    #     mb(title="Start", message="Recording 2 has started.")
    #     if not self.gif_running:
    #         self.gif_running = True
    #         self.animateWave()
    #     self.animateWave()
    #     # Wait for recording to finish before enabling buttons or saving
    #     threading.Thread(target=self.enableSaveAndPlot).start()

    # def enableSaveAndPlot(self):
    #     self.recorder.recording_finished_event.wait()  # Wait for recording to finish
    #     self.plot_button.configure(state="normal")  # Enable plot button
