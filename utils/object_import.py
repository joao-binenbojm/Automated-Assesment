import sys
sys.path.insert(1, '/Users/joaobinenbojm/desktop/Automated-Assesment/submissions/defs')
import importlib

def object_import(name, object_list):
	'''Returns the desired objects from a given .py file submission

	Positional Arguments:
	name -- name of student whose file is being read (string)
	object_list -- the objects that we would like to access from the student's file (string)

	Takes in the name of the student, the object names to import, and
	returns the objects from the student's file.
	'''
	module = importlib.__import__(name, fromlist=object_list)
	objects = []
	for obj in object_list:
		exec('objects.append(module.' + obj + ')')
	return tuple(objects)