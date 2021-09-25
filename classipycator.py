import os
from tkinter import Tk, filedialog
path=os.getcwd()
repositoryPath = "C:\\Users\\nicog\\OneDrive\\Bureau\\Classification"
extension=[element.lower() for element in os.listdir(repositoryPath)]
choice=""
while(choice!="yes" and choice != "no"):
	choice=input("Do you want to classify this path :\n"+path+"\nyes/no\n")
	if choice=="no":
		root = Tk()
		root.withdraw()
		root.attributes('-topmost', True)
		open_file = filedialog.askdirectory()
		path = open_file
		choice="repeat"
if choice =="yes":
	for element in os.listdir(path):
	#parcours tout les éléments présents dans le dossier où se trouve classiPycator
		if element != "classipycator.py":
			currentFileExtension= element[(element.rfind(".")+1):]

			if currentFileExtension.lower() not in extension:
				extension.append(currentFileExtension)
				os.mkdir(repositoryPath+"\\"+currentFileExtension)

			try :
				os.rename("{}\\{}".format(path,element), 
					      "{}\\{}\\{}".format(repositoryPath,currentFileExtension,element))
				print("{}\\{} -> {}\\{}\\{}".format(path,element, repositoryPath,currentFileExtension,element))
		
			except Exception as e:
					print("Error : file {} has not been moved".format(element))
					print("Error : ",e )
	
close=input("Press enter to close...")
