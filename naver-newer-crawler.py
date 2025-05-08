import json
import requests

cookies = {
    'NAC': '6C1DBkgzm7PeB',
    'NNB': 'T3XSKNAAZMKGQ',
    'NACT': '1',
    'SRT30': '1746715814',
    'SRT5': '1746715814',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '215ROqp3Bs8ieBqZ7IraEIP.1746715828004',
    'landHomeFlashUseYn': 'Y',
    'REALESTATE': 'Thu%20May%2008%202025%2023%3A50%3A50%20GMT%2B0900%20(Korean%20Standard%20Time)',
    '_fwb': '215ROqp3Bs8ieBqZ7IraEIP.1746715828004',
    'BUC': 'ZUBt4OOcP2LzMNy3wmsTGZQ2vyopY5Xy94tP4qbxwS0=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko;q=0.8,vi;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDY3MTU4NTAsImV4cCI6MTc0NjcyNjY1MH0.vMoxneiFu0uGR01utFB2IHNHabweYTry0emKS6P1Bqg',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/search?ms=37.3618878,127.1111231,16&a=APT:ABYG:JGC:PRE&e=RETAIL',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'NAC=6C1DBkgzm7PeB; NNB=T3XSKNAAZMKGQ; NACT=1; SRT30=1746715814; SRT5=1746715814; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=215ROqp3Bs8ieBqZ7IraEIP.1746715828004; landHomeFlashUseYn=Y; REALESTATE=Thu%20May%2008%202025%2023%3A50%3A50%20GMT%2B0900%20(Korean%20Standard%20Time); _fwb=215ROqp3Bs8ieBqZ7IraEIP.1746715828004; BUC=ZUBt4OOcP2LzMNy3wmsTGZQ2vyopY5Xy94tP4qbxwS0=',
}

response = requests.get(
    'https://new.land.naver.com/api/articles/complex/2645?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=1&complexNo=2645&buildingNos=&areaNos=&type=list&order=prc',
    cookies=cookies,
    headers=headers,
)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data
    data = response.json()
    
    # Write the JSON data to a file
    with open('naver_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Data has been saved to naver_data.json")
else:
    print(f"Failed to get data. Status code: {response.status_code}")

