#TODO

from os.path import expanduser
import os
import maya.cmds as cmds
import maya.mel as mel
import shutil
import Utils.os_Find_Env.findEnv_app as findEnv

class animShelfCore(object):

	def __init__(self):
		
		self.pathShelf, self.pathIcons = self.getPath()
		self.env = findEnv.findEnvVar_() + '/'
		self.shelf = self.env + 'Animacion/Maya_Animation_ShelfCharTools/shelf_MKF_CharTools.mel'
		self.icons = self.env + 'Animacion/Maya_Animation_ShelfCharTools/Icons/'

		icons = os.listdir(self.icons)

		for icon in icons:
			self.retrieveMasterCopy(self.icons + icon, self.pathIcons)

	def main(self):
		self.retrieveMasterCopy(self.shelf, self.pathShelf)

	def retrieveMasterCopy(self, src, dest):
		shutil.copy(src, dest)


	def getPath(self):
		'''
		'''
		
		versionsDict = {'2015': '2015-x64', '2017': '2017', '2018': '2018'}

		docs = expanduser("~")
		version = cmds.about(version=True)

		localPathShelves = docs + '/maya/2018/prefs/shelves/'
		localPathIcons = docs + '/maya/2018/prefs/icons/'

		return localPathShelves, localPathIcons

shelf = animShelfCore()
shelf.main()



