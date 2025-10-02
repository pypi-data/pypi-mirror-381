


'''
	This script should be run like:
		python3 /Metro/vehicles/octave_nexus/build__rules.py
'''

'''
	should build at:
	
		octave_nexus/rules_py/py_rules_entire.json
		octave_nexus/rules_py/PyPI_rules_legend.txt
		
				
'''

import os
from os.path import dirname, join, normpath
import pathlib
import sys

def system_proc (screenplay):
	print ("screenplay:", screenplay);
	os.system (screenplay);

this_folder = pathlib.Path (__file__).parent.resolve ();
# rules_folder = normpath (join (this_folder, "rules_py"));

py_rules_entire = "/Metro/Frontend_Vercel/static/Rules/Py_Entire.json"
py_rules_legends = "/Metro/Frontend_Vercel/static/Rules/Py_Legend.txt"


system_proc (f"pip-licenses --with-license-file --format=json > '{ py_rules_entire }'")
system_proc (f"pip-licenses > '{ py_rules_legends }'")