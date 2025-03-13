import customtkinter as ctk
import os
from themes.theme import Theme
from CTkMessagebox import CTkMessagebox as mb
from PIL import Image, ImageSequence
from Magbanua_Manansala_APP import VoiceRecorder
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from customtkinter import filedialog


class VoiceRecorderGUI(ctk.CTkFrame):
    ctk.set_appearance_mode("light")

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.parent = master
        self.poppins = ctk.CTkFont(
            family="Poppins",
        )
        self.parent.title("Voice Recorder")
        self.parent.geometry("1250x750")
        self.recorder = VoiceRecorder()
        self.is_theme_open = False
        self.is_darked = False
        self.is_paused = False
        self.track_button = 1

        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frame = ctk.CTkFrame(self, corner_radius=10)
        self.frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.hero_frame = ctk.CTkFrame(
            self.frame,
            corner_radius=10,
            width=450,
            height=400,
            fg_color="transparent",
        )
        self.hero_frame.place(x=360, y=70)
        self.plot_frame = ctk.CTkFrame(
            self.hero_frame,
            fg_color="transparent",
        )
        self.plot_frame.place(x=278, y=75)
        self.theme_frame = ctk.CTkFrame(
            self.frame,
            corner_radius=8,
            width=250,
            height=450,
        )
        self.theme_icon = ctk.CTkImage(
            light_image=Image.open("icons/theme.png"),
            dark_image=Image.open("icons/theme_dark.png"),
            size=(20, 20),
        )
        self.dark_icon = ctk.CTkImage(
            light_image=Image.open("icons/moon.png"),
            dark_image=Image.open("icons/moon_dark.png"),
            size=(20, 20),
        )
        self.sun_icon = ctk.CTkImage(
            light_image=Image.open("icons/sun.png"),
            dark_image=Image.open("icons/sun_dark.png"),
            size=(20, 20),
        )
        self.mic_icon = ctk.CTkImage(
            light_image=Image.open("icons/mic_dark.png"),
            dark_image=Image.open("icons/mic.png"),
            size=(20, 20),
        )
        self.pause_icon = ctk.CTkImage(
            light_image=Image.open("icons/pause.png"),
            dark_image=Image.open("icons/pause_dark.png"),
            size=(20, 20),
        )
        self.resume_icon = ctk.CTkImage(
            light_image=Image.open("icons/resume.png"),
            dark_image=Image.open("icons/resume_dark.png"),
            size=(20, 20),
        )
        self.stop_icon = ctk.CTkImage(
            light_image=Image.open("icons/stop.png"),
            dark_image=Image.open("icons/stop_dark.png"),
            size=(20, 20),
        )
        self.save_icon = ctk.CTkImage(
            light_image=Image.open("icons/save.png"),
            dark_image=Image.open("icons/save_dark.png"),
            size=(20, 20),
        )
        self.download_icon = ctk.CTkImage(
            light_image=Image.open("icons/download.png"),
            dark_image=Image.open("icons/download_dark.png"),
            size=(20, 20),
        )
        self.play_icon = ctk.CTkImage(
            light_image=Image.open("icons/play.png"),
            dark_image=Image.open("icons/play_dark.png"),
            size=(20, 20),
        )
        self.plot_icon = ctk.CTkImage(
            light_image=Image.open("icons/plot.png"),
            dark_image=Image.open("icons/plot_dark.png"),
            size=(20, 20),
        )
        self.upload_icon = ctk.CTkImage(
            light_image=Image.open("icons/upload.png"),
            dark_image=Image.open("icons/upload_dark.png"),
            size=(20, 20),
        )
        self.logo_image = ctk.CTkImage(
            light_image=Image.open("utils/logo.png"),
            size=(450, 400),
        )
        self.dark_button = ctk.CTkButton(
            self.frame,
            image=self.dark_icon,
            text="",
            fg_color="#FF6505",
            hover_color="#FF8C42",
            text_color="white",
            font=(self.poppins, 14, "bold"),
            height=40,
            width=40,
            corner_radius=4,
            command=self.lightDarkMode,
        )
        self.theme_button = ctk.CTkButton(
            self.frame,
            image=self.theme_icon,
            text="",
            text_color="white",
            fg_color="#FF6505",
            hover_color="#FF8C42",
            font=(self.poppins, 14, "bold"),
            height=40,
            width=40,
            corner_radius=4,
            # command=self.toggleThemeFrame,
        )
        self.dark_button.place(relx=0.91, rely=0.03, anchor="ne")
        self.theme_button.place(relx=0.97, rely=0.03, anchor="ne")

        self.record_btn1 = ctk.CTkButton(
            self.frame,
            image=self.mic_icon,
            text="",
            compound="left",
            fg_color="#FF6505",
            hover_color="#FF8C42",
            text_color=["white", "black"],
            font=(self.poppins, 24, "bold"),
            height=40,
            width=60,
            corner_radius=4,
            command=self.startRecordingOne,
        )
        self.record_btn2 = ctk.CTkButton(
            self.frame,
            image=self.mic_icon,
            text="",
            compound="left",
            fg_color="#FF6505",
            hover_color="#FF8C42",
            text_color=["white", "black"],
            font=(self.poppins, 24, "bold"),
            height=40,
            width=60,
            corner_radius=4,
            state="normal",
            command=self.startRecordingTwo,
        )
        self.badge1 = ctk.CTkLabel(
            self.frame,
            text="1",
            text_color="white",
            font=(self.poppins, 12, "bold"),
            fg_color="red",
            bg_color="red",
            height=20,
            width=20,
        )
        self.badge2 = ctk.CTkLabel(
            self.frame,
            text="2",
            text_color="white",
            font=(self.poppins, 12, "bold"),
            fg_color="red",
            bg_color="red",
            height=20,
            width=20,
        )
        self.record_btn1.place(x=45, y=115, anchor="w")
        self.record_btn2.place(x=160, y=115, anchor="w")
        self.badge1.place(x=114, y=124, anchor="w")
        self.badge2.place(x=229, y=124, anchor="w")
        self.save_button = ctk.CTkButton(
            self.frame,
            image=self.save_icon,
            text="Save",
            compound="left",
            fg_color="#FF6505",
            hover_color="#FF8C42",
            text_color=["white", "black"],
            text_color_disabled=["white", "black"],
            font=(self.poppins, 14, "bold"),
            height=40,
            width=145,
            corner_radius=4,
            state="disabled",
            command=self.saveRecordOneAndTwo,
        )
        self.check = ctk.CTkLabel(
            self.frame,
            text="1",
            text_color="white",
            font=(self.poppins, 12, "bold"),
            fg_color="#FF6505",
            bg_color="#FF6505",
            height=20,
            width=20,
        )
        self.save_button.place(x=45, y=185, anchor="w")
        self.check.place(x=164, y=190, anchor="w")

        self.plot_button = ctk.CTkButton(
            self.frame,
            image=self.plot_icon,
            text="Plot",
            compound="left",
            fg_color="#FF6505",
            hover_color="#FF8C42",
            text_color=["white", "black"],
            text_color_disabled=["white", "black"],
            font=(self.poppins, 14, "bold"),
            height=40,
            width=145,
            corner_radius=4,
            state="disabled",
            command=self.showPlot,
        )
        self.upload_button = ctk.CTkButton(
            self.frame,
            image=self.upload_icon,
            text="Upload",
            compound="left",
            fg_color="#FF6505",
            hover_color="#FF8C42",
            text_color=["white", "black"],
            text_color_disabled=["white", "black"],
            font=(self.poppins, 14, "bold"),
            height=40,
            width=145,
            corner_radius=4,
            state="disabled",
            command=self.uploadWavFile,
        )
        self.save_graph = ctk.CTkButton(
            self.frame,
            image=self.download_icon,
            text="Save Graph",
            compound="left",
            fg_color="#FF6505",
            hover_color="#FF8C42",
            text_color=["white", "black"],
            text_color_disabled=["white", "black"],
            font=(self.poppins, 14, "bold"),
            height=40,
            width=145,
            corner_radius=4,
            state="disabled",
            command=self.saveGraph,
        )
        self.plot_button.place(x=45, y=255, anchor="w")
        self.upload_button.place(x=45, y=325, anchor="w")
        self.save_graph.place(x=45, y=395, anchor="w")

        self.current_frame = 0
        self.gif_running = False
        self.wave_gif = "utils/wave.gif"
        self.gif = Image.open(self.wave_gif)
        self.frames = [
            ctk.CTkImage(light_image=frame.convert("RGBA"), size=(400, 350))
            for frame in ImageSequence.Iterator(self.gif)
        ]
        self.hero = ctk.CTkLabel(self.hero_frame, image=self.logo_image, text="")
        self.hero.place(x=65, y=50)

        self.tabview = ctk.CTkTabview(
            self.frame,
            width=800,
            height=600,
            segmented_button_selected_color="#FF6505",
            segmented_button_selected_hover_color="#FF8C42",
            anchor="ne",
        )
        self.tabview.add("Spectrum Analyzer")
        self.tabview.add("Oscilloscope")
        self.spectrum_frame = ctk.CTkFrame(
            self.tabview.tab("Spectrum Analyzer"), fg_color="transparent"
        )
        self.spectrum_frame.pack(fill=ctk.BOTH, expand=True)
        self.oscilloscope_frame = ctk.CTkFrame(
            self.tabview.tab("Oscilloscope"), fg_color="transparent"
        )
        self.oscilloscope_frame.pack(fill=ctk.BOTH, expand=True)
        self.tabview.place_forget()

    def startRecordingOne(self):
        self.recorder.recordSignal()
        mb(title="Start", message="Recording 1 has started.")
        if not self.gif_running:
            self.gif_running = True
            self.animateWave()
        self.is_paused = False
        self.animateWave()
        self.save_button.configure(state="normal", text="Save")
        # self.plot_button.configure(state="disabled")
        self.record_btn2.configure(state="disabled")
        self.track_button = 1

    def startRecordingTwo(self):
        self.recorder.recordSignal()
        mb(title="Start", message="Recording 2 has started.")
        if not self.gif_running:
            self.gif_running = True
            self.animateWave()
        self.is_paused = False
        self.animateWave()
        self.save_button.configure(state="normal", text="Save")
        # self.plot_button.configure(state="disabled")
        self.track_button = 2

    def saveRecordOneAndTwo(self):
        if self.track_button == 2:
            mb(
                title="Recording Saved",
                message="Record 2 save successfully.",
                icon="check",
                option_1="OK",
            )
            self.recorder.saveRecordingTwo()
            self.save_button.configure(
                text="Save",
                image=self.save_icon,
            )
            self.check.configure(text="1")
            self.plot_button.configure(state="normal")
            self.upload_button.configure(state="normal")
            self.save_graph.configure(state="normal")

            self.record_btn2.configure(state="disabled")
            self.badge2.configure(fg_color="green", bg_color="green")
            self.is_paused = True

        else:
            mb(
                title="Recording Saved",
                message="Record 1 save successfully.",
                icon="check",
                option_1="OK",
            )
            self.recorder.saveRecording0ne()
            self.save_button.configure(text="Save", image=self.save_icon)
            self.check.configure(text="2")
            self.record_btn2.configure(state="normal")
            self.record_btn1.configure(state="disabled")
            self.badge1.configure(fg_color="green", bg_color="green")
            self.is_paused = True

    def showPlot(self):
        mb(
            title="Plot Graph",
            message="Graph plotted successful.",
            icon="check",
            option_1="OK",
        )
        self.tabview.place(x=278, y=75)
        self.plotSpectrum()
        self.plotOscilloscope()
        self.tabview.set("Spectrum Analyzer")

    def plotSpectrum(self):
        self.hero.destroy()
        for widget in self.spectrum_frame.winfo_children():
            widget.destroy()

        spectrum_fig = self.recorder.plotSpectrum()

        if spectrum_fig:
            canvas = FigureCanvasTkAgg(spectrum_fig, master=self.spectrum_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self.spectrum_frame)
            toolbar.update()
            toolbar.pack(fill=ctk.BOTH, expand=True)
            self.spectrum_frame.pack(fill=ctk.BOTH, expand=True)

    def plotOscilloscope(self):
        self.hero.destroy()
        for widget in self.oscilloscope_frame.winfo_children():
            widget.destroy()

        oscilloscope_fig = self.recorder.plotOscilloscope()

        if oscilloscope_fig:
            canvas = FigureCanvasTkAgg(oscilloscope_fig, master=self.oscilloscope_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self.oscilloscope_frame)
            toolbar.update()
            toolbar.pack(fill=ctk.BOTH, expand=True)

            self.oscilloscope_frame.pack(fill=ctk.BOTH, expand=True)

    def uploadWavFile(self):
        file_paths = filedialog.askopenfilenames(
            initialdir="../voice_recorder-main",
            filetypes=[("WAV files", "*.wav")],
            title="Select WAV files",
        )
        if len(file_paths) == 1:
            file1 = os.path.basename(file_paths[0])
            mb(
                title="File Uploaded",
                message=f"File {file1} uploaded successfully.",
                icon="check",
                option_1="OK",
            )
            self.plotWavFile(file_paths[0])
        elif len(file_paths) == 2:
            file1 = os.path.basename(file_paths[0])
            file2 = os.path.basename(file_paths[1])
            mb(
                title="Upload WAV",
                message=f"WAV Files {file1} and {file2} uploaded successfully.",
                icon="check",
                option_1="OK",
            )
        else:
            mb(
                title="Error",
                message="Please select one or two WAV files.",
                icon="warning",
                option_1="OK",
            )

    def plotWavFile(self, filename):
        self.hero.destroy()
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        figure = self.recorder.readAndPlotWAV(filename)

        if figure:
            canvas = FigureCanvasTkAgg(figure, master=self.plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self.plot_frame)
            toolbar.update()
            toolbar.pack(fill=ctk.BOTH, expand=True)
            self.plot_frame.pack(fill=ctk.BOTH, expand=True)

    def saveGraph(self):
        mb(
            title="Save Graph",
            message="Graphs saved successfully.",
            icon="check",
            option_1="OK",
        )
        self.recorder.saveOscilloscopeGraph()
        self.recorder.saveSpectrumGraph()

    def lightDarkMode(self):
        if self.is_darked:
            ctk.set_appearance_mode("light")
            self.dark_button.configure(image=self.dark_icon)
        else:
            ctk.set_appearance_mode("dark")
            self.dark_button.configure(image=self.sun_icon)

        self.is_darked = not self.is_darked

    def animateWave(self):
        if not self.is_paused and self.gif_running:
            self.hero.configure(image=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.after(100, self.animateWave)


root = ctk.CTk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = VoiceRecorderGUI(root)
root.mainloop()
