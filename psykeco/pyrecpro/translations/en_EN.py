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

from .translation import MENU_HELP

from .translation import DEBUG_ARG_NUMBER
from .translation import DEBUG_ACT_PARAMETER
from .translation import DEBUG_ARG_NUMBERS
from .translation import DEBUG_ARG_LIST

from .translation import ERROR_NO_TRASLATION

""" 
# 
"""
def translation():
	return {
		MENU_HELP          ():"""%s is a software that help you to reorganize or restructure your c files into multiple headers and source files
		""",
		
		DEBUG_ARG_NUMBER   ():"Argument number"                              ,
		DEBUG_ACT_PARAMETER():"Actual parameter"                             ,
		DEBUG_ARG_NUMBERS  ():"number of arguments: "                        ,
		DEBUG_ARG_LIST     ():"list of arguments: "                          ,
		
		ERROR_NO_TRASLATION():"No traslation found for this msg. Contact dev"
	}
#translation