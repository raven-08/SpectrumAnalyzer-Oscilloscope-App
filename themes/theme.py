class Theme:
    def __init__(self, theme_button, dark_button, frame, theme_frame, record_btn1, record_btn2, plot_button, save_graph, tabview):
        self.theme_button = theme_button
        self.dark_button = dark_button
        self.frame = frame
        self.theme_frame = theme_frame
        self.record_btn1 = record_btn1
        self.record_btn2 = record_btn2
        self.plot_button = plot_button
        self.save_graph = save_graph
        self.tabview = tabview

    def autumn(self):
        self.theme_button.configure(
            fg_color=["#BF6F5F", "#9B4A3C"],
            hover_color=["#C8766D", "#A03E29"],
            text_color=["#F0E8E2", "#F0E8E2"],
            text_color_disabled=["#B08976", "#8D6E6E"],
            border_color=["#BF8F7C", "#6D4F4D"],
        )
        self.dark_button.configure(
            fg_color=["#BF6F5F", "#9B4A3C"],
            hover_color=["#C8766D", "#A03E29"],
            text_color=["#F0E8E2", "#F0E8E2"],
            text_color_disabled=["#B08976", "#8D6E6E"],
            border_color=["#BF8F7C", "#6D4F4D"],
        )
        self.record_btn1.configure(
            fg_color=["#BF6F5F", "#9B4A3C"],
            hover_color=["#C8766D", "#A03E29"],
            text_color=["#F0E8E2", "#F0E8E2"],
            text_color_disabled=["#B08976", "#8D6E6E"],
            border_color=["#BF8F7C", "#6D4F4D"],
        )
        self.record_btn2.configure(
            fg_color=["#BF6F5F", "#9B4A3C"],
            hover_color=["#C8766D", "#A03E29"],
            text_color=["#F0E8E2", "#F0E8E2"],
            text_color_disabled=["#B08976", "#8D6E6E"],
            border_color=["#BF8F7C", "#6D4F4D"],
        )
        self.plot_button.configure(
            fg_color=["#BF6F5F", "#9B4A3C"],
            hover_color=["#C8766D", "#A03E29"],
            text_color=["#F0E8E2", "#F0E8E2"],
            text_color_disabled=["#B08976", "#8D6E6E"],
            border_color=["#BF8F7C", "#6D4F4D"],
        )
        self.save_graph.configure(
            fg_color=["#BF6F5F", "#9B4A3C"],
            hover_color=["#C8766D", "#A03E29"],
            text_color=["#F0E8E2", "#F0E8E2"],
            text_color_disabled=["#B08976", "#8D6E6E"],
            border_color=["#BF8F7C", "#6D4F4D"],
        )
        self.tabview.configure(
            segmented_button_selected_color=["#BF6F5F", "#9B4A3C"],
            segmented_button_selected_hover_color=["#C8766D", "#A03E29"]
        )
        self.frame.configure(
            fg_color=["#E1C9B7", "#3F2F25"],
            border_color=["#A6806F", "#6D3F28"],
        )
        self.theme_frame.configure(fg_color=["#F5E5E1", "#3B2F2A"])

    def breeze(self):
        self.theme_button.configure(
            fg_color=["#4DB3C8", "#2D6D7D"],
            hover_color=["#4A9AB3", "#2B5B6D"],
            text_color=["#E1F2F6", "#E1F2F6"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#4D7A8D", "#9B9F9F"],
        )
        self.dark_button.configure(
            fg_color=["#4DB3C8", "#2D6D7D"],
            hover_color=["#4A9AB3", "#2B5B6D"],
            text_color=["#E1F2F6", "#E1F2F6"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#4D7A8D", "#9B9F9F"],
        )
        self.record_btn1.configure(
            fg_color=["#4DB3C8", "#2D6D7D"],
            hover_color=["#4A9AB3", "#2B5B6D"],
            text_color=["#E1F2F6", "#E1F2F6"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#4D7A8D", "#9B9F9F"],
        )
        self.record_btn2.configure(
            fg_color=["#4DB3C8", "#2D6D7D"],
            hover_color=["#4A9AB3", "#2B5B6D"],
            text_color=["#E1F2F6", "#E1F2F6"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#4D7A8D", "#9B9F9F"],
        )
        self.plot_button.configure(
            fg_color=["#4DB3C8", "#2D6D7D"],
            hover_color=["#4A9AB3", "#2B5B6D"],
            text_color=["#E1F2F6", "#E1F2F6"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#4D7A8D", "#9B9F9F"],
        )
        self.save_graph.configure(
            fg_color=["#4DB3C8", "#2D6D7D"],
            hover_color=["#4A9AB3", "#2B5B6D"],
            text_color=["#E1F2F6", "#E1F2F6"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#4D7A8D", "#9B9F9F"],
        )
        self.tabview.configure(
            segmented_button_selected_color=["#4DB3C8", "#2D6D7D"],
            segmented_button_selected_hover_color=["#4A9AB3", "#2B5B6D"],
        )
        self.frame.configure(
            fg_color=["#B4D9E7", "#1E3A46"],
            border_color=["#8AA1AE", "#2C4B5A"],
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])

    def carrot(self):
        self.theme_button.configure(
            fg_color=["#F76D57", "#D23016"],
            hover_color=["#E8624A", "#A31600"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#3E454A", "#949A9F"],
        )
        self.dark_button.configure(
            fg_color=["#F76D57", "#D23016"],
            hover_color=["#E8624A", "#A31600"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#3E454A", "#949A9F"],
        )
        self.record_btn1.configure(
            fg_color=["#F76D57", "#D23016"],
            hover_color=["#E8624A", "#A31600"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#3E454A", "#949A9F"],
        )
        self.record_btn2.configure(
            fg_color=["#F76D57", "#D23016"],
            hover_color=["#E8624A", "#A31600"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#3E454A", "#949A9F"],
        )
        self.plot_button.configure(
            fg_color=["#F76D57", "#D23016"],
            hover_color=["#E8624A", "#A31600"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#3E454A", "#949A9F"],
        )
        self.save_graph.configure(
            fg_color=["#F76D57", "#D23016"],
            hover_color=["#E8624A", "#A31600"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
            border_color=["#3E454A", "#949A9F"],
        )
        self.frame.configure(
            fg_color=["#FFC5A1", "#D95136"],
            border_color=["#C7745B", "#8C1C00"],
        )
        self.tabview.configure(
            segmented_button_selected_color=["#F76D57", "#D23016"],
            segmented_button_selected_hover_color=["#E8624A", "#A31600"]
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])

    def cherry(self):
        self.theme_button.configure(
            fg_color=["#F5B3B3", "#C85C5C"],
            hover_color=["#F29C9C", "#BF3E3E"],
            text_color=["#FDF5F5", "#FDF5F5"],
            text_color_disabled=["#D8A7A2", "#B68D8D"],
            border_color=["#C6A6A5", "#6F3D4B"],
        )
        self.dark_button.configure(
            fg_color=["#F5B3B3", "#C85C5C"],
            hover_color=["#F29C9C", "#BF3E3E"],
            text_color=["#FDF5F5", "#FDF5F5"],
            text_color_disabled=["#D8A7A2", "#B68D8D"],
            border_color=["#C6A6A5", "#6F3D4B"],
        )
        self.record_btn1.configure(
            fg_color=["#F5B3B3", "#C85C5C"],
            hover_color=["#F29C9C", "#BF3E3E"],
            text_color=["#FDF5F5", "#FDF5F5"],
            text_color_disabled=["#D8A7A2", "#B68D8D"],
            border_color=["#C6A6A5", "#6F3D4B"],
        )
        self.record_btn2.configure(
            fg_color=["#F5B3B3", "#C85C5C"],
            hover_color=["#F29C9C", "#BF3E3E"],
            text_color=["#FDF5F5", "#FDF5F5"],
            text_color_disabled=["#D8A7A2", "#B68D8D"],
            border_color=["#C6A6A5", "#6F3D4B"],
        )
        self.plot_button.configure(
            fg_color=["#F5B3B3", "#C85C5C"],
            hover_color=["#F29C9C", "#BF3E3E"],
            text_color=["#FDF5F5", "#FDF5F5"],
            text_color_disabled=["#D8A7A2", "#B68D8D"],
            border_color=["#C6A6A5", "#6F3D4B"],
        )
        self.save_graph.configure(
            fg_color=["#F5B3B3", "#C85C5C"],
            hover_color=["#F29C9C", "#BF3E3E"],
            text_color=["#FDF5F5", "#FDF5F5"],
            text_color_disabled=["#D8A7A2", "#B68D8D"],
            border_color=["#C6A6A5", "#6F3D4B"],
        )
        self.tabview.configure(
            segmented_button_selected_color=["#F5B3B3", "#C85C5C"],
            segmented_button_selected_hover_color=["#F29C9C", "#BF3E3E"],
        )
        self.frame.configure(
            fg_color=["#FFF1EA", "#5D3A4A"],
            border_color=["#C6A6A5", "#6F3D4B"],
        )
        self.theme_frame.configure(fg_color=["#FBE8E6", "#6D4C6C"])

    def coffee(self):
        self.theme_button.configure(
            fg_color=["#825C46", "#5A3E32"],
            hover_color=["#6F4C37", "#4B3126"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["#A89B89", "#8E7D72"],
        )
        self.dark_button.configure(
            fg_color=["#825C46", "#5A3E32"],
            hover_color=["#6F4C37", "#4B3126"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["#A89B89", "#8E7D72"],
        )
        self.record_btn1.configure(
            fg_color=["#825C46", "#5A3E32"],
            hover_color=["#6F4C37", "#4B3126"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["#A89B89", "#8E7D72"],
        )
        self.record_btn2.configure(
            fg_color=["#825C46", "#5A3E32"],
            hover_color=["#6F4C37", "#4B3126"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["#A89B89", "#8E7D72"],
        )
        self.plot_button.configure(
            fg_color=["#825C46", "#5A3E32"],
            hover_color=["#6F4C37", "#4B3126"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["#A89B89", "#8E7D72"],
        )
        self.save_graph.configure(
            fg_color=["#825C46", "#5A3E32"],
            hover_color=["#6F4C37", "#4B3126"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["#A89B89", "#8E7D72"],
        )
        self.tabview.configure(
            segmented_button_selected_color=["#825C46", "#5A3E32"],
            segmented_button_selected_hover_color=["#6F4C37", "#4B3126"]
        )
        self.frame.configure(
            fg_color=["#D8C0A0", "#725B4E"],
            border_color=["#A3886F", "#8B746A"],
        )
        self.theme_frame.configure(fg_color=["#E8D1B3", "#6D5143"])

    def lavender(self):
        self.theme_button.configure(
            fg_color=["#B19CD9", "#9370DB"],
            hover_color=["#9370DB", "#7A5DC7"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.dark_button.configure(
            fg_color=["#B19CD9", "#9370DB"],
            hover_color=["#9370DB", "#7A5DC7"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.record_btn1.configure(
            fg_color=["#B19CD9", "#9370DB"],
            hover_color=["#9370DB", "#7A5DC7"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.record_btn2.configure(
            fg_color=["#B19CD9", "#9370DB"],
            hover_color=["#9370DB", "#7A5DC7"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
        )
        
        self.plot_button.configure(
            fg_color=["#B19CD9", "#9370DB"],
            hover_color=["#9370DB", "#7A5DC7"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
        )
        
        self.save_graph.configure(
            fg_color=["#B19CD9", "#9370DB"],
            hover_color=["#9370DB", "#7A5DC7"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#DCE4EE", "#DCE4EE"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.tabview.configure(
            segmented_button_selected_color=["#B19CD9", "#9370DB"],
            segmented_button_selected_hover_color=["#9370DB", "#7A5DC7"]
        )
        
        self.frame.configure(
            fg_color=["#9370DB", "#B19CD9"],
            border_color=["#3E454A", "#949A9F"],
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])

    def marsh(self):
        self.theme_button.configure(
            fg_color=["#7DBE98", "#4E8F69"],
            hover_color=["#6EAA8C", "#397F5A"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#F0F8ED", "#F0F8ED"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.dark_button.configure(
            fg_color=["#7DBE98", "#4E8F69"],
            hover_color=["#6EAA8C", "#397F5A"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#F0F8ED", "#F0F8ED"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.record_btn1.configure(
            fg_color=["#7DBE98", "#4E8F69"],
            hover_color=["#6EAA8C", "#397F5A"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#F0F8ED", "#F0F8ED"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.record_btn2.configure(
            fg_color=["#7DBE98", "#4E8F69"],
            hover_color=["#6EAA8C", "#397F5A"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#F0F8ED", "#F0F8ED"],
            text_color_disabled=["gray74", "gray60"],
        )
      
        self.plot_button.configure(
            fg_color=["#7DBE98", "#4E8F69"],
            hover_color=["#6EAA8C", "#397F5A"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#F0F8ED", "#F0F8ED"],
            text_color_disabled=["gray74", "gray60"],
        )
       
        self.save_graph.configure(
            fg_color=["#7DBE98", "#4E8F69"],
            hover_color=["#6EAA8C", "#397F5A"],
            border_color=["#3E454A", "#949A9F"],
            text_color=["#F0F8ED", "#F0F8ED"],
            text_color_disabled=["gray74", "gray60"],
        )
        self.tabview.configure(
            segmented_button_selected_color=["#7DBE98", "#4E8F69"],
            segmented_button_selected_hover_color=["#6EAA8C", "#397F5A"]
        )
       
        self.frame.configure(
            fg_color=["#B0C9A0", "#4F5F4A"],
            border_color=["#8A9E72", "gray28"],
        )
        self.theme_frame.configure(fg_color=["#B0C9A0", "gray14"])

    def metal(self):
        self.theme_button.configure(
            fg_color= ["#A0A0A0", "#505050"],
            hover_color= ["#909090", "#606060"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#F0F0F0", "#F0F0F0"],
            text_color_disabled= ["#C0C0C0", "#808080"]
        )
        self.dark_button.configure(
            fg_color= ["#A0A0A0", "#505050"],
            hover_color= ["#909090", "#606060"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#F0F0F0", "#F0F0F0"],
            text_color_disabled= ["#C0C0C0", "#808080"]
        )
        self.record_btn1.configure(
            fg_color= ["#A0A0A0", "#505050"],
            hover_color= ["#909090", "#606060"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#F0F0F0", "#F0F0F0"],
            text_color_disabled= ["#C0C0C0", "#808080"]
        )
        self.record_btn2.configure(
            fg_color= ["#A0A0A0", "#505050"],
            hover_color= ["#909090", "#606060"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#F0F0F0", "#F0F0F0"],
            text_color_disabled= ["#C0C0C0", "#808080"]
        )
       
        self.plot_button.configure(
            fg_color= ["#A0A0A0", "#505050"],
            hover_color= ["#909090", "#606060"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#F0F0F0", "#F0F0F0"],
            text_color_disabled= ["#C0C0C0", "#808080"]
        )
       
        self.save_graph.configure(
            fg_color= ["#A0A0A0", "#505050"],
            hover_color= ["#909090", "#606060"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#F0F0F0", "#F0F0F0"],
            text_color_disabled= ["#C0C0C0", "#808080"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#A0A0A0", "#505050"],
            segmented_button_selected_hover_color=["#909090", "#606060"]
        )
        
        self.frame.configure(
            fg_color=["#C0C0C0", "#404040"],
            border_color=["#808080", "#606060"],
        )
        self.theme_frame.configure(fg_color=["#E0E0E0", "#363636"])
        
    def midnight(self):
        self.theme_button.configure(
            fg_color= ["#003F6C", "#002E5D"],
            hover_color= ["#004080", "#00214B"],
            border_color= ["#003D4E", "#7F8C8D"],
            text_color= ["#E5E9F0", "#E5E9F0"],
            text_color_disabled= ["#C0C6CE", "#A6A9AE"]
        )
        self.dark_button.configure(
            fg_color= ["#003F6C", "#002E5D"],
            hover_color= ["#004080", "#00214B"],
            border_color= ["#003D4E", "#7F8C8D"],
            text_color= ["#E5E9F0", "#E5E9F0"],
            text_color_disabled= ["#C0C6CE", "#A6A9AE"]
        )
        self.record_btn1.configure(
            fg_color= ["#003F6C", "#002E5D"],
            hover_color= ["#004080", "#00214B"],
            border_color= ["#003D4E", "#7F8C8D"],
            text_color= ["#E5E9F0", "#E5E9F0"],
            text_color_disabled= ["#C0C6CE", "#A6A9AE"]
        )
        self.record_btn2.configure(
            fg_color= ["#003F6C", "#002E5D"],
            hover_color= ["#004080", "#00214B"],
            border_color= ["#003D4E", "#7F8C8D"],
            text_color= ["#E5E9F0", "#E5E9F0"],
            text_color_disabled= ["#C0C6CE", "#A6A9AE"]
        )
        
        self.plot_button.configure(
            fg_color= ["#003F6C", "#002E5D"],
            hover_color= ["#004080", "#00214B"],
            border_color= ["#003D4E", "#7F8C8D"],
            text_color= ["#E5E9F0", "#E5E9F0"],
            text_color_disabled= ["#C0C6CE", "#A6A9AE"]
        )
       
        self.save_graph.configure(
            fg_color= ["#003F6C", "#002E5D"],
            hover_color= ["#004080", "#00214B"],
            border_color= ["#003D4E", "#7F8C8D"],
            text_color= ["#E5E9F0", "#E5E9F0"],
            text_color_disabled= ["#C0C6CE", "#A6A9AE"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#003F6C", "#002E5D"],
            segmented_button_selected_hover_color=["#004080", "#00214B"]
        )
        self.frame.configure(
            fg_color= ["#BCC6D0", "#434E5A"],
            border_color= ["#5A5C66", "#003B6C"],
        )
        self.theme_frame.configure(fg_color=["#DCE4EE", "#001F3F"])
    
    def patina(self):
        self.theme_button.configure(
            fg_color= ["#B57A4C", "#6F4C3B"],
            hover_color= ["#A9643A", "#5C3A24"],
            border_color= ["#9B5D3A", "#3E2D1F"],
            text_color= ["#F5F2E6", "#F5EDE6"],
            text_color_disabled= ["#C4A97B", "#9B8C6D"]
        )
        self.dark_button.configure(
            fg_color= ["#B57A4C", "#6F4C3B"],
            hover_color= ["#A9643A", "#5C3A24"],
            border_color= ["#9B5D3A", "#3E2D1F"],
            text_color= ["#F5F2E6", "#F5EDE6"],
            text_color_disabled= ["#C4A97B", "#9B8C6D"]
        )
        self.record_btn1.configure(
            fg_color= ["#B57A4C", "#6F4C3B"],
            hover_color= ["#A9643A", "#5C3A24"],
            border_color= ["#9B5D3A", "#3E2D1F"],
            text_color= ["#F5F2E6", "#F5EDE6"],
            text_color_disabled= ["#C4A97B", "#9B8C6D"]
        )
        self.record_btn2.configure(
            fg_color= ["#B57A4C", "#6F4C3B"],
            hover_color= ["#A9643A", "#5C3A24"],
            border_color= ["#9B5D3A", "#3E2D1F"],
            text_color= ["#F5F2E6", "#F5EDE6"],
            text_color_disabled= ["#C4A97B", "#9B8C6D"]
        )
      
        self.plot_button.configure(
            fg_color= ["#B57A4C", "#6F4C3B"],
            hover_color= ["#A9643A", "#5C3A24"],
            border_color= ["#9B5D3A", "#3E2D1F"],
            text_color= ["#F5F2E6", "#F5EDE6"],
            text_color_disabled= ["#C4A97B", "#9B8C6D"]
        )
        self.save_graph.configure(
            fg_color= ["#B57A4C", "#6F4C3B"],
            hover_color= ["#A9643A", "#5C3A24"],
            border_color= ["#9B5D3A", "#3E2D1F"],
            text_color= ["#F5F2E6", "#F5EDE6"],
            text_color_disabled= ["#C4A97B", "#9B8C6D"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#B57A4C", "#6F4C3B"],
            segmented_button_selected_hover_color=["#A9643A", "#5C3A24"]
        )
      
        self.frame.configure(
            fg_color= ["#CAAFA4", "#AC968D"],
            border_color= ["#A67C5F", "#926E54"]
        )
        self.theme_frame.configure(fg_color=["#DAB396", "#D1A482"])
    
    def orange(self):
        self.theme_button.configure(
            fg_color= ["#FF8C42", "#FF6505"],
            hover_color= ["#E67320", "#CC5500"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.dark_button.configure(
            fg_color= ["#FF8C42", "#FF6505"],
            hover_color= ["#E67320", "#CC5500"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn1.configure(
            fg_color= ["#FF8C42", "#FF6505"],
            hover_color= ["#E67320", "#CC5500"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn2.configure(
            fg_color= ["#FF8C42", "#FF6505"],
            hover_color= ["#E67320", "#CC5500"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
      
        self.plot_button.configure(
            fg_color= ["#FF8C42", "#FF6505"],
            hover_color= ["#E67320", "#CC5500"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        
        self.save_graph.configure(
            fg_color= ["#FF8C42", "#FF6505"],
            hover_color= ["#E67320", "#CC5500"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#FF8C42", "#FF6505"],
            segmented_button_selected_hover_color=["#E67320", "#CC5500"]
        )
       
        self.frame.configure(
            fg_color= ["#FF6505", "#FF8C42"],
            border_color= ["gray65", "gray28"]
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])
        
    def pink(self):
        self.theme_button.configure(
            fg_color= ["#FF6B6B", "#B74177"],
            hover_color= ["#FF4E4E", "#A01E5C"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.dark_button.configure(
            fg_color= ["#FF6B6B", "#B74177"],
            hover_color= ["#FF4E4E", "#A01E5C"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn1.configure(
            fg_color= ["#FF6B6B", "#B74177"],
            hover_color= ["#FF4E4E", "#A01E5C"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn2.configure(
            fg_color= ["#FF6B6B", "#B74177"],
            hover_color= ["#FF4E4E", "#A01E5C"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        
        self.plot_button.configure(
            fg_color= ["#FF6B6B", "#B74177"],
            hover_color= ["#FF4E4E", "#A01E5C"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
       
        self.save_graph.configure(
            fg_color= ["#FF6B6B", "#B74177"],
            hover_color= ["#FF4E4E", "#A01E5C"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#FF6B6B", "#B74177"],
            segmented_button_selected_hover_color=["#FF4E4E", "#A01E5C"]
        )
        
        self.frame.configure(
            fg_color= ["#B74177", "#FF6B6B"],
            border_color= ["gray65", "gray28"]
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])
    
    def red(self):
        self.theme_button.configure(
            fg_color= ["#D03434", "#A11D1D"],
            hover_color= ["#B22E2E", "#791414"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.dark_button.configure(
            fg_color= ["#D03434", "#A11D1D"],
            hover_color= ["#B22E2E", "#791414"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn1.configure(
            fg_color= ["#D03434", "#A11D1D"],
            hover_color= ["#B22E2E", "#791414"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn2.configure(
            fg_color= ["#D03434", "#A11D1D"],
            hover_color= ["#B22E2E", "#791414"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        
        self.plot_button.configure(
            fg_color= ["#D03434", "#A11D1D"],
            hover_color= ["#B22E2E", "#791414"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        
        self.save_graph.configure(
            fg_color= ["#D03434", "#A11D1D"],
            hover_color= ["#B22E2E", "#791414"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#D03434", "#A11D1D"],
            segmented_button_selected_hover_color=["#B22E2E", "#791414"]
        )
      
        self.frame.configure(
            fg_color= ["#A11D1D", "#D03434"],
            border_color= ["gray65", "gray28"]
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])
    
    def rime(self):
        self.theme_button.configure(
            fg_color= ["#6E8BA4", "#4A5D6B"],
            hover_color= ["#5F7A8E", "#3A4A54"],
            border_color= ["#6C7B82", "#9D9F9F"],
            text_color= ["#F2F7FC", "#F2F7FC"],
            text_color_disabled= ["#B4BCC1", "#A8A8A8"]
        )
        self.dark_button.configure(
            fg_color= ["#6E8BA4", "#4A5D6B"],
            hover_color= ["#5F7A8E", "#3A4A54"],
            border_color= ["#6C7B82", "#9D9F9F"],
            text_color= ["#F2F7FC", "#F2F7FC"],
            text_color_disabled= ["#B4BCC1", "#A8A8A8"]
        )
        self.record_btn1.configure(
            fg_color= ["#6E8BA4", "#4A5D6B"],
            hover_color= ["#5F7A8E", "#3A4A54"],
            border_color= ["#6C7B82", "#9D9F9F"],
            text_color= ["#F2F7FC", "#F2F7FC"],
            text_color_disabled= ["#B4BCC1", "#A8A8A8"]
        )
        self.record_btn2.configure(
            fg_color= ["#6E8BA4", "#4A5D6B"],
            hover_color= ["#5F7A8E", "#3A4A54"],
            border_color= ["#6C7B82", "#9D9F9F"],
            text_color= ["#F2F7FC", "#F2F7FC"],
            text_color_disabled= ["#B4BCC1", "#A8A8A8"]
        )
        self.plot_button.configure(
            fg_color= ["#6E8BA4", "#4A5D6B"],
            hover_color= ["#5F7A8E", "#3A4A54"],
            border_color= ["#6C7B82", "#9D9F9F"],
            text_color= ["#F2F7FC", "#F2F7FC"],
            text_color_disabled= ["#B4BCC1", "#A8A8A8"]
        )
        
        self.save_graph.configure(
            fg_color= ["#6E8BA4", "#4A5D6B"],
            hover_color= ["#5F7A8E", "#3A4A54"],
            border_color= ["#6C7B82", "#9D9F9F"],
            text_color= ["#F2F7FC", "#F2F7FC"],
            text_color_disabled= ["#B4BCC1", "#A8A8A8"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#6E8BA4", "#4A5D6B"],
            segmented_button_selected_hover_color=["#5F7A8E", "#3A4A54"]
        )
        
        self.frame.configure(
            fg_color= ["#C0C8CE", "#2D2F33"],
            border_color= ["gray65", "gray28"]
        )
        self.theme_frame.configure(fg_color=["#E0E6E9", "#2B2D2F"])
    
    def rose(self):
        self.theme_button.configure(
            fg_color= ["#a85475", "#6c1f2b"],
            hover_color= ["#98415f", "#5c0f0b"],
            border_color= ["#8b3c49", "#b7707d"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.dark_button.configure(
            fg_color= ["#a85475", "#6c1f2b"],
            hover_color= ["#98415f", "#5c0f0b"],
            border_color= ["#8b3c49", "#b7707d"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn1.configure(
            fg_color= ["#a85475", "#6c1f2b"],
            hover_color= ["#98415f", "#5c0f0b"],
            border_color= ["#8b3c49", "#b7707d"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn2.configure(
            fg_color= ["#a85475", "#6c1f2b"],
            hover_color= ["#98415f", "#5c0f0b"],
            border_color= ["#8b3c49", "#b7707d"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
       
        self.plot_button.configure(
            fg_color= ["#a85475", "#6c1f2b"],
            hover_color= ["#98415f", "#5c0f0b"],
            border_color= ["#8b3c49", "#b7707d"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
       
        self.save_graph.configure(
            fg_color= ["#a85475", "#6c1f2b"],
            hover_color= ["#98415f", "#5c0f0b"],
            border_color= ["#8b3c49", "#b7707d"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#a85475", "#6c1f2b"],
            segmented_button_selected_hover_color=["#98415f", "#5c0f0b"]
        )
        
        self.frame.configure(
            fg_color= ["#ffc0cb", "#985475"],
            border_color= ["#cb8bb2", "#7c3847"]
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])
    
    def sky(self):
        self.theme_button.configure(
            fg_color= ["#27577D", "#BBD1E4"],
            hover_color= ["#000099", "#9999ff"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.dark_button.configure(
            fg_color= ["#27577D", "#BBD1E4"],
            hover_color= ["#000099", "#9999ff"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn1.configure(
            fg_color= ["#27577D", "#BBD1E4"],
            hover_color= ["#000099", "#9999ff"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn2.configure(
            fg_color= ["#27577D", "#BBD1E4"],
            hover_color= ["#000099", "#9999ff"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
     
        self.plot_button.configure(
            fg_color= ["#27577D", "#BBD1E4"],
            hover_color= ["#000099", "#9999ff"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
      
        self.save_graph.configure(
            fg_color= ["#27577D", "#BBD1E4"],
            hover_color= ["#000099", "#9999ff"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#27577D", "#BBD1E4"],
            segmented_button_selected_hover_color=["#000099", "#9999ff"]
        )
        
        self.frame.configure(
            fg_color= ["#BBD1E4", "#27577D"],
            border_color= ["#8EADC4", "#36719F"]
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])
        
    def violet(self):
        self.theme_button.configure(
            fg_color= ["#7C63A6", "#402E5C"],
            hover_color= ["#6C5090", "#301E3C"],
            border_color= ["#5F4B7A", "#8B7FAE"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.dark_button.configure(
            fg_color= ["#7C63A6", "#402E5C"],
            hover_color= ["#6C5090", "#301E3C"],
            border_color= ["#5F4B7A", "#8B7FAE"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn1.configure(
            fg_color= ["#7C63A6", "#402E5C"],
            hover_color= ["#6C5090", "#301E3C"],
            border_color= ["#5F4B7A", "#8B7FAE"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn2.configure(
            fg_color= ["#7C63A6", "#402E5C"],
            hover_color= ["#6C5090", "#301E3C"],
            border_color= ["#5F4B7A", "#8B7FAE"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.plot_button.configure(
            fg_color= ["#7C63A6", "#402E5C"],
            hover_color= ["#6C5090", "#301E3C"],
            border_color= ["#5F4B7A", "#8B7FAE"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
        
        self.save_graph.configure(
            fg_color= ["#7C63A6", "#402E5C"],
            hover_color= ["#6C5090", "#301E3C"],
            border_color= ["#5F4B7A", "#8B7FAE"],
            text_color= ["#F3EFFF", "#F3EFFF"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#7C63A6", "#402E5C"],
            segmented_button_selected_hover_color= ["#6C5090", "#301E3C"]
        )
       
        self.frame.configure(
            fg_color= ["#D3CFFC", "#6C63A6"],
            border_color= ["#9F9AE3", "#504778"]
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])
        
    def yellow(self):
        self.theme_button.configure(
            fg_color= ["#FFA500", "#FF8C00"],
            hover_color= ["#FF8C00", "#FF6600"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.dark_button.configure(
            fg_color= ["#FFA500", "#FF8C00"],
            hover_color= ["#FF8C00", "#FF6600"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn1.configure(
            fg_color= ["#FFA500", "#FF8C00"],
            hover_color= ["#FF8C00", "#FF6600"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.record_btn2.configure(
            fg_color= ["#FFA500", "#FF8C00"],
            hover_color= ["#FF8C00", "#FF6600"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        
        self.plot_button.configure(
            fg_color= ["#FFA500", "#FF8C00"],
            hover_color= ["#FF8C00", "#FF6600"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
       
        self.save_graph.configure(
            fg_color= ["#FFA500", "#FF8C00"],
            hover_color= ["#FF8C00", "#FF6600"],
            border_color= ["#3E454A", "#949A9F"],
            text_color= ["#DCE4EE", "#DCE4EE"],
            text_color_disabled= ["gray74", "gray60"]
        )
        self.tabview.configure(
            segmented_button_selected_color=["#FFA500", "#FF8C00"],
            segmented_button_selected_hover_color= ["#FF8C00", "#FF6600"]
        )
    
        self.frame.configure(
            fg_color= ["#FF8C00", "#FFA500"],
            border_color= ["gray65", "gray28"]
        )
        self.theme_frame.configure(fg_color=["gray92", "gray14"])