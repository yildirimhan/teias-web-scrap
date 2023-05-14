import requests
from bs4 import BeautifulSoup
import boto3


def getHTML():
    URL = 'https://seffaflik.epias.com.tr/transparency/tuketim/gerceklesen-tuketim/gercek-zamanli-tuketim.xhtml'
    page = requests.get(URL)

    source = BeautifulSoup(page.content,"html.parser")

    findTables= source.find_all("tr", attrs={"role":"row"})

    i=0
    id=""
    for tableRow in findTables:
        print("i = " , i)
        findFirst = tableRow.find_all("td")
        saatlik=[]
        for link in findFirst:
            saatlik.append(link.text)
        i=i+1
        print(saatlik)
    return 0
    


if __name__ == '__main__':
    getHTML()
