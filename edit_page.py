import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

from styling import tkinter_styles_

def setup_label_frames(self):

	self.main_frame = LabelFrame(self.top,text="Details:")
	self.main_frame.grid(row=2, column=0, columnspan = 8, rowspan = 2,sticky='NSEW',padx=5, pady=5, ipadx=2, ipady=5)
	

def setup_widgets():
	def wrapper(widgets_func):
		def wrapped_function(self, widgets):
			
			#Title
			self.title_entry = tk.Entry(self.main_frame)
			widgets.append(self.title_entry)
			
			widgets_func(self, widgets)
			
			#Add Widgets to page
			tkinter_styles_.add_widgets(widgets)
			
			tkinter_styles_.setup_ok_cancel_btns(self.top, self, row=4, column=6)
		
		return wrapped_function
	return wrapper
	
	
def check_user_input():
	def wrapper(check_func):
		def wrapped_function(self, title_checker):
			
			#Title
			status_text = None
			msg = title_checker(self.title_entry.get())		
			
			if not msg:
				msg = check_func(self, title_checker)
				status_text = self.mainapp.status_box.gen_status_text(self.mode, self.title_entry.get())
				
			return msg, status_text
		
		return wrapped_function
	return wrapper