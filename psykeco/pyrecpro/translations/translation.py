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

import locale

def MENU_HELP           (): return "MENU_HELP"
def DEBUG_ARG_NUMBER    (): return "DEBUG_ARG_NUMBER"
def DEBUG_ACT_PARAMETER (): return "DEBUG_ACT_PARAMETER"
def DEBUG_ARG_NUMBERS   (): return "DEBUG_ARG_NUMBERS"
def DEBUG_ARG_LIST      (): return "DEBUG_ARG_LIST"
def ERROR_NO_TRASLATION (): return "ERROR_NO_TRASLATION"

def en_EN(): return "en_EN"
def it_IT(): return "it_IT"

def default(): return en_EN()

def checkLang(): 
	print(locale.getdefaultlocale())
	return en_EN()
#checkLang

""" 
# 
"""
class Translation:
	translation=None

	def __init__(self, lang=None) -> None:
		lang= lang if lang!=None else checkLang() 
		fileTrans="en_EN.translation"

		if (lang==it_IT()):
			from .it_IT import translation
		else:
			# default language english
			from .en_EN import translation
		
		self.translation=translation()
	#constructor

	def getKey(self,key):
		value=self.translation.get(key)

		return value if value else self.translation[ERROR_NO_TRASLATION()]

#class