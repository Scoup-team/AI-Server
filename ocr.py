import io
import json
import os
import requests
import time
import uuid
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

def clova(file):
    api_url = os.environ["CLOVA_URL"]
    secret_key = os.environ["CLOVA_SECRET"]

    request_json = {
        'images': [
            {
                'format': 'jpg',
                'name': 'demo'
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V2',
        'timestamp': int(round(time.time() * 1000))
    }

    payload = {'message': json.dumps(request_json).encode('UTF-8')}
    files = [
        ('file', io.BufferedReader(io.BytesIO(file)))
    ]
    headers = {
        'X-OCR-SECRET': secret_key,
    }

    try:
        response = requests.request("POST", api_url, headers=headers, data = payload, files = files)
    except:
        return {"status": 500, "message": "영수증 인식에 실패했습니다."}
    json_object = json.loads(response.text)
    # print(json_object)

    final_res = {}
    try:
        result = json_object['images'][0]['receipt']['result']
        valid = result['subResults'][0]['items'][0]['price']
    except:
        return {"status": 400, "message": "올바른 영수증 형식이 아닙니다."}

    # store info
    try:
        final_res["store"] = result['storeInfo']['name']['formatted']['value']
    except:
        final_res["store"] = ''

    # card info
    try:
        final_res["cardName"] = result['paymentInfo']['cardInfo']['company']['formatted']['value']
    except:
        final_res["cardName"] = ''
    try:
        final_res["cardNum"] = result['paymentInfo']['cardInfo']['number']['formatted']['value']
    except:
        final_res["cardNum"] = ''

    # menu info
    menus = []
    for i in range(len(result['subResults'][0]['items'])):
        menu = {}
        menu['name'] = result['subResults'][0]['items'][i]['name']['formatted']['value']
        try:
            menu['count'] = result['subResults'][0]['items'][i]['count']['formatted']['value']
        except:
            menu['count'] = '1'
        menu['price'] = result['subResults'][0]['items'][i]['price']['price']['formatted']['value']

        menus.append(menu)
    
    final_res['items'] = menus
    return final_res
