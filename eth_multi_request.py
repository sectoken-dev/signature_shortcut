import base64
import requests
from config import SIGNATURE_HOST, HOST


def make_and_send(hmac: str, wallet_id: str, outputs: [dict], coin: str = 'ETH', feerate: int = 0,
                  privkey: str = '', _coin="eth"):
    make_res = make_tx(hmac, wallet_id, outputs, coin, feerate, _coin)
    make_res_privkey = base64.b64decode(make_res['privkey']).decode() if make_res['privkey'] != "" else ""
    privkey = privkey if privkey else make_res_privkey
    unsigned_tx = make_res["unsigned_tx"]
    sequence_id = make_res["sequence_id"]

    sign_res = sign_tx(unsigned_tx, privkey, _coin)
    signed_tx = sign_res["signature"]

    send_res = send_tx(hmac, wallet_id, signed_tx, sequence_id, _coin)

    return send_res.get("txid")


def make_tx(hmac: str, wallet_id: str, outputs: [dict], coin: str = 'ETH', feerate: int = 0, _coin="eth"):
    resp = requests.post(
        url=HOST + f'wallet/{_coin}/dotx/',
        headers={'HMAC': hmac},
        json={'wallet_id': wallet_id, 'outputs': outputs, 'coin': coin, 'feerate': feerate}
    )
    if resp.status_code != 200:
        raise BaseException(f'make tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        raise BaseException(f'make tx response code {code}')

    return json_resp.get("data")


def sign_tx(message: str, privkey: str, _coin="eth"):
    resp = requests.post(
        url=f'{SIGNATURE_HOST + "eth"}/signFirst',
        json={'data': message, 'prikey': privkey, 'message': True}
    )
    if resp.status_code != 200:
        raise BaseException(f'sign tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        raise BaseException(f'sign tx response code {code}')

    return json_resp.get("data")


def send_tx(hmac: str, wallet_id: str, signed_tx: str, sequnece_id: int, _coin="eth"):
    resp = requests.post(
        url=HOST + f'wallet/{_coin}/send/', headers={'HMAC': hmac},
        json={'wallet_id': wallet_id, 'signed_tx': signed_tx, "sequnece_id": sequnece_id})
    if resp.status_code != 200:
        raise BaseException(f'send tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        raise BaseException(f'send tx response code {code}')
    return json_resp.get("data")
