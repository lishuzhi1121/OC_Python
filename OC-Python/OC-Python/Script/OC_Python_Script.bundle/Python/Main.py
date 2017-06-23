#!/usr/bin/python
# encoding: utf-8
import os
import sys
import Functions
from Functions import *
from PBXProjectHelper import *

reload(sys)
sys.setdefaultencoding("utf-8")

# 操作文件路径
filePath = None
if  len(sys.argv) > 0:
	filePath = sys.argv[0]
	print(filePath)

# funcs = Functions()
# funcs.run(filePath)

helper = PBXProjectHelper("/Users/youzu/Desktop/UniversalApp/UniversalApp.xcodeproj/project.pbxproj")
helper.run(filePath)
