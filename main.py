from Commander import *
import sys


if (len(sys.argv) == 1):
    print("USAGE: \n    -s      for a single search(do not explicate the name of component)\n    -a      to search all components in the URL file\n")
    print("GOING TO SCAN ALL THE ELEMENTS\n\n")
    sys.argv.append("-a")

commandMap = {
    "-s" : SingleSearchCommand(),
    "-a" : MultipleSearchCommand()
}

commandMap[sys.argv[1]].execute()
