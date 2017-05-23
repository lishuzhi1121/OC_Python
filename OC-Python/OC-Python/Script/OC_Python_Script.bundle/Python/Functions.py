#!/usr/bin/python
# encoding: utf-8

import os
import sys
import json
import oc_python_module
reload(sys)
sys.setdefaultencoding("utf-8")

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
        	orig = super(Singleton, cls)
        	cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class Functions(Singleton):
	# 运行检测路径方法
	def run(self, filePath):
		if self.__loadPath(filePath):

			print("Success")
		else :

			print("Run Exception.")
		
	# 检测路径是否存在
	def __loadPath(self, filePath):
		self.filePath = filePath
		if os.path.exists(filePath):

			print("FilePath Exists.")
			return True
		else :

			print("FilePath Not Exists.")
			return False

	# Log
	def oc_PythonLog(self, *data):
		print(data)
		return json.dumps({"success":"yes", "msg":str(data)})

	# 读数据库到plist文件
	def oc_PythonWriteFile(self):
		path = '/Users/lishuzhi/Desktop/oc_python_test.txt'
		f = open(path, 'w+')
		try:
			f.write('A Python demo to show how Objective-C call Python and reverse.')
		except Exception as e:
			print 'Some bad happened:', e
		f.close()
		print('Write success.')
		return json.dumps({"success":"yes", "msg":'Write success.'})

	# Python Call OC
	def python_OCLog(self):
		return oc_python_module.myLog("I'm from Python.")

	# Python Call OC
	def python_OCAlert(self):
		return oc_python_module.myAlert()



		
# OC调用Python打印
# 函数参数前加*号表示可变长参数
def oc_PythonLogButtonClick(*data):
	print data
	funcs = Functions()
	return funcs.oc_PythonLog(data[0], data[1])

# OC调用Python写文件
def oc_PythonWriteFileButtonClick():
	funcs = Functions()
	return funcs.oc_PythonWriteFile()

# Python调用OC打印
def python_OCLogButtonClick():
	funcs = Functions()
	return funcs.python_OCLog()

# Python调用OC弹窗
def python_OCAlertButtonClick():
	funcs = Functions()
	return funcs.python_OCAlert()




