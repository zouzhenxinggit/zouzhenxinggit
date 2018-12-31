#!/usr/bin/python3
#coding=utf-8


print("package make")

import package_one.sendmsg

package_one.sendmsg.send_message()


from package_one import *

recvmsg.recv_message()


#__init__.py中__all__是*调用那些模块
#模块中的__all__是*调用哪些东西

#包是可以嵌套的
'''
Phone/
    __init__.py
    common_util.py
    Voicedta/
        __init__.py
        Pots.py
        Isdn.py
    Fax/
        __init__.py
        G3.py
    Mobile/
        __init__.py
        Analog.py
        igital.py
    Pager/
        __init__.py
        Numeric.py

#沿着树的结构可以一直调用
import Phone.Mobile.Analog
from Phone import Mobile
from Phone.Mobile import Analog
from Phone.Mobile.Analog import dial
from package.module import *
'''