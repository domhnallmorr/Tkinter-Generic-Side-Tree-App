
class GraphPageBackend:

	def __init__(self):
	
		self.setup_variables()
		
	def setup_variables(self):
	
		self.title = None
		self.data_type = 'Graph'
		
	def update_variables(self, source):
	
		self.title = source.title
		
	def gen_save_dict(self):
	
		save_dict = {'title': self.title,
						'data type': self.data_type}
						
		return save_dict