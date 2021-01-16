


# def main_func(x, y):
	# def inner(func):
		# func()
	# return inner
		

# @main_func
# def second_func():
	# print(x)
	# print('second func')
	
	
# second_func('var x', 'var y')

def my_decorator(a):
	def wrapper(f):
		def wrapped_function(y, widgets):
			
			print('wrapped_function')
			print(f(y, widgets) + a)
			widgets.append('a widget')
			
			print(widgets)
		return wrapped_function
	return wrapper

x=8	
@my_decorator(x)
def function(y, widgets):
	widgets.append('another widget')
	
	return y

widgets = []	
function(5, widgets)