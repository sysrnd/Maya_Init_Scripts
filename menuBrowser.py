#TODO
#filter by user
#delete menu in case there aren't any valid submenus found
import os
import maya.cmds as cmds
import Utils.os_Find_Env.findEnv_app as findEnv

class proceduralMenus(object):
	def __init__(self):
		'''
		Initiliazes env vars of MAYA_SCRIPT_PATH
		Creates a list of folders where it shouldn't look into

		'''
		self.invalidFolders = ['Maya_Init_Scripts', '.git', 'Utils', 'Modules', 'RenUI', 'Old', 'Dev']
		self.invalidFiles = ['__init__', '.pyc', 'old']
		#self.env = findEnv.findEnvVar_()
		self.env = 'Z:/RnD/Pipeline/Maya/Scripts/'
		
		self.menus = []
		self.submenus = []

	def main(self):
		avMenus = self.browseDirs(self.env)

		for avMenu in avMenus:
			#concatenate path
			if self.isValidMenu(avMenu):
				niceMenuName = self.getNiceFileName(avMenu)
				menu = self.createMenu(niceMenuName)
				avSubmenus = self.browseDirs(avMenu)

				for avSubmenu in avSubmenus:
					filesInSubmenus = self.browseFiles(avSubmenu)

					for avFileInSubmenu in filesInSubmenus:
						if self.isValidSubMenu(avFileInSubmenu):
							
							command = self.parseCommandString(avFileInSubmenu)
							niceFileName = self.getNiceFileName(avFileInSubmenu)
							self.createSubMenu(menu, avFileInSubmenu, niceFileName, command)




	def browseDirs(self, path):
		'''
		'''
		menus = []

		for dirs in os.listdir(path):
			dirPath = path + '/' + dirs

			if os.path.isdir(dirPath):
					menus.append(dirPath)

		return menus


	def browseFiles(self, path):
		'''
		'''
		files = []

		for file in os.listdir(path):
			filePath = path + '/' + file

			if os.path.isfile(filePath):
				files.append(filePath)

		return files

	def isValidMenu(self, file):
		'''
		'''
		isValid = False

		#unnecesary
		if os.path.isdir(file):
			isValid = True

		for invalid in self.invalidFolders:
			if file.find(invalid) != -1:
				isValid = False

		return isValid
	
	def isValidSubMenu(self, file):
		'''
		'''
		fileName = file.split('/')[-1]

		isValid = False

		#unnecesary
		if os.path.isdir(file):
			isValid = False

		if file.find('app') != -1 and file.find('old') == -1:
			isValid = True

		for invalid in self.invalidFiles:
			if file.find(invalid) != -1:
				isValid = False

		return isValid

	def createMenu(self, direc):
		'''
		'''

		menu = cmds.menu(direc, label=direc, parent='MayaWindow', to=True)
		return menu

	def createSubMenu(self, menuParent, subMenu, label, command):
		'''
		'''
		subMenu = cmds.menuItem(subMenu, label=label, parent= menuParent, command=command)
		return subMenu


	def parseCommandString(self, path):
		'''
		'''
		relativePath = path.replace(self.env + '/', '')
		relativePath = relativePath.replace('/', '.')
		relativePath = relativePath.replace('.py', '')
		parsedPath = 'import ' + relativePath + '; ' + 'reload(' + relativePath + ')'
		return parsedPath

	def getNiceFileName(self, path):

		file = path.split('/')[-1]
		niceName = file.replace('.py', '')
		niceName = niceName.replace('app', '')
		niceName = niceName.replace('_', ' ')

		if niceName.startswith(' '):
			niceName = niceName[1: len(niceName)]

		return niceName

menu = proceduralMenus()
menu.main()