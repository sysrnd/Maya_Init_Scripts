#TODO
#command
#title
#filter by user
#always return full path

import os
import maya.cmds as cmds
import Utils.os_Find_Env.findEnv_app as findEnv
import getpass

class proceduralMenus(object):
	def __init__(self):
		'''
		Initiliazes env vars of MAYA_SCRIPT_PATH
		Creates a list of folders where it shouldn't look into

		'''
		self.invalidFolders = ['Maya_Init_Scripts', '.git', 'Utils', 'Modules']
		self.invalidFiles = ['__init__', '.pyc', 'old']
		self.env = findEnv.findEnvVar_()
		
		self.menus = []
		self.submenus = []

	def main(self):
		avMenus = self.browseDirs(self.env)

		for avMenu in avMenus:
			#concatenate path
			avMenuPath = self.env + '/' + avMenu

			if self.isValidMenu(avMenuPath):
				menu = self.createMenu(avMenu)
				avSubmenus = self.browseDirs(avMenuPath)

				for avSubmenu in avSubmenus:
					avSubmenuPath = avMenuPath + '/' + avSubmenu
					filesInSubmenus = self.browseFiles(avSubmenuPath)
					for avFileInSubmenu in filesInSubmenus:
						filesInSubmenuPath = avSubmenuPath + '/' + avFileInSubmenu
						if self.isValidSubMenu(filesInSubmenuPath):
							command = self.parseCommandString(filesInSubmenuPath)
							self.createSubMenu(menu, avFileInSubmenu, command)




	def browseDirs(self, path):
		'''
		'''
		menus = []

		for dirs in os.listdir(path):
			dirPath = path + '/' + dirs
			if os.path.isdir(dirPath):
					menus.append(dirs)

		return menus


	def browseFiles(self, path):
		'''
		'''
		files = []

		for file in os.listdir(path):
			filePath = path + '/' + file
			if os.path.isfile(filePath):
				files.append(file)

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
		menu = cmds.menu(direc, label=direc, parent='MayaWindow')
		return menu

	def createSubMenu(self, menuParent, subMenu, command):
		'''
		'''
		subMenu = cmds.menuItem(subMenu, label=subMenu, parent= menuParent, command=command)
		return subMenu


	def parseCommandString(self, path):
		'''
		'''
		relativePath = path.replace(self.env + '/', '')
		relativePath = relativePath.replace('/', '.')
		parsedPath = 'import ' + relativePath + '; ' + 'reload(' + relativePath + ')'
		return parsedPath

	def splitLabelScreen(self, file):

		label = file.split('.')[0]
		label = label.strip('app')
		
		return label

	def getFileName(self, path):

		file = path.split('/')[-1]
		return file

menu = proceduralMenus()
menu.main()