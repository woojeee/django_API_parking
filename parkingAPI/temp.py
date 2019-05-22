import requests, xmltodict

raw_data = f'http://apis.data.go.kr/6260000/BusanPblcPrkngInfoService/getPblcPrkngInfo?serviceKey=oZg%2Fo1Rdz7BpoLQ6t3OScfDZK7horX7A9MswscbojjB2VIkr0SBjh%2FDidI3hC2Xs6wZjvPJJGj5GOFKg3b0vxg%3D%3D&pageNo=1&numOfRows=200&resultType=xml'
data = requests.get(raw_data).content
xmlObject = xmltodict.parse(data)

#xmlObject['response']['body']['items']['item']
#pkNam, pkCnt, jibunAddr, tponNum
#이름, 주차구획수, 주소, 전화번호

items = xmlObject['response']['body']['items']['item']
sortedItems = []

for item in items:
    sortedItems.append({'pkName': item['pkNam'], 'pkCount': item['pkCnt'], 'pkAddr': item['jibunAddr'], 'pNum': item['tponNum']})

print(sortedItems)