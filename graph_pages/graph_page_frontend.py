



def update_label_text(self):
	self.top_label = tk.Label(self, text=(f'Graph: {self.backend.title}'),font=self.mainapp.title_font, anchor="w")
	#self.top_label.pack(fill=tk.BOTH, expand=True)
	self.top_label.pack()
	

	