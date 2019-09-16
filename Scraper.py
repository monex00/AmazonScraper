import requests
from bs4 import BeautifulSoup

HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

def openFILE():
    file = open("URL.txt", 'r')
    content = file.read().split('\n')
    element= []
    for ele in content:
        element.append(ele.split(";"))
    file.close
    return element

def search(content):
    result=""
    prices=[]
    som = 0
    for i in range(len(content)):
        title = content[i][0]
        url= content[i][1]
        oldPrice = float(content[i][2])

        page = requests.get(url, headers=HEADER)
        soup = BeautifulSoup(page.content, 'html.parser')

        price = soup.find(id="priceblock_ourprice").get_text().replace(",", ".")
        price = float(price[0:5])

        if(price < oldPrice):
            diff = round(oldPrice - price, 2)
            result += title + ": " + str(price) + " " + "PREZZO DIMINUITO DI: " + str(diff) + '\n'  
        elif(price > oldPrice):
            diff = round(price - oldPrice, 2)
            result += title + ": " + str(price) + " " + "PREZZO AUMENTATO DI: "  + str(diff) + '\n'
        else:
            result += title + ": " + str(price) + " " + "PREZZO RIMASTO UGUALE " + '\n'
        
        if title.find("MIGLIORE") == -1:
            som += price
        
        print(result.split('\n')[-2]);
        prices.append(price)
    print("TOTALE: " + str(som))
    updateURL(content, prices)
    writeRes(result, som)

def updateURL(content, prices):
    file = open("URL.txt", 'w')
    newContent=""
    for i in range(0, len(content)):
        if i == len(content) -1:
            newContent += content[i][0] + ";" + content[i][1] + "; " + str(prices[i])
        else: 
            newContent += content[i][0] + ";" + content[i][1] + "; " + str(prices[i]) + '\n'
    file.write(newContent)
    file.close

def writeRes(result, sum):
    file = open("Result.txt", 'w')
    result += "TOTALE: " + str(sum)
    file.write(result)
    file.close

content = openFILE()
search(content)
