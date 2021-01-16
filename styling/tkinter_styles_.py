from tkinter import font as tkfont
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


def setup_fonts(mainapp):

	mainapp.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
	mainapp.title_font.configure(underline=True)
	
	mainapp.status_font = tkfont.Font(family='Helvetica', size=8)
	
def setup_labels(labels, parent, width = 20, row=0, column=0):
	
	for text in labels:
		Label(parent, text=text, anchor='e', width = width).grid(row=row, column=column, sticky='NE')
		
		row += 1
		
def add_widgets(widgets, row=0, column=1):

	for widget in widgets:
		widget.grid(row=row, column=column, pady=5, sticky='NW')
		row += 1
		
def setup_ok_cancel_btns(frame, parent_page, row, column, rowspan=1, columnspan=1):

	#ok button
	ttk.Button(frame, text='OK', command=lambda button='ok': parent_page.cleanup(button)).grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
	
	#cancel button
	ttk.Button(frame, text='Cancel', command=lambda button='cancel': parent_page.cleanup(button)).grid(row=row, column=column+columnspan, rowspan=rowspan, columnspan=columnspan)