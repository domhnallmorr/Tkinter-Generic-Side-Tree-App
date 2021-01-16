import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

class StatusBox(tk.Frame):
	def __init__(self, mainapp):
		tk.Frame.__init__(self)
		
		self.mainapp = mainapp
		
		self.text_box = tk.Text(self, height = 10, bg='grey89', font = mainapp.status_font)
		self.text_box.pack(fill=tk.BOTH, expand=True)
		self.text_box.insert("1.0", 'Starting App')
		self.text_box.config(state='disabled')
		
	def gen_status_text(self, mode, title):
	
		if mode == 'new':
			status_text = self.new_component_text(title)
			
		return status_text
		
	def new_component_text(self, title):
	
		return f'Created Component {title}'
		
		
	def add_text(self, status_text):
		
		if status_text != None:
			self.text_box.config(state='normal')
			print(status_text)
			self.text_box.insert(END, '\n')
			self.text_box.insert(END, status_text)
			self.text_box.config(state='disabled')
	