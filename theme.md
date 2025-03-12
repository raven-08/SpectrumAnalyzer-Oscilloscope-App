









        # Theme Buttons
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
        self.lavender.place(relx=0.2, rely=0.21, anchor="n")
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
        self.marsh.place(relx=0.4, rely=0.21, anchor="n")
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
        self.metal.place(relx=0.6, rely=0.21, anchor="n")
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
        self.midnight.place(relx=0.8, rely=0.21, anchor="n")
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
        self.patina.place(relx=0.2, rely=0.31, anchor="n")
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
        self.orange.place(relx=0.4, rely=0.31, anchor="n")
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
        self.pink.place(relx=0.6, rely=0.31, anchor="n")
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
        self.red.place(relx=0.8, rely=0.31, anchor="n")
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
        self.rime.place(relx=0.2, rely=0.41, anchor="n")
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
        self.rose.place(relx=0.4, rely=0.41, anchor="n")
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
        self.sky.place(relx=0.6, rely=0.41, anchor="n")
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
        self.violet.place(relx=0.8, rely=0.41, anchor="n")
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
        self.yellow.place(relx=0.2, rely=0.51, anchor="n")
        self.theme = Theme(
            self.theme_button, self.dark_button, self.frame, self.theme_frame
        )















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
