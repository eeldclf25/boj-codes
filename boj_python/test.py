import sys

class File:
    def __init__(self, fileName):
        self.name = fileName
        self.childFile = {}

    def search(self, fileName):
        if fileName in self.childFile:
            return self.childFile[fileName]
        else:
            return None
    
    def make(self, fileName):
        if not fileName in self.childFile:
            self.childFile[fileName] = File(fileName)
            return True
        else:
            return False

def SearchFile(file, pathList):
    if file == None or len(pathList) == 0:
        return file
    else:
        return SearchFile(file.search(pathList[0]) , pathList[1:])

def copyFile(baseFile, targetFile):
    for key in baseFile.childFile.keys():
        targetFile.make(key)
        copyFile(baseFile.childFile[key], targetFile.childFile[key])
    
def printFile(file, path):
    for childFile in file.childFile.values():
        print(path + childFile.name)
    for childFile in file.childFile.values():
        printFile(childFile, path + childFile.name + "/")





def func(inputValue):
    rootFile = File("")

    for i in range(0, len(inputValue)):
        if "mkdir" in inputValue[i]:
            pathList = inputValue[i].split()[1].split("/")
            checkFile = SearchFile(rootFile, pathList[1:-1])

            if checkFile is not None:
                checkFile.make(pathList[len(pathList) - 1])
            
        elif "cp" in inputValue[i]:
            basePathList = inputValue[i].split()[1].split("/")
            baseFile = SearchFile(rootFile, basePathList[1:])
            targetPathList = inputValue[i].split()[2].split("/")
            targetFile = SearchFile(rootFile, targetPathList[1:])

            if baseFile and targetFile is not None:
                copyFile(baseFile, targetFile)
        elif "rm" in inputValue[i]:
            print("rm test")

    printFile(rootFile, "/")

    





if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)