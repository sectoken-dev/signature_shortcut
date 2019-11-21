import base64

import requests


def make_and_send(url: str, hmac: str, wallet_id: str, to_address: str, value: str, feerate: int = 0,
                  total: bool = False, memo: str = '', privkey: str = ''):
    code, ips, scs, ops, prikey = make_tx(url, hmac, wallet_id, to_address, value, memo, feerate, total)
    if code != 200:
        raise BaseException(f'make tx response code {code}')

    if url.startswith('https://testnet'):
        network = 'testnet'
    else:
        network = 'mainnet'

    if prikey != "":
        privkey = prikey

    code, signed = sign_tx(ips, scs, ops, privkey, network)
    if code != 200:
        raise BaseException(f'sign tx response code {code}')
    code, txid = send_tx(url, hmac, wallet_id, signed)
    if code != 200:
        raise BaseException(f'submit tx response code {code}')
    return txid


def make_tx(url: str, hmac: str, wallet_id: str, to_address: str, value: str, memo: str = '', feerate: int = 0,
            total: bool = False):
    resp = requests.post(url + 'wallet/usdt/dotx/', headers={'HMAC': hmac},
                         json={'wallet_id': wallet_id, 'to_address': to_address, 'value': value, 'feerate': feerate,
                               'total': total, 'memo': memo})
    if resp.status_code != 200:
        raise BaseException(f'make tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        return code, None, None, None, None

    privkey = ''
    if json_resp['data']['privkey'] != "":
        privkey = base64.b64decode(json_resp['data']['privkey']).decode()

    return 200, json_resp['data']['unsigned_tx']['inputs'], json_resp['data']['unsigned_tx']['scripts'], \
           json_resp['data']['unsigned_tx']['outputs'], privkey


def sign_tx(inputs: list, scripts: list, outputs: list, privkey: str, network):
    resp = requests.post('https://internal.sectoken.io/usdt/signFirst',
                         json={'inputs': inputs, 'scripts': scripts, 'outputs': outputs, 'prikey': privkey,
                               'network': network})
    if resp.status_code != 200:
        raise BaseException(f'sign tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        return code, None

    return 200, json_resp['data']['signed_tx']


def send_tx(url: str, hmac: str, wallet_id: str, signed_tx: str):
    resp = requests.post(url + 'wallet/usdt/send/', headers={'HMAC': hmac},
                         json={'wallet_id': wallet_id, 'signed_tx': signed_tx})
    if resp.status_code != 200:
        raise BaseException(f'send tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        return code, None
    return 200, json_resp['data']['txid']
