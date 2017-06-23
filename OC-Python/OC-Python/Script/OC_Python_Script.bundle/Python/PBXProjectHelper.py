#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import re
import hashlib
import uuid
import json

reload(sys)

# PBX解析类
class PBXProjectHelper (object) :

	def __init__(self, path) :
		super (PBXProjectHelper, self).__init__()

		if os.path.exists (path) :

			self.path = path
			# print "开始解析PBX路径 = %s" %path

			pbxprojFile = open(path, 'r')
			pbxprojData = pbxprojFile.read()

			# print "项目数据 = %s" %pbxprojData
			# 解释项目数据
			self.__parseDocument (pbxprojData)

		else :
			print "无效的PBX路径 = %s" %path


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


	# 解析文档
	def __parseDocument (self, projData) :

		pos = 0

		# 取得头描述，
		if len (projData) > 2 and projData [0] == "/" and projData [1] == "/" :

			start = pos = 2
			while len (projData) > pos and projData[pos] != "\n":
				pos += 1

			self.header = projData [start : pos].strip()
			# print "pbx header = %s" %self.header

		projData = projData[pos:]
		

		# 去除所有注释内容
		(projData, num) = re.subn ("\/\*.*?\*\/", "", projData)

		# 获取带引号值
		self.__quotValues = []
		for match in re.finditer("(\".*?\")", projData) :
			if  match :
				self.__quotValues.append (match.groups()[0])
				# print match.groups()[0]

		# 过滤空白字符
		(projData, num) = re.subn ("\s+", "", projData)
		# print "projData = %s" %projData
		
		pos = 0
		if projData [pos] == "{" :

			(self.root, pos) = self.__parseDictionary (projData, pos + 1)
			# print "解析成功! root = %s" %self.root

		else :

			print "无效的PBX数据!"
			self.header = None
			self.root = None


	# 解析数据
	def __parseData (self, projData, start) :

		data = None
		datatype = 0

		c = projData[start]
		if c == "{" :

			# 字典
			datatype = 1
			(data, end) = self.__parseDictionary (projData, start + 1)

		elif c == "(" :

			# 数组
			datatype = 2
			(data, end) = self.__parseArray (projData, start + 1)

		else :

			# 单值
			datatype = 3
			(data, end) = self.__parseSimpleValue (projData, start)


		return data, datatype, end

	# 解析字典数据
	def __parseDictionary (self, projData, start) :
		
		dictValue = {}
		end = start

		# print "++++++++++start dict"
		while len (projData) > end and projData [end] != "}" :
			
			(key, value, end) = self.__parseKeyValuePair (projData, end)
			if key :
				# print "key = %s, value = %s" %(key, value)
				dictValue [key] = value	

		if len (projData) > end + 1 and (projData [end + 1] == ";" or projData [end + 1] == ",") :
			end += 1

		# print "++++++++++end dict"

		return dictValue, end + 1 

	# 解析字典的键值对
	def __parseKeyValuePair (self, projData, start) :
		
		key = None
		value = None
		end = start
		isQuotStart = False

		if projData[end] == "\"" :
			end += 1
			isQuotStart = True

		while len (projData) > end :

			hasFindKey = False

			if isQuotStart :

				if projData[end] == "\"" :
					end += 1
					hasFindKey = True

			elif projData [end] == "=" :

				hasFindKey = True

			if hasFindKey :
				key = projData [start : end]

				if isQuotStart :
					key = self.__quotValues [0]
					del self.__quotValues [0]

				# print "******** find key = %s" %key
				# 获取值
				(value, datatype, end) = self.__parseData (projData, end + 1)
				break

			else :
				
				end += 1

		return (key, value, end)

	# 解析数组数据
	def  __parseArray (self, projData, start) :

		arrayValue = []
		end = start

		# print "================start array"
		while len (projData) > end and projData [end] != ")" :

			(elm, datatype, end) = self.__parseData (projData, end)
			if elm :
				# print "elm = %s" %elm
				arrayValue.append (elm)

		if len (projData) > end + 1 and (projData [end + 1] == ";" or projData [end + 1] == ",") :
			end += 1

		# print "================end array"

		return arrayValue, end + 1



	# 解析一个简单值
	def  __parseSimpleValue (self, projData, start):
		
		value = None
		end = start
		isQuotStart = False

		if projData [end] == "\"" :
			end += 1
			isQuotStart = True

		while len (projData) > end :

			if isQuotStart :

				if projData[end] == "\"" :
					end += 1
					break
				else :
					end += 1

			elif projData[end] == ";" or projData[end] == "," :

				break

			else :

				end += 1

		if end > start :

			value = projData [start : end]

			if isQuotStart :
				value = self.__quotValues [0]
				del self.__quotValues [0]

		return value, end + 1

	# 创建唯一ID
	def __genID(self):
		examplehash = "D04218DC1BA6CBB90031707C"
		# uniquehash = hashlib.sha224(name).hexdigest().upper()
		# uniquehash = uniquehash[:len(examplehash) - 4]
		# return '365' + uniquehash

		uid = str(uuid.uuid1 ())
		(uid, num) = re.subn ("-", "", uid)
		uid = uid.upper ()
		return uid [:len(examplehash)]

	# 转换值为字符串
	def __valueToString(self, value, indent):
		
		if isinstance (value, dict) :
			return self.__dictToString (value, indent)
		elif isinstance (value, list) :
			return self.__listToString (value, indent)
		else :
			return self.__simpleValueToString (value, indent)

	# 转换简单值为字符串
	def __simpleValueToString(self, data, indent):
		return data

	# 转换数组为字符串
	def __listToString(self, data, indent):
		text = "(\n"

		indent += "\t"
		for value in data :
			text += indent + self.__valueToString (value, indent) + ",\n"

		indent = indent [0 : len (indent) - 1]
		text += indent + ")"
		
		return text

	# 转换字典为字符串
	def __dictToString(self, data, indent) :

		text = "{\n"

		indent += "\t"
		for (k,v) in data.items() :
			text += indent + k + " = " + self.__valueToString (v, indent) + ";\n"

		indent = indent [0 : len (indent) - 1]
		text += indent + "}"

		return text

	# 保存修改
	def save (self) :

		indent = ""
		projData = "// " + self.header + "\n"

		projData += self.__dictToString (self.root, indent)
		# print projData

		# 写入到文件
		project_file = open(self.path, 'w')
		project_file.write(projData)



	# 获取分组信息
	# @param gid 分组标识
	# @return 分组信息
	def getGroup (self, gid) :

		if not gid :
			# 获取主分组ID
			rootObjId = self.root ["rootObject"]
			gid = self.root ["objects"] [rootObjId] ["mainGroup"]


		groupInfo = self.root ["objects"] [gid]
		if groupInfo ["isa"] == "PBXGroup" or groupInfo ["isa"] == "PBXVariantGroup" :
			return groupInfo

		return None

	# 根据分组名称获取分组ID列表
	def getGroupIDsByName (self, name) :

		groupIds = []

		for (k,v) in self.root ["objects"].items() :

			if (v["isa"] == "PBXGroup" or v["isa"] == "PBXVariantGroup") and v.has_key("name") and v["name"] == name :
				groupIds.append (k)

		return groupIds

	# 添加分组
	# @param name   分组名称
    # @param parentGroupId  父级分组标识，如果为None则表示根分组
    # @param isVarGroup 是否为Variant Group
    # @return 分组ID
	def addGroup (self, name, parentGroupId = None, isVarGroup = False) :
		
		# 创建分组标识
		gid = self.__genID()
		# print "gid = %s" %gid

		# 创建分组信息
		groupInfo = {}

		if isVarGroup : 
			groupInfo ["isa"] = "PBXVariantGroup"
		else :
			groupInfo ["isa"] = "PBXGroup"

		groupInfo ["name"] = name
		groupInfo ["sourceTree"] = "\"<group>\""
		groupInfo ["children"] = []

		# 查找父级目录
		parentGround = self.getGroup (parentGroupId)
		# print "group = %s" %parentGround
		if parentGround:
			# 写入分组信息
			self.root ["objects"] [gid] = groupInfo
			parentGround ["children"].append (gid)

		return gid

	# 移除分组信息
	# @param gid 分组id
	def removeGroup (self, gid) :
		
		if gid :
			del self.root ["objects"] [gid]

	# # 添加系统框架
	def addSysFramework (self, framework) :
		
		self.addFramework('System/Library/Frameworks/' + framework)

	# # 添加框架
	def addFramework (self, framework, groupId = None) :
		
		name = os.path.basename(framework)

		sourceTreeStr = None
		if framework.startswith("System/Library/Frameworks/") :
			sourceTreeStr = "SDKROOT"
		else :
			sourceTreeStr = "\"<group>\""

		# 判断是否存在此文件引用
		fileRefIds = self.getFileReferenceIDsByPath (framework)

		if len (fileRefIds) > 0 :
			fileRefGuid = fileRefIds [0]
		else :
			# 添加文件引用
			fileRefGuid = self.addFileReference(name, "wrapper.framework", framework, sourceTreeStr)

		# 判断文件是否已经加入编译列表
		buildFileIds = self.getBuildFileIDsByFileRefID (fileRefGuid)

		if len (buildFileIds) > 0 :
			buildFileGuid = buildFileIds [0]
		else :
			# 添加编译文件
			buildFileGuid = self.addBuildFile(fileRefGuid)

		# 添加文件到分组
		group = None
		if groupId :
			group = self.getGroup (groupId)

		if not group :
			frameworkGroupIds = self.getGroupIDsByName ("Frameworks")
			if len (frameworkGroupIds) > 0 :
				groupId = frameworkGroupIds [0]
			else :
				groupId = self.addGroup ("Frameworks")

			group = self.getGroup (groupId)

		self.addFileToGroup (fileRefGuid, group)

		# 添加Build Phase
		self.addFrameworkBuildPhase (buildFileGuid)

	# 添加Framework Build Phase
	# @param buildFileGuid  编译文件唯一标识
	def addFrameworkBuildPhase (self, buildFileGuid) :

		for (k,v) in self.root ["objects"].items() :

			if v ["isa"] == "PBXFrameworksBuildPhase" :

				if buildFileGuid not in v["files"] :
					v["files"].append (buildFileGuid)

			break

	# 添加Resource Build Phase
	# @param buildFileGuid  编译文件唯一标识
	def addResourcePhase (self, buildFileGuid) :

		for (k,v) in self.root ["objects"].items() :

			if v ["isa"] == "PBXResourcesBuildPhase" :

				if buildFileGuid not in v["files"] :
					v["files"].append (buildFileGuid)

			break

	# 添加系统动态库
	# @param dylib  动态库名称
	def addSysDylib (self, dylib) :

		self.addDylib ("usr/lib/" + dylib)

	# 添加动态库
	# @parma dylib  动态库路径
	# @param groupId 所属分组ID，默认为None，即加入Framework分组中
	def addDylib (self, dylib, groupId = None) :

		name = os.path.basename(dylib)

		sourceTreeStr = None
		if dylib.startswith("usr/lib/") :
			sourceTreeStr = "SDKROOT"
		else :
			sourceTreeStr = "\"<group>\""

		# 判断是否存在此文件引用
		fileRefIds = self.getFileReferenceIDsByPath (dylib)

		if len (fileRefIds) > 0 :
			fileRefGuid = fileRefIds [0]
		else :
			# 添加文件引用
			fileRefGuid = self.addFileReference(name, "compiled.mach-o.dylib", dylib, sourceTreeStr)


		# 判断文件是否已经加入编译列表
		buildFileIds = self.getBuildFileIDsByFileRefID (fileRefGuid)

		if len (buildFileIds) > 0 :
			buildFileGuid = buildFileIds [0]
		else :
			# 添加编译文件
			buildFileGuid = self.addBuildFile(fileRefGuid)

		# 添加文件到分组
		group = None
		if groupId :
			group = self.getGroup (groupId)

		if not group :
			frameworkGroupIds = self.getGroupIDsByName ("Frameworks")
			if len (frameworkGroupIds) > 0 :
				groupId = frameworkGroupIds [0]
			else :
				groupId = self.addGroup ("Frameworks")

			group = self.getGroup (groupId)

		self.addFileToGroup (fileRefGuid, group)

		# 添加Build Phase
		self.addFrameworkBuildPhase (buildFileGuid)

	# 添加静态库
	# @param staticLib 静态库路径
	# @param groupId 分组ID
	def addStaticLib (self, staticLib, groupId = None) :

		name = os.path.basename (staticLib)

		# 判断是否存在此文件引用
		fileRefIds = self.getFileReferenceIDsByPath (staticLib)

		if len (fileRefIds) > 0 :
			fileRefGuid = fileRefIds [0]
		else :
			# 添加文件引用
			fileRefGuid = self.addFileReference(name, "archive.ar", staticLib, "\"<group>\"")

		# 判断文件是否已经加入编译列表
		buildFileIds = self.getBuildFileIDsByFileRefID (fileRefGuid)

		if len (buildFileIds) > 0 :
			buildFileGuid = buildFileIds [0]
		else :
			# 添加编译文件
			buildFileGuid = self.addBuildFile(fileRefGuid)

		# 添加文件到分组
		group = None
		if groupId :
			group = self.getGroup (groupId)

		if not group :
			frameworkGroupIds = self.getGroupIDsByName ("Frameworks")
			if len (frameworkGroupIds) > 0 :
				groupId = frameworkGroupIds [0]
			else :
				groupId = self.addGroup ("Frameworks")

			group = self.getGroup (groupId)

		self.addFileToGroup (fileRefGuid, group)

		# 添加Build Phase
		self.addFrameworkBuildPhase (buildFileGuid)

	# 添加头文件
	# @param header 头文件路径
	# @param groupId 分组ID
	def addHeaderFile (self, header, groupId = None) :
	
		name = os.path.basename (header)

		# 判断是否存在此文件引用
		fileRefIds = self.getFileReferenceIDsByPath (header)

		if len (fileRefIds) > 0 :
			fileRefGuid = fileRefIds [0]
		else :
			# 添加文件引用
			fileRefGuid = self.addFileReference(name, "sourcecode.c.h", header, "\"<group>\"")

		group = self.getGroup (groupId)
		self.addFileToGroup (fileRefGuid, group)

	# 添加Bundle
	# @param bunlde 资源包路径
	# @param groupId  分组ID
	def addBundle (self, bundle, groupId = None) :

		name = os.path.basename(bundle)

		# 判断是否存在此文件引用
		fileRefIds = self.getFileReferenceIDsByPath (bundle)

		if len (fileRefIds) > 0 :
			fileRefGuid = fileRefIds [0]
		else :
			# 添加文件引用
			fileRefGuid = self.addFileReference(name, "wrapper.plug-in", bundle, "SOURCE_ROOT")

		# 判断文件是否已经加入编译列表
		buildFileIds = self.getBuildFileIDsByFileRefID (fileRefGuid)

		if len (buildFileIds) > 0 :
			buildFileGuid = buildFileIds [0]
		else :
			# 添加编译文件
			buildFileGuid = self.addBuildFile(fileRefGuid)

		# 添加文件到分组
		group = self.getGroup (groupId)
		self.addFileToGroup (fileRefGuid, group)

		#  添加Bundle Phase
		self.addResourcePhase(buildFileGuid)

	# 添加本地化文件
	# @param lang   语言
	# @param path 路径
	# @param groupId 	分组ID
	def addLocalizedFile (self, lang, path, groupId = None) :

		print lang + path

		fileRefIds = self.getFileReferenceIDsByPath (path)
		if len (fileRefIds) > 0 :
			fileRefGuid = fileRefIds [0]
		else :
			# 添加文件引用
			fileRefGuid = self.addFileReference(lang, "text.plist.strings", path, "\"<group>\"")

		# 判断文件是否已经加入编译列表
		buildFileIds = self.getBuildFileIDsByFileRefID (fileRefGuid)

		if len (buildFileIds) > 0 :
			buildFileGuid = buildFileIds [0]
		else :
			# 添加编译文件
			buildFileGuid = self.addBuildFile(fileRefGuid)

		# 添加文件到分组
		group = self.getGroup (groupId)
		self.addFileToGroup (fileRefGuid, group)

		self.addResourcePhase(buildFileGuid)


	# 获取配置项信息
	# @param target 编译目标，如果为None，则表示获取项目的根配置信息
	# @param scheme 模式：Debug、Release或者其他
	# @return 配置信息
	def getBuildSettings (self, target = None, scheme = "Debug") :

		projId = self.root ["rootObject"]
		projInfo = self.root ["objects"] [projId]
		if projInfo and projInfo ["isa"] == "PBXProject" :

			# 获取默认的配置ID
			confId = projInfo ["buildConfigurationList"]

			if target :

				# 查找Target
				targets = projInfo ["targets"]
				for tid in targets :
					targetInfo = self.root ["objects"] [tid]
					if targetInfo ["isa"] == "PBXNativeTarget" and targetInfo ["name"] == target :
						confId = targetInfo ["buildConfigurationList"]
						break

			confiListInfo = self.root ["objects"] [confId]
			if confiListInfo and confiListInfo ["isa"] == "XCConfigurationList" :

				# 查找指定Scheme的配置信息
				buildConfs = confiListInfo ["buildConfigurations"]
				for bcid in buildConfs :
					buildConfInfo = self.root ["objects"] [bcid]
					if buildConfInfo and buildConfInfo ["isa"] == "XCBuildConfiguration" and buildConfInfo ["name"] == scheme :
						return buildConfInfo ["buildSettings"]

		return None

	# 添加Framework搜索路径
	# @param path 搜索路径
	# @param target 编译目标，如果为None，则表示获取项目的根配置信息
	# @param scheme 模式：Debug、Release或者其他
	def addFrameworkSearchPath (self, path, target = None, scheme = "Debug") :

		settings = self.getBuildSettings (target, scheme)
		if settings :

			if not settings.has_key("FRAMEWORK_SEARCH_PATHS") : 
				settings ["FRAMEWORK_SEARCH_PATHS"] = []

			if path not in settings ["FRAMEWORK_SEARCH_PATHS"] :
				settings ["FRAMEWORK_SEARCH_PATHS"].append (path)


	# 添加Library搜索路径
	# @param path 搜索路径
	# @param target 编译目标，如果为None，则表示获取项目的根配置信息
	# @param scheme 模式：Debug、Release或者其他
	def addLibrarySearchPath (self, path, target = None, scheme = "Debug") :

		settings = self.getBuildSettings (target, scheme)
		if settings :

			if not settings.has_key("LIBRARY_SEARCH_PATHS") : 
				settings ["LIBRARY_SEARCH_PATHS"] = []

			if path not in settings ["LIBRARY_SEARCH_PATHS"] :
				settings ["LIBRARY_SEARCH_PATHS"].append (path)


	# 添加Other Linker Flag
	# @param flag 标识
	# @param target 编译目标，如果为None，则表示获取项目的根配置信息
	# @param scheme 模式：Debug、Release或者其他
	def addOtherLinkerFlag (self, flag, target = None, scheme = "Debug"):

		settings = self.getBuildSettings (target, scheme)
		if settings :

			if not settings.has_key("OTHER_LDFLAGS") : 
				settings ["OTHER_LDFLAGS"] = []

			if flag not in settings ["OTHER_LDFLAGS"] :
				settings ["OTHER_LDFLAGS"].append (flag)


	# 添加文件到分组
	# @param fileRefId 文件标识
	# @param group 分组信息
	def addFileToGroup (self, fileRefId, group) :
		if group and (fileRefId not in group ["children"]) :
			group ["children"].append (fileRefId)

	# 添加文件引用
	# @param name   名称
	# @param fileType   文件类型
	# @param path   路径信息
	# @param sourceTree 
	# @return 文件引用ID
	def addFileReference (self, name, fileType, path, sourceTree) :

		fid = self.__genID()

		fileRefInfo = {}
		fileRefInfo ["path"] = path
		fileRefInfo ["sourceTree"] = sourceTree
		fileRefInfo ["isa"] = "PBXFileReference"
		fileRefInfo ["lastKnownFileType"] = fileType
		fileRefInfo ["name"] = name

		self.root ["objects"] [fid] = fileRefInfo

		return fid

	# 获取文件引用信息
	# @param fid
	# @return 文件引用信息
	def getFileReference (self, fid) :

		fileRefInfo = self.root ["objects"] [fid]
		if fileRefInfo ["isa"] == "PBXFileReference" :
			return fileRefInfo

		return None

	# 根据路径获取文件引用ID集合
	# @param path 路径
	# @return 文件ID数组
	def getFileReferenceIDsByPath (self, path) :

		fileRefIds = []

		for (k,v) in self.root ["objects"].items() :

			if v["isa"] == "PBXFileReference" and v["path"] == path :
				fileRefIds.append (k)

		return fileRefIds

	# 添加编译文件
	# @param fileRefGuid    文件引用标识
	# @return 编译文件ID
	def addBuildFile (self, fileRefGuid):

		bid = self.__genID()

		buildFileInfo = {}
		buildFileInfo ["isa"] = "PBXBuildFile"
		buildFileInfo ["fileRef"] = fileRefGuid

		self.root ["objects"] [bid] = buildFileInfo

		return bid

	# 获取编译文件信息
	# @param bid 编译文件ID
	# @return 编译文件信息
	def getBuildFile (self, bid) :

		buildFileInfo = self.root ["objects"] [fid]
		if buildFileInfo ["isa"] == "PBXBuildFile" :
			return buildFileInfo

		return None

	# 根据文件引用ID获取编译文件ID列表
	# @param fileRefId 文件应用标识
	# @return 编译文件ID列表
	def getBuildFileIDsByFileRefID (self, fileRefId) :

		buildFileIds = []

		for (k,v) in self.root ["objects"].items() :

			if v["isa"] == "PBXBuildFile" and v["fileRef"] == fileRefId :
				buildFileIds.append (k)

		return buildFileIds


# python PBXProjectHelper.py /Users/fenghj/Documents/work/Demo/Demo.xcodeproj/project.pbxproj
# def main():

# 	sys.setdefaultencoding('utf-8')

# 	if  len (sys.argv) > 1 :
# 		pbxPath = sys.argv[1]
# 		parser = PBXProjectHelper (pbxPath)
# 		parser.addGroup ("Demo")
# 		parser.addSysFramework("UIKit.framework")
# 		parser.addSysDylib("libz.tbd")
# 		parser.addStaticLib("123.a")
# 		parser.addOtherLinkerFlag("-ObjC")
# 		parser.save ()


# if __name__ == "__main__":
# 	sys.exit(main())

# OC调用Python打印
# 函数参数前加*号表示可变长参数
def oc_PythonLogButtonClick(*data):
	print data
	helper = PBXProjectHelper("/Users/youzu/Desktop/UniversalApp/UniversalApp.xcodeproj/project.pbxproj")
	helper.addLocalizedFile(data[0], data[1])
	return json.dumps({"success":"yes", "msg":str(data)})

