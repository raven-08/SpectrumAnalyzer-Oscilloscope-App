import customtkinter as ctk
from CTkMessagebox import CTkMessagebox as mb
from PIL import Image, ImageSequence
from Magbanua_Manansala_APP import VoiceRecorder


class VoiceRecorderGUI(ctk.CTkFrame):
    ctk.set_appearance_mode("light")

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.parent = master
        self.poppins = ctk.CTkFont(
            family="Poppins",
        )
        self.parent.title("Voice Recorder")
        self.parent.geometry("1000x600")
        self.recorder = VoiceRecorder()
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
        self.logo_image = ctk.CTkImage(
            light_image=Image.open("utils/logo.png"),
            size=(400, 350),
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
        #   self.tabview = ctk.CTkTabview(
        #       self.frame,
        #       width=675,
        #       height=475,
        #       segmented_button_selected_color="#FF6505",
        #       segmented_button_selected_hover_color="#FF8C42",
        #       anchor="n",
        #   )
        #   self.tabview.place(x=240, y=70)
        #   self.tabview.add("Spectrum Analyzer")
        #   self.tabview.add("Oscilloscope")

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
        self.badge1 = ctk.CTkLabel(
            self.frame,
            text="1",
            text_color="white",
            font=(self.poppins, 12, "bold"),
            fg_color="red",
            bg_color="red",
            height=20,
            width=20,
            corner_radius=7.65,
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
        self.badge2 = ctk.CTkLabel(
            self.frame,
            text="2",
            text_color="white",
            font=(self.poppins, 12, "bold"),
            fg_color="red",
            bg_color="red",
            height=20,
            width=20,
            corner_radius=7.65,
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
            font=(self.poppins, 17, "bold"),
            height=40,
            width=145,
            corner_radius=4,
            state="normal",
            # command=self.saveRecording,
            command=self.saveRecordOneAndTwo,
        )
        self.check = ctk.CTkLabel(
            self.frame,
            text="1",
            text_color="white",
            font=(self.poppins, 12, "bold"),
            fg_color="red",
            bg_color="red",
            height=20,
            width=20,
            corner_radius=7.65,
        )
        self.save_button.place(x=45, y=185, anchor="w")
        self.check.place(x=160, y=190, anchor="w")

        self.plot_button = ctk.CTkButton(
            self.frame,
            image=self.plot_icon,
            text="Plot",
            compound="left",
            fg_color="#FF6505",
            hover_color="#FF8C42",
            text_color="white",
            font=(self.poppins, 14, "bold"),
            height=40,
            width=140,
            corner_radius=4,
            state="disabled",
            # command=self.plot_Recording,
        )
        self.current_frame = 0
        self.gif_running = False
        self.wave_gif = "utils/wave.gif"
        self.gif = Image.open(self.wave_gif)
        self.frames = [
            ctk.CTkImage(light_image=frame.convert("RGBA"), size=(400, 350))
            for frame in ImageSequence.Iterator(self.gif)
        ]
        self.plot_current_frame = 0
        self.plot_running = False
        self.hero = ctk.CTkLabel(self.hero_frame, image=self.logo_image, text="")
        self.hero.pack()
        self.dark_button.place(relx=0.96, rely=0.05, anchor="ne")

        self.save_button.place(x=45, y=185, anchor="w")
        self.plot_button.place(x=45, y=255, anchor="w")

    def startRecordingOne(self):
        self.recorder.recordSignal()
        mb(title="Start", message="Recording 1 has started.")
        if not self.gif_running:
            self.gif_running = True
            self.animateWave()
        self.is_paused = False
        self.animateWave()
        self.save_button.configure(state="normal", text="Save ₁")
        self.plot_button.configure(state="disabled")
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
        self.save_button.configure(state="normal", text="Save ₂")
        self.plot_button.configure(state="disabled")
        self.track_button = 2

    def saveRecordOneAndTwo(self):
        if self.track_button == 2:
            self.recorder.saveRecordingTwo()
            self.save_button.configure(
                text="Save ₁",
                image=self.save_icon,
            )

            self.record_btn2.configure(state="disabled")
            self.is_paused = True

        else:
            self.recorder.saveRecording0ne()
            self.save_button.configure(text="Save ₂", image=self.save_icon)
            self.record_btn2.configure(state="normal")
            self.record_btn1.configure(state="disabled")
            self.is_paused = True

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
            frame = self.frames[self.current_frame]
            self.hero.configure(image=frame)
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.after(100, self.animateWave)


root = ctk.CTk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = VoiceRecorderGUI(root)
root.mainloop()
