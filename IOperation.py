import os.path
import sys

INPUT = "files/URL.txt"
OUTPUT = "files/Result.txt"

class IOperation:
    def __init__(self, inPath = INPUT , outPath = OUTPUT):
        if(os.path.exists(inPath)):
            self.inPath = inPath
            self.outPath = outPath
        else:
            sys.exit("FILE: " + inPath + " does not exists")
    
    def getInput(self):
        file = open(self.inPath, 'r')
        content = file.read().split('\n')
        element= []
        for ele in content:
            element.append(ele.split(";"))
        file.close
        return element

    def setResult(self, result, sum):
        file = open(self.outPath, 'w')
        result += "TOTALE: " + str(sum)
        file.write(result)
        file.close
    
    def updateInput(self, content, prices):
        file = open(self.inPath, 'w')
        newContent = ""
        for i in range(0, len(content)):
            if i != len(content) -1:
                newContent += content[i][0] + ";" + content[i][1] + "; " + str(prices[i]) + '\n'
            else: 
                newContent += content[i][0] + ";" + content[i][1] + "; " + str(prices[i]) 
        file.write(newContent)
        file.close

    def getSingleInput(self):
        file = open(self.inPath, 'r')
        content = file.read().split('\n')
        choise = 0
        for index in range(0,len(content)):
            ele = content[index].split(';')
            print(str(index) + ": " + ele[0])

        choise = input("inserisci il numero scelto: ")
        line = content[int(choise)]
        element= line.split(';')
        file.close
        return element