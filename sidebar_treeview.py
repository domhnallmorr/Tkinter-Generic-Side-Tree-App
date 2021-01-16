import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

from main import PopUpScreen

class MainTreeview(ttk.Treeview):

	def __init__(self, nodes, mainapp, component_class):
		
		super(MainTreeview, self).__init__(mainapp.sidebar_frame, selectmode='browse', show="tree") #check if this convention is right
		
		self.mainapp = mainapp
		self.nodes = nodes
		self.component_class = component_class
		
		self.setup_nodes()
		
		self.current_frame = None #the current page being shown
		self.frames = {}
		
		#bind left click event
		self.bind('<<TreeviewSelect>>',lambda event, : self.singleclick(event))
		
		self.special_chars = [',', '/', '_', '.', '@']
		
	def setup_nodes(self):
	
		for node in self.nodes:
			self.insert("",'end',node,text=node)
			
			
	def new_component(self, type):
		
		self.w = PopUpScreen(self.mainapp, self.mainapp.master, 'new', None, self.mainapp.edit_pages[type])
		#self.w = self.mainapp.edit_pages[type](self.mainapp, self.master, 'new', None)
		self.master.wait_window(self.w.top)
		
		if self.w.button == 'ok':
		
			component = self.component_class(self.mainapp.container, self.mainapp, type, self.w) #create frontend and backend instances
			
			self.frames[component.backend.title] = component #so we can access the page later
			
			iid = self.insert_component_into_tree(component)
			
			self.show_page(component.backend.title)
	
		
	def insert_component_into_tree(self, component):
	
		iid = self.insert(component.treeview_node,'end', text=component.backend.title)
		
		component.iid = iid
		
	def show_page(self, component):

		if self.current_frame:
			self.current_frame.pack_forget()
			
		frame = self.frames[component]
		frame.pack(fill="both", expand=True)
		self.current_frame = self.frames[component]
		
	def singleclick(self, event):

		item_iid = event.widget.selection()[0]
		parent_iid = event.widget.parent(item_iid)
		
		if parent_iid: #if it is a child node
			self.show_page(event.widget.item(item_iid, 'text'))
	
	def check_title(self, title):
		
		msg = None
		
		#check title entered
		if title == '':
			msg = 'Enter a Title'
			
		if not msg:
			#check special characters
			for char in self.special_chars:
				if char in title:
					msg = 'Title cannot contain any of the following characters;\n'
					msg = f'{msg} {"  ".join(self.special_chars)}'
		
		#Check title clash
		if not msg:
			if title in self.frames.keys():
				msg = 'A component with that title already exists, enter another title'
				
		return msg