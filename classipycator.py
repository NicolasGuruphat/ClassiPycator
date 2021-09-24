import os
path=os.getcwd()
repositoryPath = "C:\\Users\\nicog\\OneDrive\\Bureau\\Classification"
extension=[element.lower() for element in os.listdir(windowPath)]
print(extension)
choice=""
while(choice!="yes"):
	choice=input("Do you want to classify this path :\n"+path+"\n yes/no\n")
for element in os.listdir(path):
	print(element)
	if element != "classipycator.py":
		currentFileExtension= element[(element.rfind(".")+1):]
		print(currentFileExtension)
		if currentFileExtension.lower() not in extension:
			extension.append(currentFileExtension)
			os.mkdir(windowPath+"\\"+currentFileExtension)
		for ext in extension:
			if element[-len(ext):] == ext:
				try :
					os.rename("{}\\{}".format(path,element), "{}\\{}\\{}".format(windowPath,ext,element))
					print("{}\\{}".format(path,element)," move ", "({})".format(ext))
				except Exception as e:
					print("Error : file {} has not been moved".format(element))
					print("Error : ",e )
				break
fermer=input("Press enter to close...")
