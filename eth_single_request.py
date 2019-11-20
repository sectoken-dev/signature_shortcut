import base64

import requests
from requests.exceptions import HTTPError


def make_and_send(url: str, hmac: str, wallet_id: str, to_address: str, value: str, coin_type: str = 'ETH',
                  feerate: int = 0,
                  total: bool = False, privkey: str = ''):
    code, unsigned, prikey = make_tx(url, hmac, wallet_id, to_address, value, coin_type, feerate, total)
    if code != 200:
        raise BaseException(f'make tx response code {code}')

    if prikey != "":
        privkey = prikey

    code, signed = sign_tx(unsigned, privkey)
    if code != 200:
        raise BaseException(f'sign tx response code {code}')

    code, txid = send_tx(url, hmac, wallet_id, signed)
    if code != 200:
        raise BaseException(f'submit tx response code {code}')
    return txid


def make_tx(url: str, hmac: str, wallet_id: str, to_address: str, value: str, coin_type: str = 'ETH', feerate: int = 0,
            total: bool = False):
    resp = requests.post(url + 'wallet/eth_single/dotx/', headers={'HMAC': hmac},
                         json={'wallet_id': wallet_id, 'to_address': to_address, 'value': value, 'coin_type': coin_type,
                               'feerate': feerate, 'total': total})
    if resp.status_code != 200:
        raise HTTPError(f'make tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        return code, None, None

    privkey = ''
    if json_resp['data']['privkey'] != "":
        privkey = base64.b64decode(json_resp['data']['privkey']).decode()
    return 200, json_resp['data']['unsigned_tx'], privkey


def sign_tx(unsigned_tx: str, privkey: str):
    resp = requests.post('https://internal.sectoken.io/eth/signFirst',
                         json={'data': unsigned_tx, 'prikey': privkey, 'message': False})
    if resp.status_code != 200:
        raise HTTPError(f'sign tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        return code, None

    return 200, json_resp['data']['tx']


def send_tx(url: str, hmac: str, wallet_id: str, signed_tx: str):
    resp = requests.post(url + 'wallet/eth_single/send/', headers={'HMAC': hmac},
                         json={'wallet_id': wallet_id, 'signed_tx': signed_tx})
    if resp.status_code != 200:
        raise HTTPError(f'send tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        return code, None
    return 200, json_resp['data']['txid']
