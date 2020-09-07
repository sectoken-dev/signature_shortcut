import base64
import requests
from .config import NETWORK, SIGNATURE_HOST, HOST


def make_and_send(hmac: str, wallet_id: str, outputs: dict, feerate: int = 0, total: int = 0,
                  memo: str = '', privkey: str = '', confirm_target: int = 0, _coin="btc"):
    make_res = make_tx(hmac, wallet_id, outputs, memo, feerate, confirm_target, total, _coin)

    make_res_privkey = base64.b64decode(make_res['privkey']).decode() if make_res['privkey'] else ""
    privkey = privkey if privkey else make_res_privkey
    inputs = make_res['unsigned_tx']['inputs']
    scripts = make_res['unsigned_tx']['scripts']
    outputs = make_res['unsigned_tx']['outputs']
    sequence_id = make_res["sequence_id"]

    sign_res = sign_tx(inputs, scripts, outputs, privkey, NETWORK, _coin)
    signed_tx = sign_res.get("signed_tx")

    send_res = send_tx(hmac, wallet_id, signed_tx, sequence_id, _coin)

    return send_res.get("txid")


def make_tx(hmac: str, wallet_id: str, outputs: dict, memo: str = '', feerate: int = 0,
            confirm_target: int = 0, total: int = 0, _coin: str = "btc"):
    resp = requests.post(
        url=HOST + f'wallet/{_coin}/dotx/',
        headers={'HMAC': hmac},
        json={'wallet_id': wallet_id, 'outputs': outputs, 'feerate': feerate, 'total': total,
              'memo': memo, "confirm_target": confirm_target}
    )

    if resp.status_code != 200:
        raise BaseException(f'make tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    code = json_resp.get("code")
    if code != 200:
        raise BaseException(f'make tx response code {code}')

    return json_resp.get("data")


def sign_tx(inputs: list, scripts: list, outputs: list, privkey: str, network: str, _coin: str = "btc"):
    resp = requests.post(
        url=f'{SIGNATURE_HOST + _coin}/signFirst',
        json={'inputs': inputs, 'scripts': scripts, 'outputs': outputs, 'prikey': privkey, 'network': network}
    )
    if resp.status_code != 200:
        raise BaseException(f'sign tx HTTP response code {resp.status_code}')

    json_resp = resp.json()
    if json_resp.get("code") != 200:
        raise BaseException(f'sign tx response code {json_resp.get("code")}')

    return json_resp.get("data")


def send_tx(hmac: str, wallet_id: str, signed_tx: str, sequence_id: int, _coin: str = "btc"):
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
        raise BaseException(f'send tx response code {json_resp.get("code")}')
    return json_resp.get("data")
