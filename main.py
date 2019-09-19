from IOperation import IOperation
from Scraper import Scraper

ioperation = IOperation()
content = ioperation.getInput() 
scraper = Scraper(content, ioperation)
