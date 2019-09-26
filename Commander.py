from abc import ABC, abstractmethod
from IOperation import IOperation
from Scraper import Scraper

class ABScommander(ABC):
    
    def execute(self,):
        pass

class SingleSearchCommand(ABScommander):
    def __init__(self):
        self.ioperation = IOperation()

    def execute(self):
        content = self.ioperation.getSingleInput();
        scraper = Scraper(content, self.ioperation, True)

class MultipleSearchCommand(ABScommander):
    def __init__(self):
        self.ioperation = IOperation()

    def execute(self):
        content = self.ioperation.getInput();
        scraper = Scraper(content, self.ioperation)