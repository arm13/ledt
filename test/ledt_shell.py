###############################################################
#       LEDT - Linux Exploit Development Tool
#
#       Copyright (C) 2014 random <random@pku.edu.cn>
#
###############################################################
try:
	import sys 
	sys.path.append("..") 
	from lib.ledt import *
	from lib.utils import *
except Exception,e:
	print e



LEDT().interact_shell()

