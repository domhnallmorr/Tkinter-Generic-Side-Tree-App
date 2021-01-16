
from styling import tkinter_styles_


class DataPageBackend:

	def __init__(self):
	
		self.setup_variables()
		
	def setup_variables(self):
	
		self.title = None
		self.data_type = None
		
	def update_variables(self, source):
	
		self.title = source.title
		self.data_type = source.data_type
		
	def gen_save_dict(self):
	
		save_dict = {'title': self.title,
						'data type': self.data_type}
						
		return save_dict