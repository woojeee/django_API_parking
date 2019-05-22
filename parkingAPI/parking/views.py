from django.shortcuts import render
import requests, xmltodict
import os, json

# Create your views here.

#API key 안올라가게, config json파일 & git ignore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'parkingAPI/config/index.json')) as f: secrets = json.loads(f.read())

APIKEY = secrets['APIKEY']['KEY']

#xmlObject['response']['body']['items']['item']
#pkNam, pkCnt, jibunAddr, tponNum
#이름, 주차구획수, 주소, 전화번호

#requests 쓰기 때문에 request로 인자 바꿈
def home(request):
    raw_data = f'http://apis.data.go.kr/6260000/BusanPblcPrkngInfoService/getPblcPrkngInfo?serviceKey={APIKEY}&pageNo=1&numOfRows=200&resultType=xml'
    data = requests.get(raw_data).content
    xmlObject = xmltodict.parse(data)
    items = xmlObject['response']['body']['items']['item']
    sortedItems = []

    for item in items:
        sortedItems.append({'pkName': item['pkNam'], 'pkCount': item['pkCnt'], 'pkAddr': item['jibunAddr'], 'pNum': item['tponNum']})

    return render(request, 'home.html', { 'items' : sortedItems })