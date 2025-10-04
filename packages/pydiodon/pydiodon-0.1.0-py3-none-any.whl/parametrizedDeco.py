#!/usr/bin/env python3

#https://stackoverflow.com/questions/739654/how-do-i-make-function-decorators-and-chain-them-together/1594484#1594484

import multiprocessing

def decorator_with_args(decorator_to_enhance):
	""" 
	This function is supposed to be used as a decorator.
	It must decorate an other function, that is intended to be used as a decorator.
	Take a cup of coffee.
	It will allow any decorator to accept an arbitrary number of arguments,
	saving you the headache to remember how to do that every time.
	"""
	
	# We use the same trick we did to pass arguments
	def decorator_maker(*args, **kwargs):
		# We create on the fly a decorator that accepts only a function
		# but keeps the passed arguments from the maker.

		def decorator_wrapper(func):
			# We return the result of the original decorator, which, after all, 
			# IS JUST AN ORDINARY FUNCTION (which returns a function).
			# Only pitfall: the decorator must have this specific signature or it won't work:
			return decorator_to_enhance(func, *args, **kwargs)
		return decorator_wrapper
	return decorator_maker



@decorator_with_args 
def spawn(func, *args, **kwargs): 
	def wrapper(*args_w, **kwargs_w):
		if kwargs['skip']:
			#print(f'SKIPPED {func=}\n{args=} {kwargs=}\n{args_w[0]=} {kwargs_w=}')
			return func(*args_w, **kwargs_w)
		else:
			def _(*args_w, **kwargs_w):
				p = multiprocessing.Process(target=func, args=args_w, kwargs=kwargs_w, daemon=False)
				p.start()
			return _(*args_w, **kwargs_w)
	return wrapper

