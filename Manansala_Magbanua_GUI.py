import customtkinter as ctk
from threading import Thread
import time
from themes.theme import Theme
from CTkMessagebox import CTkMessagebox as mb
from PIL import Image, ImageSequence
from Magbanua_Manansala_APP import SpectrumAnalyzer
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


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
        self.recorder = SpectrumAnalyzer()
        self.is_theme_open = False
        self.is_darked = False
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
            font=(self.poppins, 14, "bold"),
            height=40,
            width=40,
            corner_radius=4,
            command=self.toggleThemeFrame,
        )
        self.dark_button.place(relx=0.91, rely=0.03, anchor="ne")
        self.theme_button.place(relx=0.97, rely=0.03, anchor="ne")

        self.record_btn1 = ctk.CTkButton(
            self.frame,
            image=self.mic_icon,
            text="",
            compound="left",
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
            text_color=["white", "black"],
            font=(self.poppins, 24, "bold"),
            height=40,
            width=60,
            corner_radius=4,
            state="disabled",
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

        self.plot_button = ctk.CTkButton(
            self.frame,
            image=self.plot_icon,
            text="Plot",
            compound="left",
            text_color=["white", "black"],
            text_color_disabled=["white", "black"],
            font=(self.poppins, 14, "bold"),
            height=40,
            width=145,
            corner_radius=4,
            state="disabled",
            command=self.showPlot,
        )
        # self.upload_button = ctk.CTkButton(
        #     self.frame,
        #     image=self.upload_icon,
        #     text="Upload",
        #     compound="left",
        #     text_color=["white", "black"],
        #     text_color_disabled=["white", "black"],
        #     font=(self.poppins, 14, "bold"),
        #     height=40,
        #     width=145,
        #     corner_radius=4,
        #     state="disabled",
        #     command=self.uploadWavFile,
        # )
        self.save_graph = ctk.CTkButton(
            self.frame,
            image=self.download_icon,
            text="Save Graph",
            compound="left",
            text_color=["white", "black"],
            text_color_disabled=["white", "black"],
            font=(self.poppins, 14, "bold"),
            height=40,
            width=145,
            corner_radius=4,
            state="disabled",
            command=self.saveGraph,
        )
        self.plot_button.place(x=45, y=185, anchor="w")
        # self.upload_button.place(x=45, y=255, anchor="w")
        self.save_graph.place(x=45, y=255, anchor="w")

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

        # self.upload_tab_view = ctk.CTkTabview(
        #     self.frame,
        #     width=800,
        #     height=600,
        #     anchor="ne",
        # )
        # self.upload_tab_view.add("Spectrum Analyzer")
        # self.upload_tab_view.add("Oscilloscope")
        # self.upload_spectrum_frame = ctk.CTkFrame(
        #     self.upload_tab_view.tab("Spectrum Analyzer"), fg_color="transparent"
        # )
        # self.upload_spectrum_frame.pack(fill=ctk.BOTH, expand=True)
        # self.upload_oscilloscope_frame = ctk.CTkFrame(
        #     self.upload_tab_view.tab("Oscilloscope"), fg_color="transparent"
        # )
        # self.upload_oscilloscope_frame.pack(fill=ctk.BOTH, expand=True)
        # self.upload_tab_view.place_forget()
        
        self.theme_frame = ctk.CTkFrame(
            self.frame,
            corner_radius=8,
            width=250,
            height=450,
        )
        self.autumn = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#BF6F5F", "#9B4A3C"],
            hover_color=["#C8766D", "#A03E29"],
            border_color=["#BF8F7C", "#6D4F4D"],
            command=self.setAutumnTheme,
        )
        self.autumn.place(relx=0.2, rely=0.1, anchor="n")
        self.breeze = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#4DB3C8", "#2D6D7D"],
            hover_color=["#4A9AB3", "#2B5B6D"],
            border_color=["#4D7A8D", "#9B9F9F"],
            command=self.setBreezeTheme,
        )
        self.breeze.place(relx=0.4, rely=0.1, anchor="n")
        self.carrot = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#F76D57", "#D23016"],
            hover_color=["#E8624A", "#A31600"],
            border_color=["#3E454A", "#949A9F"],
            command=self.setCarrotTheme,
        )
        self.carrot.place(relx=0.6, rely=0.1, anchor="n")
        self.cherry = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#F5B3B3", "#C85C5C"],
            hover_color=["#F29C9C", "#BF3E3E"],
            border_color=["#F4A3A0", "#A8A8A8"],
            command=self.setCherryTheme,
        )
        self.cherry.place(relx=0.8, rely=0.1, anchor="n")
        self.coffee = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#825C46", "#5A3E32"],
            hover_color=["#6F4C37", "#4B3126"],
            border_color=["#3E454A", "#949A9F"],
            command=self.setCoffeeTheme,
        )
        self.coffee.place(relx=0.8, rely=0.1, anchor="n")
        self.lavender = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#B19CD9", "#9370DB"],
            hover_color=["#9370DB", "#7A5DC7"],
            border_color=["#3E454A", "#949A9F"],
            command=self.setLavenderTheme,
        )
        self.lavender.place(relx=0.2, rely=0.22, anchor="n")
        self.marsh = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#7DBE98", "#4E8F69"],
            hover_color=["#6EAA8C", "#397F5A"],
            border_color=["#3E454A", "#949A9F"],
            command=self.setMarshTheme,
        )
        self.marsh.place(relx=0.4, rely=0.22, anchor="n")
        self.metal = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color=["#A0A0A0", "#505050"],
            hover_color=["#909090", "#606060"],
            border_color=["#3E454A", "#949A9F"],
            command=self.setMetalTheme,
        )
        self.metal.place(relx=0.6, rely=0.22, anchor="n")
        self.midnight = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color= ["#003F6C", "#002E5D"],
            hover_color= ["#004080", "#00214B"],
            border_color= ["#003D4E", "#7F8C8D"],
            command=self.setMidnightTheme,
        )
        self.midnight.place(relx=0.8, rely=0.22, anchor="n")
        self.patina = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color= ["#B57A4C", "#6F4C3B"],
            hover_color= ["#A9643A", "#5C3A24"],
            border_color= ["#9B5D3A", "#3E2D1F"],
            command=self.setPatinaTheme,
        )
        self.patina.place(relx=0.2, rely=0.34, anchor="n")
        self.orange = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color= ["#FF8C42", "#FF6505"],
            hover_color= ["#E67320", "#CC5500"],
            border_color= ["#3E454A", "#949A9F"],
            command=self.setOrangeTheme,
        )
        self.orange.place(relx=0.4, rely=0.34, anchor="n")
        self.pink = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color= ["#FF6B6B", "#B74177"],
            hover_color= ["#FF4E4E", "#A01E5C"],
            border_color= ["#3E454A", "#949A9F"],
            command=self.setPinkTheme,
        )
        self.pink.place(relx=0.6, rely=0.34, anchor="n")
        self.red = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color= ["#D03434", "#A11D1D"],
            hover_color= ["#B22E2E", "#791414"],
            border_color= ["#3E454A", "#949A9F"],
            command=self.setRedTheme,
        )
        self.red.place(relx=0.8, rely=0.34, anchor="n")
        self.rime = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color= ["#6E8BA4", "#4A5D6B"],
            hover_color= ["#5F7A8E", "#3A4A54"],
            border_color= ["#6C7B82", "#9D9F9F"],
            command=self.setRimeTheme,
        )
        self.rime.place(relx=0.2, rely=0.46, anchor="n")
        self.rose = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color= ["#a85475", "#6c1f2b"],
            hover_color= ["#98415f", "#5c0f0b"],
            border_color= ["#8b3c49", "#b7707d"],
            command=self.setRoseTheme,
        )
        self.rose.place(relx=0.4, rely=0.46, anchor="n")
        self.sky = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color= ["#27577D", "#BBD1E4"],
            hover_color= ["#000099", "#9999ff"],
            border_color= ["#3E454A", "#949A9F"],
            command=self.setSkyTheme,
        )
        self.sky.place(relx=0.6, rely=0.46, anchor="n")
        self.violet = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color= ["#7C63A6", "#402E5C"],
            hover_color= ["#6C5090", "#301E3C"],
            border_color= ["#5F4B7A", "#8B7FAE"],
            command=self.setVioletTheme,
        )
        self.violet.place(relx=0.8, rely=0.46, anchor="n")
        self.yellow = ctk.CTkButton(
            self.theme_frame,
            text="",
            corner_radius=20,
            height=40,
            width=40,
            fg_color= ["#FFA500", "#FF8C00"],
            hover_color= ["#FF8C00", "#FF6600"],
            border_color= ["#3E454A", "#949A9F"],
            command=self.setYellowTheme,
        )
        self.yellow.place(relx=0.2, rely=0.58, anchor="n")
        self.theme = Theme(
            self.theme_button, self.dark_button, self.frame, self.theme_frame, self.record_btn1, self.record_btn2, self.plot_button, self.save_graph, self.tabview
        )

    def startRecordingOne(self):
        self.resetView()
        self.recorder.recordSignal()
        mb(title="Start", message="Recording 1 has started.")
        self.gif_running = True
        self.animateWave()
        Thread(target=self.changeBadgeColor, args=(self.badge1,)).start()
        Thread(target=self.trackRecordingOne).start()

    def startRecordingTwo(self):
        self.recorder.saveRecording0ne()
        self.recorder.recordSignal()
        mb(title="Start", message="Recording 2 has started.")
        self.gif_running = True
        self.animateWave()
        Thread(target=self.changeBadgeColor, args=(self.badge2,)).start()
        Thread(target=self.trackRecordingTwo).start()

    def changeBadgeColor(self, badge):
        time.sleep(5)
        badge.configure(fg_color="green", bg_color="green")

    def trackRecordingOne(self):
        time.sleep(5)
        self.record_btn2.configure(state="normal")
        self.plot_button.configure(state="disabled")
        self.record_btn1.configure(state="disabled")

    def trackRecordingTwo(self):
        time.sleep(5)
        self.record_btn1.configure(state="normal")
        self.plot_button.configure(state="normal")
        self.record_btn2.configure(state="disabled")

    def showPlot(self):
        self.gif_running = False
        self.hero_frame.forget()
        self.recorder.saveRecordingTwo()
        self.save_graph.configure(state="normal")
        self.badge1.configure(fg_color="red", bg_color="red")
        self.badge2.configure(fg_color="red", bg_color="red")

        mb(
            title="Plot Graph",
            message="Graph plotted successfully.",
            icon="check",
            option_1="OK",
        )
        self.tabview.place(x=278, y=75)
        self.plotSpectrum()
        self.plotOscilloscope()
        self.tabview.set("Spectrum Analyzer")

    # def showPlotWAVFiles(self, filename1, filename2):
    #     self.hero_frame.forget()
    #     self.upload_tab_view.place(x=278, y=75)
    #     self.recorder.readAndPlotWAV(filename1, filename2)
    #     self.uploadPlotSpectrum()
    #     self.uploadPlotOscilloscope()
    #     self.upload_tab_view.set("Spectrum Analyzer")

    def plotSpectrum(self):
        # self.hero.destroy()
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
        # self.hero.destroy()
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

    # def uploadPlotSpectrum(self):
    #     # self.hero.destroy()
    #     self.tabview.place_forget()
    #     for widget in self.upload_spectrum_frame.winfo_children():
    #         widget.destroy()

    #     spectrum_fig = self.recorder.plotSpectrum()

    #     if spectrum_fig:
    #         canvas = FigureCanvasTkAgg(spectrum_fig, master=self.upload_spectrum_frame)
    #         canvas.draw()
    #         canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

    #         toolbar = NavigationToolbar2Tk(canvas, self.upload_spectrum_frame)
    #         toolbar.update()
    #         toolbar.pack(fill=ctk.BOTH, expand=True)
    #         self.upload_spectrum_frame.pack(fill=ctk.BOTH, expand=True)

    # def uploadPlotOscilloscope(self):
    #     # self.hero.destroy()
    #     self.tabview.place_forget()
    #     for widget in self.upload_oscilloscope_frame.winfo_children():
    #         widget.destroy()

    #     oscilloscope_fig = self.recorder.plotOscilloscope()

    #     if oscilloscope_fig:
    #         canvas = FigureCanvasTkAgg(
    #             oscilloscope_fig, master=self.upload_oscilloscope_frame
    #         )
    #         canvas.draw()
    #         canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

    #         toolbar = NavigationToolbar2Tk(canvas, self.upload_oscilloscope_frame)
    #         toolbar.update()
    #         toolbar.pack(fill=ctk.BOTH, expand=True)

    #         self.upload_oscilloscope_frame.pack(fill=ctk.BOTH, expand=True)

    # def uploadWavFile(self):
    #     file_paths = filedialog.askopenfilenames(
    #         initialdir="../voice_recorder-main",
    #         filetypes=[("WAV files", "*.wav")],
    #         title="Select WAV files",
    #     )
    #     if len(file_paths) == 1:
    #         mb(
    #             title="Error",
    #             message="Please select two(2) WAV files.",
    #             icon="warning",
    #             option_1="OK",
    #         )
    #     elif len(file_paths) == 2:
    #         file1 = os.path.basename(file_paths[0])
    #         file2 = os.path.basename(file_paths[1])
    #         mb(
    #             title="Upload WAV",
    #             message=f"WAV Files {file1} and {file2} uploa*ded successfully.",
    #             icon="check",
    #             option_1="OK",
    #         )
    #         self.showPlotWAVFiles(filename1=file_paths[0], filename2=file_paths[1])
    #     else:
    #         mb(
    #             title="Error",
    #             message="Please select two(2) WAV files",
    #             icon="cancel",
    #             option_1="OK",
    #         )

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
        if self.gif_running:
            self.hero.configure(image=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.after(100, self.animateWave)

    def resetView(self):
        if self.tabview.winfo_exists():
            self.tabview.place_forget()
        # if self.upload_tab_view.winfo_exists():
        #     self.upload_tab_view.place_forget()
        self.gif_running = True

    def toggleThemeFrame(self):
        if self.is_theme_open:
            self.theme_frame.place_forget()
        else:
            self.theme_frame.place(relx=0.98, rely=0.16, anchor="ne")  # Show the frame

        self.is_theme_open = not self.is_theme_open

    def setAutumnTheme(self):
        self.theme.autumn()

    def setBreezeTheme(self):
        self.theme.breeze()

    def setDefaultTheme(self):
        self.theme.default()

    def setCarrotTheme(self):
        self.theme.carrot()

    def setCherryTheme(self):
        self.theme.cherry()

    def setCoffeeTheme(self):
        self.theme.coffee()

    def setLavenderTheme(self):
        self.theme.lavender()

    def setMarshTheme(self):
        self.theme.marsh()

    def setMetalTheme(self):
        self.theme.metal()

    def setMidnightTheme(self):
        self.theme.midnight()

    def setPatinaTheme(self):
        self.theme.patina()

    def setOrangeTheme(self):
        self.theme.orange()

    def setPinkTheme(self):
        self.theme.pink()

    def setRedTheme(self):
        self.theme.red()

    def setRimeTheme(self):
        self.theme.rime()

    def setRoseTheme(self):
        self.theme.rose()

    def setSkyTheme(self):
        self.theme.sky()

    def setVioletTheme(self):
        self.theme.violet()

    def setYellowTheme(self):
        self.theme.yellow()


root = ctk.CTk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = VoiceRecorderGUI(root)
root.mainloop()
