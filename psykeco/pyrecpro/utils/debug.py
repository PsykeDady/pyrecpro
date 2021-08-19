##########################################################################
#                                                                        #
# THIS SOFTWARE IS PART OF "PyRecPro" project by "PsykeDady"             #
# AND IS RELEASED UNDER GPLv3 LICENSE.                                   #
#                                                                        #
# Please read LICENSE file or footer of main file "pyrecpro.py"          #
# for other informations.                                                #
#                                                                        #
# Github repository of project at: https://github.com/PsykeDady/pyrecpro #
#                                                                        #
##########################################################################

"""
### if true, print debug is globally active
"""
global_debug=False

""" 
# DebugPrint
This calss contains a logging system for project
"""
class DebugPrint:
	"""
	if true, debug is active for local instance
	"""
	local_debug=False
	caller=None

	def __init__(self,local_debug=False,caller=None) -> None:
		self.local_debug=local_debug
		self.caller=caller
	#constructor

	def setLocalDebug(self,local_debug):
		self.local_debug=local_debug
	#setLocalDebug

	"""
	debug method print only 
	"""
	def debug(self,*args, sep=' ', end='\n', file=None):
		caller= "[DEBUG]" if self.caller==None else "[DEBUG "+self.caller+"] "
		if (global_debug and self.local_debug):
			print(caller,*args,sep=sep,end=end,file=file)
		#fi
	#print
#class
