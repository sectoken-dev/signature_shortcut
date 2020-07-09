import base64
import requests
from config import SIGNATURE_HOST, HOST


def make_and_send(hmac: str, wallet_id: str, to_address: str, value: str, coin: str = 'ETH',
                  gas_price: int = 0, total: int = 0, privkey: str = '', _coin: str = 'eth_single'):
    make_res = make_tx(hmac, wallet_id, to_address, value, coin, gas_price, total, _coin)
    sequence_id = make_res['sequence_id']
    unsigned_tx = make_res['unsigned_tx']

    make_res_privkey = base64.b64decode(make_res['privkey']).decode() if make_res['privkey'] != "" else ""
    privkey = privkey if privkey else make_res_privkey

    sign_res = sign_tx(unsigned_tx, privkey)
    signed_tx = sign_res["signature"]

    send_res = send_tx(hmac, wallet_id, signed_tx, sequence_id, _coin)

    return send_res.get("txid")


def make_tx(hmac: str, wallet_id: str, to_address: str, value: str, coin: str = 'ETH', gas_price: int = 0,
            total: int = 0, _coin: str = 'eth_single'):
    resp = requests.post(
        url=HOST + f'wallet/{_coin}/dotx/',
        headers={'HMAC': hmac},
        json={'wallet_id': wallet_id, 'to_address': to_address, 'value': value, 'coin': coin, 'total': total,
              'gas_price': gas_price}
    )
    if resp.status_code != 200:
        raise BaseException(f'make tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        raise BaseException(f'make tx response code {code}')

    return json_resp.get("data")


def sign_tx(unsigned_tx: str, privkey: str):
    resp = requests.post(
        url=f'{SIGNATURE_HOST + "eth"}/signFirst',
        json={'data': unsigned_tx, 'prikey': privkey, 'message': False}
    )
    if resp.status_code != 200:
        raise BaseException(f'sign tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        raise BaseException(f'sign tx response code {code}')

    return json_resp.get("data")


def send_tx(hmac: str, wallet_id: str, signed_tx: str, sequence_id: int, _coin: str = "eth_sigle"):
    resp = requests.post(
        url=HOST + f'wallet/{_coin}/send/', headers={'HMAC': hmac},
        json={'wallet_id': wallet_id, 'signed_tx': signed_tx, "sequence_id": sequence_id}
    )
    if resp.status_code != 200:
        raise BaseException(f'send tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        raise BaseException(f'send tx response code {code}')
    return json_resp.get("data")
