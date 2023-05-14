import requests
from bs4 import BeautifulSoup
import boto3

def getHTML():
    URL = 'https://seffaflik.epias.com.tr/transparency/piyasalar/gop/ptf.xhtml'
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
        try:
            id=str(saatlik[0]+saatlik[1])
            putDB(id,saatlik[0],saatlik[1],saatlik[2],saatlik[3],saatlik[4])
        except:
            putDB("error",0,0,0,0,0)
    return 0
    

def putDB(id, date, time, ptf_TL, ptf_USD, ptf_EUR):
    # this will create dynamodb resource object and
    # here dynamodb is resource name
    client = boto3.resource('dynamodb')

    # this will search for dynamoDB table 
    # your table name may be different
    table = client.Table("KPTF")
    print(table.table_status)

    table.put_item(Item= {
        'id': id,
        'date':  date, 
        'time': time, 
        'ptfEUR': ptf_EUR, 
        'ptfTL': ptf_TL,
        'ptfUSD': ptf_USD
    })

def lambda_handler(event, context):
    getHTML()
    return    {
        'result': "KPTFs are imported to DynamoDB"

    }
