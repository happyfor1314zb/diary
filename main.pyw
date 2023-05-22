import os
# 设置一个环境变量
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python310\tcl\tcl8.6'
from toDOCX import *
from sentTo import *

if __name__ == '__main__':
    toDOCX()
    send_to()
