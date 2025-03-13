# def plotWavFile(self, filename):
#     self.hero.destroy()
#     self.tabview.place_forget()
#     for widget in self.plot_frame.winfo_children():
#         widget.destroy()

#     figure = self.recorder.readAndPlotWAV(filename)

#     if figure:
#         canvas = FigureCanvasTkAgg(figure, master=self.plot_frame)
#         canvas.draw()
#         canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

#         toolbar = NavigationToolbar2Tk(canvas, self.plot_frame)
#         toolbar.update()
#         toolbar.pack(fill=ctk.BOTH, expand=True)
#         self.plot_frame.pack(fill=ctk.BOTH, expand=True)
