import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from coin_request import make_and_send as coin_make_and_send
from usdt_request import make_and_send as usdt_make_and_send
from eth_single_request import make_and_send as eths_make_and_send
from eth_multi_request import make_and_send as ethm_make_and_send
from eos_request import make_and_send as eos_make_and_send
from trx_request import make_and_send as trx_make_and_send
from xrp_request import make_and_send as xrp_make_and_send
from xlm_request import make_and_send as xlm_make_and_send
from config import SERVER, PORT


class SignatureShortcut(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        body, json_body = self.rfile.read(int(self.headers.get('Content-Length', 0))), dict()
        try:
            json_body = json.loads(body)
        except Exception as e:
            print(e)
            self.send_response(400)
            return

        route = {
            '/bch': self.handle_coin,
            '/btc': self.handle_coin,
            '/dash': self.handle_coin,
            '/ltc': self.handle_coin,
            '/usdt': self.handle_usdt,
            '/eth_single': self.handle_eth_single,
            '/eth': self.handle_eth_multi,
            '/trx': self.handle_trx,
            '/eos': self.handle_eos,
            '/xrp': self.handle_xrp,
            '/xlm': self.handle_xlm
        }
        handle = route.get(self.path, None)
        if handle is not None:
            json_body["_coin"] = self.path[1:]
            # noinspection PyArgumentList
            return handle(json_body=json_body)
        self.send_response(404)
        return

    def handle_eth_single(self, json_body: dict):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        to_address = json_body.get('to_address')
        value = str(json_body.get('value', '0'))
        coin = json_body.get('coin', 'ETH')
        gas_price = json_body.get('gas_price', 0)
        total = json_body.get('total', 0)
        privkey = json_body.get('privkey', '')
        _coin = json_body.get("_coin")

        if not (hmac and wallet_id and to_address and value):
            self.send_response(400)
            return

        try:
            txid = eths_make_and_send(hmac, wallet_id, to_address, value, coin, gas_price, total, privkey, _coin)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_eth_multi(self, json_body: dict):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        outputs = json_body.get('outputs')
        coin = json_body.get('coin', 'ETH')
        feerate = json_body.get('feerate', 0)
        privkey = json_body.get('privkey', '')
        _coin = json_body.get("_coin")
        if not (hmac and wallet_id and outputs):
            self.send_response(400)
            return

        try:
            txid = ethm_make_and_send(hmac, wallet_id, outputs, coin, feerate, privkey, _coin)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_usdt(self, json_body: dict):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        to_address = json_body.get('to_address')
        value = str(json_body.get('value', '0'))
        feerate = json_body.get('feerate', 0)
        total = json_body.get('total', False)
        privkey = json_body.get('privkey', '')
        confirm_target = json_body.get("confirm_target", 0)
        memo = json_body.get('memo', '')
        _coin = json_body.get("_coin")
        if not (hmac and wallet_id and to_address and value):
            self.send_response(400)
            return

        try:
            txid = usdt_make_and_send(hmac, wallet_id, to_address, value, feerate, total, memo, privkey, confirm_target,
                                      _coin)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_coin(self, json_body: dict):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        outputs = json_body.get('outputs')
        feerate = json_body.get('feerate', 0)
        total = json_body.get('total', 0)
        privkey = json_body.get('privkey', '')
        memo = json_body.get('memo', '')
        confirm_target = json_body.get("confirm_target", 0)
        _coin = json_body.get("_coin", "btc")
        if not (hmac and wallet_id and outputs):
            self.send_response(400)
            return

        try:
            txid = coin_make_and_send(hmac, wallet_id, outputs, feerate, total, memo, privkey, confirm_target, _coin)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_eos(self, json_body: dict):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        outputs = json_body.get('outputs')
        coin = json_body.get('coin', 'eos')
        privkey = json_body.get('privkey', '')
        memo = json_body.get('memo', '')
        total = json_body.get('total', 0)
        _coin = json_body.get("_coin")
        if not (hmac and wallet_id and outputs):
            self.send_response(400)
            return

        try:
            txid = eos_make_and_send(hmac, wallet_id, outputs, coin, memo, privkey, total, _coin)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_trx(self, json_body: dict):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        to_address = json_body.get('to_address')
        value = json_body.get('value')
        coin = json_body.get('coin', 'eos')
        privkey = json_body.get('privkey', '')
        memo = json_body.get('memo', '')
        total = json_body.get('total', 0)
        _coin = json_body.get("_coin")
        if not (hmac and wallet_id and to_address and value):
            self.send_response(400)
            return

        try:
            txid = trx_make_and_send(hmac, wallet_id, to_address, value, coin, memo, total, privkey, _coin)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_xrp(self, json_body: dict):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        to_address = json_body.get('to_address')
        value = json_body.get('value')
        coin = json_body.get('coin', 'xrp')
        privkey = json_body.get('privkey', '')
        memo = json_body.get('memo', '')
        total = json_body.get('total', 0)
        _coin = json_body.get("_coin")
        if not (hmac and wallet_id and to_address and value):
            self.send_response(400)
            return

        try:
            txid = xrp_make_and_send(hmac, wallet_id, to_address, value, coin, memo, total, privkey, _coin)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_xlm(self, json_body: dict):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        to_address = json_body.get('to_address')
        value = json_body.get('value')
        coin = json_body.get('coin', 'xlm')
        privkey = json_body.get('privkey', '')
        memo = json_body.get('memo', '')
        total = json_body.get('total', 0)
        _coin = json_body.get("_coin")
        if not (hmac and wallet_id and to_address and value):
            self.send_response(400)
            return

        try:
            txid = xlm_make_and_send(hmac, wallet_id, to_address, value, coin, memo, total, privkey, _coin)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())


if __name__ == '__main__':
    server = HTTPServer((SERVER, int(PORT)), SignatureShortcut)
    print(f"server already run at http://{SERVER}:{PORT}")
    server.serve_forever()
