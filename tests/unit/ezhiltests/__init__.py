# (C) 2013 Muthiah Annamalai
# path manipulation magic sets up the current development verison of ezhil
# as the library from the "ezhil-lang/tests/unit" path.

import sys, os

ezhil_path = "/".join(os.getcwd().split('/')[:-2])
#print ezhil_path
sys.path.insert(0,ezhil_path)

import ezhil    