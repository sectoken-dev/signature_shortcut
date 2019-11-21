import base64

import requests


def make_and_send(url: str, hmac: str, wallet_id: str, to_address: str, value: str, coin_type: str = 'ETH',
                  feerate: int = 0, privkey: str = ''):
    code, message, prikey = make_tx(url, hmac, wallet_id, to_address, value, coin_type, feerate)
    if code != 200:
        raise BaseException(f'make tx response code {code}')

    if prikey != "":
        privkey = prikey

    code, sig = sign_tx(message, privkey)
    if code != 200:
        raise BaseException(f'sign tx response code {code}')

    code, txid = send_tx(url, hmac, wallet_id, message, sig)
    if code != 200:
        raise BaseException(f'submit tx response code {code}')
    return txid


def make_tx(url: str, hmac: str, wallet_id: str, to_address: str, value: str, coin_type: str = 'ETH', feerate: int = 0):
    resp = requests.post(url + 'wallet/eth/dotx/', headers={'HMAC': hmac},
                         json={'wallet_id': wallet_id, 'to_address': to_address, 'value': value, 'coin_type': coin_type,
                               'feerate': feerate})
    if resp.status_code != 200:
        raise BaseException(f'make tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        return code, None, None

    privkey = ''
    if json_resp['data']['privkey'] != "":
        privkey = base64.b64decode(json_resp['data']['privkey']).decode()
    return 200, json_resp['data']['data'], privkey


def sign_tx(message: str, privkey: str):
    resp = requests.post('https://internal.sectoken.io/eth/signFirst',
                         json={'data': message, 'prikey': privkey, 'message': True})
    if resp.status_code != 200:
        raise BaseException(f'sign tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        return code, None

    return 200, json_resp['data']['signature']


def send_tx(url: str, hmac: str, wallet_id: str, data: str, signature: str):
    resp = requests.post(url + 'wallet/eth_single/send/', headers={'HMAC': hmac},
                         json={'wallet_id': wallet_id, 'data': data, 'signature': signature})
    if resp.status_code != 200:
        raise BaseException(f'send tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        return code, None
    return 200, json_resp['data']['txid']
