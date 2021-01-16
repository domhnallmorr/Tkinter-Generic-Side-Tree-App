import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.messagebox

#import sys
#sys.path.append('..\\styling')
#from styling import tkinter_styles_
#from data_pages import data_page_backend



# class DataPage(tk.Frame):

	# def __init__(self, container, mainapp, backend):
		
		# self.mainapp = mainapp
		
		# self.backend = backend
		
		# self.update_component()
	
def update_component(self):
	pass
	#self.update_label_text()
	#self.assign_treeview_node()
	

def update_label_text(self):
	self.top_label = tk.Label(self, text=(f'Data: {self.backend.title}'),font=self.mainapp.title_font, anchor="w")
	#self.top_label.pack(fill=tk.BOTH, expand=True)

		
		
class EditDataPage(object):
	def __init__(self, mainapp, master, mode, parent_page):
		#self.drawing_dictionary = drawing_dictionary
		self.top = Toplevel(master)
		self.top.grab_set()
		self.mainapp = mainapp
		self.mode = mode
		self.parent_page = parent_page
		
		self.setup_label_frames()
		self.setup_widgets()
		
	def setup_label_frames(self):
	
		self.main_frame = LabelFrame(self.top,text="Details:")
		self.main_frame.grid(row=2, column=0, columnspan = 8, rowspan = 2,sticky='NSEW',padx=5, pady=5, ipadx=2, ipady=5)	
		
	def setup_widgets(self):
		
		# Setup Labels
		labels = ['Title:', 'Data Type:', 'Month:', 'Year:', 'Input file:']
		tkinter_styles_.setup_labels(labels, self.main_frame, width=10)
		
		#Setup Input Widgets
		widgets = []
		
		#Title
		self.title_entry = Entry(self.main_frame)
		widgets.append(self.title_entry)
		
		#Data Type
		self.data_type_combo = ttk.Combobox(self.main_frame, values=['Temperature', 'Rainfall'], state='readonly')
		self.data_type_combo.set('Temperature')
		widgets.append(self.data_type_combo)
		
		#Month
		self.month_combo = ttk.Combobox(self.main_frame, values=['January', 'February', 'March'], state='readonly')
		widgets.append(self.month_combo)
		
		#Year
		self.year_combo = ttk.Combobox(self.main_frame, values=['2018', '2019', '2020', '2021'], state='readonly')
		widgets.append(self.year_combo)
		
		#Input File
		self.input_file_entry = Entry(self.main_frame, width=50)
		widgets.append(self.input_file_entry)

		#Add Widgets to page
		tkinter_styles_.add_widgets(widgets)
		
		tkinter_styles_.setup_ok_cancel_btns(self.top, self, row=4, column=6)
		
	def check_user_input(self):
	
		msg = self.mainapp.sidebar_tree.check_title(self.title_entry.get())
		
		if msg:
			tkinter.messagebox.showerror(master=self.top, title='Error', message=msg)
			
		return msg

	def get_user_input(self):
		
		self.title = self.title_entry.get()
		self.data_type = self.data_type_combo.get()
		self.month = self.month_combo.get()
		self.year = self.year_combo.get()
		self.input_file = self.input_file_entry.get()
				
	def cleanup(self, button):
		
		self.button = button
		
		if button == 'cancel': #close the window
			self.top.destroy()
			
		else: #handle user clicking ok
			
			msg = self.check_user_input()
			
			if not msg:
				
				#get input data
				self.get_user_input()
				
				#close the window
				self.top.destroy()