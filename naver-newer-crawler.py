import requests

cookies = {
    'NAC': 'ohywBkAOYSW2',
    '_fbp': 'fb.1.1743671418323.800031726640063182',
    'NNB': '47KV22T4KDXGO',
    'nstore_session': '/S1JYXTnw0t0HbZHy6tcgMwI',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '156JJLWdIWaAC8I80wWWHAn.1746670185410',
    'landHomeFlashUseYn': 'Y',
    'NACT': '1',
    'nid_inf': '1954336181',
    '_fwb': '156JJLWdIWaAC8I80wWWHAn.1746670185410',
    '_ga': 'GA1.1.829390112.1746689208',
    'NIPD': '1',
    'NID_AUT': 'c3P0oATAh0HlcvlhIdcicdxfnLCxXu+80jZRQ0h88rLF8nowYujUNEX1QznZVR9P',
    'nstore_pagesession': 'jtxOLdqqrHPdSssdFZs-046608',
    'page_uid': 'jtxPNwqo1aVssvUB64ZssssstUZ-434392',
    'SRT30': '1746691920',
    '_ga_451MFZ9CFM': 'GS2.1.s1746692369$o2$g0$t1746692385$j0$l0$h0',
    'NID_SES': 'AAABhwlW7txRjymhnNbSXibhh1kw4ucPktygJNAgPN+E9QnN6N1XBLnu9sSQPMPGMAFkdKEyuoepbaEF7PwP1Wk9M5vroSr9MtfqvJ7iots6WJGshRIy7p5Fo90ajM6be0ibX/+b/PrDIKUSlGInC6Ge/Z+Bim3xWQWzO64IVBJIYMrGVv/auMzamk43IrVfnXeardPuFeTpAJlAhb46dNND7WHxnGbD5IEKZbZt/jdygUDWY2O17i9Zz9CLM+5IM8GH3ZJDzbiPOaA41MITRRJpvzOU7AOKqJgfLmpiGJPEiDfTGQs5bBrOhUzIgGscj1NT+fdKqGauVF0xL4fGuT4evv23Vx3JTl+STXFaKVSPVcHjmxVL4PEw/5pgq+Dv3myI/eDxlJyvuBSasaqvrtDS3UwkWQDg2Vs65+xOnF09t6QS6vBvGfRKFsyAcsBhphIO1O2Bgh1M7vnk1Xd0YENiapUiWQAud9hBxYOjvzGkxckNd3jLEnllnps+S9O7HS3mh9YYgv5DI4v+/iuXd6deEF8=',
    'REALESTATE': 'Thu%20May%2008%202025%2017%3A36%3A38%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'SRT5': '1746694041',
    'BUC': 'a4fG3zBF3vym2TAhloizkmez1-lMLtDoSOzP-6BAn_o=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ko;q=0.8,vi;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDY2OTMzOTgsImV4cCI6MTc0NjcwNDE5OH0.98-59aP81vDcPYnwxLuTUPZzQEiEMgkz2-CsL7_QlvE',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/113736?ms=36.5203223,127.2400895,16&a=PRE:APT&e=RETAIL&articleNo=2522970086',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    # 'cookie': 'NAC=ohywBkAOYSW2; _fbp=fb.1.1743671418323.800031726640063182; NNB=47KV22T4KDXGO; nstore_session=/S1JYXTnw0t0HbZHy6tcgMwI; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=156JJLWdIWaAC8I80wWWHAn.1746670185410; landHomeFlashUseYn=Y; NACT=1; nid_inf=1954336181; _fwb=156JJLWdIWaAC8I80wWWHAn.1746670185410; _ga=GA1.1.829390112.1746689208; NIPD=1; NID_AUT=c3P0oATAh0HlcvlhIdcicdxfnLCxXu+80jZRQ0h88rLF8nowYujUNEX1QznZVR9P; nstore_pagesession=jtxOLdqqrHPdSssdFZs-046608; page_uid=jtxPNwqo1aVssvUB64ZssssstUZ-434392; SRT30=1746691920; _ga_451MFZ9CFM=GS2.1.s1746692369$o2$g0$t1746692385$j0$l0$h0; NID_SES=AAABhwlW7txRjymhnNbSXibhh1kw4ucPktygJNAgPN+E9QnN6N1XBLnu9sSQPMPGMAFkdKEyuoepbaEF7PwP1Wk9M5vroSr9MtfqvJ7iots6WJGshRIy7p5Fo90ajM6be0ibX/+b/PrDIKUSlGInC6Ge/Z+Bim3xWQWzO64IVBJIYMrGVv/auMzamk43IrVfnXeardPuFeTpAJlAhb46dNND7WHxnGbD5IEKZbZt/jdygUDWY2O17i9Zz9CLM+5IM8GH3ZJDzbiPOaA41MITRRJpvzOU7AOKqJgfLmpiGJPEiDfTGQs5bBrOhUzIgGscj1NT+fdKqGauVF0xL4fGuT4evv23Vx3JTl+STXFaKVSPVcHjmxVL4PEw/5pgq+Dv3myI/eDxlJyvuBSasaqvrtDS3UwkWQDg2Vs65+xOnF09t6QS6vBvGfRKFsyAcsBhphIO1O2Bgh1M7vnk1Xd0YENiapUiWQAud9hBxYOjvzGkxckNd3jLEnllnps+S9O7HS3mh9YYgv5DI4v+/iuXd6deEF8=; REALESTATE=Thu%20May%2008%202025%2017%3A36%3A38%20GMT%2B0900%20(Korean%20Standard%20Time); SRT5=1746694041; BUC=a4fG3zBF3vym2TAhloizkmez1-lMLtDoSOzP-6BAn_o=',
}

params = {
    'pyeongTypeNumber': '4',
}

response = requests.get(
    'https://new.land.naver.com/api/property/complex/113736/vr/representative',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.status_code)
print(response.text)

# Save response to JSON file
import json
from datetime import datetime

# Get current timestamp for filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"naver_property_data_{timestamp}.json"

# Parse JSON response
response_data = response.json()

# Write to file with proper formatting
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(response_data, f, ensure_ascii=False, indent=4)

print(f"Data saved to {filename}")
