import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.messagebox
import os

from styling import tkinter_styles_
import edit_page


def setup_label_frames(self):

	self.main_frame = LabelFrame(self.top,text="Details:")
	self.main_frame.grid(row=2, column=0, columnspan = 8, rowspan = 2,sticky='NSEW',padx=5, pady=5, ipadx=2, ipady=5)	

@edit_page.setup_widgets()
def setup_widgets(self, widgets):
	
	# Setup Labels
	labels = ['Title:', 'Data Type:', 'Month:', 'Year:', 'Input file:']
	tkinter_styles_.setup_labels(labels, self.main_frame, width=10)
	
	#Data Type
	self.data_type_combo = ttk.Combobox(self.main_frame, values=['Temperature', 'Rainfall'], state='readonly')
	self.data_type_combo.set('Temperature')
	widgets.append(self.data_type_combo)
	
	#Month
	self.month_combo = ttk.Combobox(self.main_frame, values=['January', 'February', 'March'], state='readonly')
	self.month_combo.set('January')
	widgets.append(self.month_combo)
	
	#Year
	self.year_combo = ttk.Combobox(self.main_frame, values=['2018', '2019', '2020', '2021'], state='readonly')
	self.year_combo.set('2018')
	widgets.append(self.year_combo)
	
	#Input File
	self.input_file_entry = Entry(self.main_frame, width=50)
	widgets.append(self.input_file_entry)


@edit_page.check_user_input()
def check_user_input(self, title_checker):
	
	msg = None
	
	#Check input file exists
	if not os.path.isfile(self.input_file_entry.get()):
		msg = 'Input File Does Not Exist'
	
	return msg

def get_user_input(self):
	
	self.title = self.title_entry.get()
	self.data_type = self.data_type_combo.get()
	self.month = self.month_combo.get()
	self.year = self.year_combo.get()
	self.input_file = self.input_file_entry.get()
	
def setup_page(self, widgets):

	setup_label_frames(self)
	setup_widgets(self, widgets)
