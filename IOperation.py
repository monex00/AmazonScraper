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
        file = open("Result.txt", 'w')
        result += "TOTALE: " + str(sum)
        file.write(result)
        file.close
    
    def updateInput(self, content, prices):
        file = open("URL.txt", 'w')
        newContent = ""
        for i in range(0, len(content)):
            if i != len(content) -1:
                newContent += content[i][0] + ";" + content[i][1] + "; " + str(prices[i]) + '\n'
            else: 
                newContent += content[i][0] + ";" + content[i][1] + "; " + str(prices[i]) 
        file.write(newContent)
        file.close
