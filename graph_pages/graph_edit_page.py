import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.messagebox

from styling import tkinter_styles_
import edit_page


def setup_label_frames(self):

	self.main_frame = LabelFrame(self.top,text="Details:")
	self.main_frame.grid(row=2, column=0, columnspan = 8, rowspan = 2,sticky='NSEW',padx=5, pady=5, ipadx=2, ipady=5)
	
def setup_widgets(self):

	# Setup Labels
	labels = ['Title:']
	tkinter_styles_.setup_labels(labels, self.main_frame, width=10)

	#Setup Input Widgets
	widgets = []
	
	# Title
	self.title_entry = Entry(self.main_frame)
	widgets.append(self.title_entry)

	#Add Widgets to page
	tkinter_styles_.add_widgets(widgets)
	
	tkinter_styles_.setup_ok_cancel_btns(self.top, self, row=4, column=6)
		

def get_user_input(self):

	self.title = self.title_entry.get()
	
def check_user_input(self, title_checker):
	
	msg = None
	
	msg = self.mainapp.sidebar_tree.check_title(self.title_entry.get())
	
	return msg
	
def setup_page(self):

	setup_label_frames(self)
	setup_widgets(self)