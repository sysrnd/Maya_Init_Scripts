#TODO
#scan for folders for menus
#scan for subfolders for submenus
#find those that actually have the app.py file
#check if number of apps found match with those, it they do skip steps
#write to a file
#TODO
#command
#json
 myimport os
import Utils.findEnv as findEnv

class proceduralMenus (object) :
	
	def __init__(self):

		self.invalidFolders = ['initScripts']
		self.env = findEnv.findEnv_()
		self.menus = []
		self.submenus = []
	def main(self):

		avMenus = self.browseDirs

		for avMenu in avMenus:
			if self.isValidMenu(avMenu):
				self.createMenu()

				avSubmenus = browseFiles(avMenu)
				for avSubmenu in avSubmenus:
					if self.isValidSubMenu(avSubmenu)
						self.createSubMenu()





    def browseDirs(self, path):
    	'''
    	'''
    	menus = []

    	for dirs in os.listdir(path):
			if os.path.isdir(dirs):
				menu = cmds.menu(dirs, label=dirs, parent='MayaWindow')
				menus.append(menu)

		return menus

	def createMenu(self, dir, command):
		'''
		'''
		menu = cmds.menu(dirs, label=dirs, parent='MayaWindow')

	def createSubMenu(self, menuParent, subMenu):
		'''
		'''

    def browseFiles(self, menu, path):
    	'''
    	'''
    	files = []

    	for file in os.listdir(path):
			files.append(file)

		return files

	def isValidMenu(file):
		'''
		'''
		isValid = False

		if os.path.isDir(file):
			isValid = True

		if file in self.invalidFolders:
			isValid = False

		return isValid

	def isValidSubMenu(self, file):
		'''
		'''
		isValid = False

		if os.path.isfile(file):
			isValid = True

		if file.find('app') != -1:
			isValid = True
			if file.find('old'): == -1:
				#in case there are several apps
				isValid = True
			else:
				isValid = False

		return isValid

    def writeLocalInfo(self, file, txt):
    	'''
    	'''

        with open(file + '.txt' ,'w') as f:
            data = f.write(txt)

    def readLocalInfo(self, file, txt):
    	'''
    	'''

        if os.path.exists(file + '.txt'):
            with open(file + '.txt' ,'r') as f:
                data = f.read()
            txt.setText(data)
            return True
        else:
            return False