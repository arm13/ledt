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

ledt = LEDT()

###################################################

out = ledt.disassemble("\x50\xff\xe4")
line_output(out)

out = ledt.disassemble_wrapper("\x50\xff\xe4")
line_output(out)

out = ledt.shellcode_format(out)
line_output(out)

###################################################
