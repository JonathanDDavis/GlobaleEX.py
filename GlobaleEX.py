#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      jd0919889
#
# Created:     22/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
y = "global"

def globalScope():
    global x
    x = "local!"

globalScope()

print(x)