import os
from tkinter import Tk, filedialog

path = os.getcwd()
folderPath = os.getcwd()
choice = ""

while (choice != "yes"):
    choice = input("Do you want to classify this path :\n" + path + "\nyes/no\n")
    if choice == "no":
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        open_file = filedialog.askdirectory()
        path = open_file
        choice = "repeat"

choice=""

folderPath = path
while (choice != "yes"):
	choice = input("Do you want to classify in this path :\n" + folderPath + "\nyes/no\n")
	if choice == "no":
		root = Tk()
		root.withdraw()
		root.attributes('-topmost', True)
		open_file = filedialog.askdirectory()
		folderPath = open_file
		choice = "repeat"

# extension = [element.lower() for element in os.listdir(folderPath)]

extension = []

foledPath=folderPath+"\\Classi"
os.mkdir(folderPath)

for element in os.listdir(path):
	if element != __file__[__file__.rfind("\\")+1:]:
		currentFileExtension = element[(element.rfind(".")+1):]

		if currentFileExtension.lower() not in extension:
			extension.append(currentFileExtension)
			os.mkdir(folderPath+"\\"+currentFileExtension)

		try:
			os.rename("{}\\{}".format(path, element),
						"{}\\{}\\{}".format(folderPath, currentFileExtension, element))
			print("{}\\{} -> {}\\{}\\{}".format(path, element,
					folderPath, currentFileExtension, element))

		except Exception as e:
			print("Error : file {} has not been moved".format(element))
			print("Error : ", e)

close = input("Press enter to close...")
