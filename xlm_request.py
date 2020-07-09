import base64
import requests
from config import SIGNATURE_HOST, HOST


def make_and_send(hmac: str, wallet_id, to_address="", value="", coin="xlm", memo=None, total=0,
                  privkey: str = '', _coin="xlm"):
    make_res = make_tx(hmac, wallet_id, to_address, value, coin, memo, total, _coin)
    make_res_privkey = base64.b64decode(make_res['privkey']).decode() if make_res['privkey'] else ""
    unsigned_tx = make_res["unsigned_tx"]
    sequence_id = make_res["sequence_id"]
    privkey = privkey if privkey else make_res_privkey

    sign_res = sign_tx(unsigned_tx, privkey, _coin)
    signed_tx = sign_res["signature"]

    send_res = send_tx(hmac, wallet_id, signed_tx, sequence_id, _coin)

    return send_res["txid"]


def make_tx(hmac: str, wallet_id, to_address="", value="", coin="xlm", memo=None, total=0, _coin="xlm"):
    resp = requests.post(
        url=HOST + f'wallet/{_coin}/dotx/',
        headers={'HMAC': hmac},
        json={'wallet_id': wallet_id, 'to_address': to_address, 'value': value, 'total': total, 'memo': memo,
              "coin": coin}
    )

    if resp.status_code != 200:
        raise BaseException(f'make tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        raise BaseException(f'make tx response code {code}')

    return json_resp.get("data")


def sign_tx(unsigned_tx="", privkey="", _coin: str = "xlm"):
    resp = requests.post(
        url=f'{SIGNATURE_HOST + _coin} / signFirst',
        json={"sig_payload": unsigned_tx, "prikey": privkey}
    )

    if resp.status_code != 200:
        raise BaseException(f'sign tx HTTP response code {resp.status_code}')
    json_resp = resp.json()
    code = json_resp['code']

    if code != 200:
        raise BaseException(f'sign tx response code {code}')

    return json_resp.get("data")


def send_tx(hmac: str, wallet_id: str, signed_tx: str, sequence_id: int, _coin: str = "xlm"):
    resp = requests.post(
        url=HOST + f'wallet/{_coin}/send/',
        headers={'HMAC': hmac},
        json={'wallet_id': wallet_id, 'signed_tx': signed_tx, "sequence_id": sequence_id}
    )
    if resp.status_code != 200:
        raise BaseException(f'send tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp['code']
    if code != 200:
        raise BaseException(f'send tx response code {code}')
    return json_resp.get("data")
