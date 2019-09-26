import requests
from bs4 import BeautifulSoup

HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

class Scraper:
    def __init__(self, content, ioperation, isSingleSearch = False):
        self.ioperation = ioperation
        self.content = content

        self.result = ""    #string of all results
        self.som = 0    #total cost of components
        self.prices = []    #array of new prices

        if(isSingleSearch):
            self.__singleProcessing()
        else:
            self.__processing()

    def __singleProcessing(self):
        title = self.content[0]
        url= self.content[1]
        oldPrice = float(self.content[2])

        price = self.__bs4Operation(url) 

        self.__makeResult(oldPrice, price, title)

    def __processing(self,):
        for i in range(len(self.content)):
            title = self.content[i][0]
            url= self.content[i][1]
            oldPrice = float(self.content[i][2])

            price = self.__bs4Operation(url)

            self.__makeResult(oldPrice, price, title)
        self.som = round(self.som, 2)
        self.__manageResult()

    def __bs4Operation(self, url):
        page = requests.get(url, headers=HEADER)
        soup = BeautifulSoup(page.content, 'html.parser')

        price = soup.find(id="priceblock_ourprice").get_text().replace(",", ".")
        price = float(price[0:5])

        return price

    def __makeResult(self, oldPrice, price, title):
        if(price < oldPrice):
            diff = round(oldPrice - price, 2)
            self.result += title + ": " + str(price) + " " + "PREZZO DIMINUITO DI: " + str(diff) + '\n'  
        elif(price > oldPrice):
            diff = round(price - oldPrice, 2)
            self.result += title + ": " + str(price) + " " + "PREZZO AUMENTATO DI: "  + str(diff) + '\n'
        else:
            self.result += title + ": " + str(price) + " " + "PREZZO RIMASTO UGUALE " + '\n'
        
        if title.find("MIGLIORE") == -1:
            self.som += price
        
        print(self.result.split('\n')[-2]);
        self.prices.append(price)
    
    def __manageResult(self):
        print("TOTALE: " + str(self.som))
        self.ioperation.updateInput(self.content, self.prices)
        self.ioperation.setResult(self.result, self.som)

