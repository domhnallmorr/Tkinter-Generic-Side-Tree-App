
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.messagebox

import sidebar_treeview
import status_box
from styling import tkinter_styles_

from data_pages import data_page_frontend
from data_pages import data_page_backend
from data_pages import data_edit_page

from graph_pages import graph_page_frontend
from graph_pages import graph_page_backend
from graph_pages import graph_edit_page

class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		
		self.parent = parent

		#styles
		tkinter_styles_.setup_fonts(self)
		
		self.setup_main_frames()
		
		#Define Component Classes (Backend and Frontend Classes)
		self.define_classes()
		
		#setup sidebar treeview
		tree_nodes = ['Project', 'Temperature', 'Rainfall', 'Graphs']
		self.sidebar_tree = sidebar_treeview.MainTreeview(tree_nodes, self, self.component_class)
		self.sidebar_tree.grid(row=1, column=1, sticky='NSEW')
		
		#menubar
		self.setup_menu()
		

		
		
	def setup_main_frames(self):
	
		self.main_rootpane = tk.PanedWindow(self.parent, orient=tk.VERTICAL)
		self.main_rootpane.grid(row=1,column=0, columnspan=4,sticky="nsew")
		
		self.rootpane = tk.PanedWindow(orient=tk.HORIZONTAL)
		self.rootpane.grid(row=1,column=0, columnspan=4,sticky="nsew")
		
		self.main_rootpane.add(self.rootpane)
		
		self.status_box = status_box.StatusBox(self)
		self.main_rootpane.add(self.status_box)
		
		self.parent.grid_rowconfigure(1, weight=1)
		self.parent.grid_columnconfigure(3, weight=1)
		self.frame = Frame(self.parent)
		
		self.sidebar_frame = tk.Frame()
		self.sidebar_frame.grid_rowconfigure(1, weight=1)
		self.sidebar_frame.grid_columnconfigure(19, weight=1)
		self.rootpane.add(self.sidebar_frame)

		self.frame.grid(row=0,column=0, sticky="n")
		
		# the container is where we'll stack a bunch of frames
		self.container = tk.Frame(self.rootpane, bg="pink")
		self.container.grid_columnconfigure(0, weight=1)
		self.rootpane.add(self.container,stretch="always")

		
	def setup_menu(self):

		menu = tk.Menu(self.master)
		self.master.config(menu=menu)
		
		#________ INSERT ________					  
		insert_menu = tk.Menu(menu, tearoff = 0)
		menu.add_cascade(label='Insert',menu=insert_menu)

		insert_menu.add_command(label = 'Data Component', command = lambda type='data': self.sidebar_tree.new_component(type))
		insert_menu.add_command(label = 'Graph Component', command = lambda type='graph': self.sidebar_tree.new_component(type))

	def define_classes(self):
		
		self.edit_pages = {'data': data_edit_page,
							'graph': graph_edit_page}
		
		self.backend_classes = {'data': data_page_backend.DataPageBackend,
								'graph': graph_page_backend.GraphPageBackend}
		
		self.frontend_classes = {'data': data_page_frontend,
								'graph': graph_page_frontend}
		
		self.component_class = AppFrontendComponent

class AppFrontendComponent(tk.Frame):
	def __init__(self, container, mainapp, component_type, source):
		tk.Frame.__init__(self, container)
		
		self.mainapp = mainapp
		
		#create backend instance
		self.backend = mainapp.backend_classes[component_type]()
		self.backend.update_variables(source)
		
		#create the frontend instance
		self.frontend = mainapp.frontend_classes[component_type]#(self, mainapp, self.backend)
		
		self.setup_labels()
		
		self.assign_treeview_node()
		
	def setup_labels(self):
		
		self.top_label = tk.Label(self, text=(f'Data: {self.backend.title}'),font=self.mainapp.title_font, anchor="w")
		self.top_label.pack()
	
	def update_component(self):
	
		self.assign_treeview_node()
		
	def assign_treeview_node(self):
	
		#Assign a node in the treeview
		if self.backend.data_type == 'Temperature':
			self.treeview_node = 'Temperature'
		elif self.backend.data_type == 'Rainfall':
			self.treeview_node = 'Rainfall'
		elif self.backend.data_type == 'Graph':
			self.treeview_node = 'Graphs'

class PopUpScreen:
	def __init__(self, mainapp, master, mode, parent_page, page_module):
		self.top = Toplevel(master)
		self.top.grab_set()
		self.mainapp = mainapp
		self.mode = mode
		self.parent_page = parent_page
		self.page_module = page_module
		
		self.page_module.setup_page(self, [])

	# def setup_page(self):
	
		# self.page_module.setup_label_frames(self)
		# self.page_module.setup_widgets(self)

	def cleanup(self, button):
		
		self.button = button
		
		if button == 'cancel': #close the window
			self.top.destroy()
			
		else: #handle user clicking ok
			
			title_checker = self.mainapp.sidebar_tree.check_title
			msg, status_text = self.page_module.check_user_input(self, title_checker)
			
			if not msg:
				
				#get input data
				self.page_module.get_user_input(self)
				#close the window
				self.top.destroy()
				self.mainapp.status_box.add_text(status_text)
				
			else:

				tkinter.messagebox.showerror(master=self.top, title='Error', message=msg)
		
if __name__ == "__main__":
	root = tk.Tk()
	root.resizable(width=tk.TRUE, height=tk.TRUE)
	#MainApplication(root).pack(side="top", fill="both", expand=True)
	MA = MainApplication(root)
	MA.grid(row=1, columnspan=4, sticky='nsew')
	#root.bind('<Control-z>', MA.states.undo)
	#root.bind('<Control-y>', MA.states.redo)
	
	#root.geometry('{}x{}'.format(MA.screen_width, MA.screen_height))    
	
	root.mainloop()