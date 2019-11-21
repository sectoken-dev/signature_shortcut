import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from btc_request import make_and_send as btc_make_and_send
from ltc_request import make_and_send as ltc_make_and_send
from usdt_request import make_and_send as usdt_make_and_send
from eth_single_request import make_and_send as eths_make_and_send
from eth_multi_request import make_and_send as ethm_make_and_send


class SignatureShortcut(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        self._set_headers()

        body = self.rfile.read(int(self.headers.get('Content-Length', 0)))
        try:
            json_body = json.loads(body)
        except:
            self.send_response(400)
            return

        route = {
            '/eth_single': self.handle_eth_single,
            '/eth': self.handle_eth_multi,
            '/btc': self.handle_btc,
            '/ltc': self.handle_ltc,
            '/usdt': self.handle_usdt,
        }
        handle = route.get(self.path)
        if handle is not None:
            handle(json_body)
            return

        self.send_response(404)
        return 

    def handle_eth_single(self, json_body):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        to_address = json_body.get('to_address')
        value = str(json_body.get('value', '0'))
        coin_type = json_body.get('coin_type', 'ETH')
        feerate = json_body.get('feerate', 0)
        total = json_body.get('total', False)
        privkey = json_body.get('privkey', '')

        if not (hmac and wallet_id and to_address and value):
            self.send_response(400)
            return

        try:
            txid = eths_make_and_send(URL, hmac, wallet_id, to_address, value, coin_type, feerate, total, privkey)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_eth_multi(self, json_body):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        to_address = json_body.get('to_address')
        value = str(json_body.get('value', '0'))
        coin_type = json_body.get('coin_type', 'ETH')
        feerate = json_body.get('feerate', 0)
        privkey = json_body.get('privkey', '')
        if not (hmac and wallet_id and to_address and value):
            self.send_response(400)
            return

        try:
            txid = ethm_make_and_send(URL, hmac, wallet_id, to_address, value, coin_type, feerate, privkey)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_btc(self, json_body):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        outputs = json_body.get('outputs')
        feerate = json_body.get('feerate', 0)
        total = json_body.get('total', False)
        privkey = json_body.get('privkey', '')
        memo = json_body.get('memo', '')
        if not (hmac and wallet_id and outputs):
            self.send_response(400)
            return

        try:
            txid = btc_make_and_send(URL, hmac, wallet_id, outputs, feerate, total, memo, privkey)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_ltc(self, json_body):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        outputs = json_body.get('outputs')
        feerate = json_body.get('feerate', 0)
        total = json_body.get('total', False)
        privkey = json_body.get('privkey', '')
        memo = json_body.get('memo', '')
        if not (hmac and wallet_id and outputs):
            self.send_response(400)
            return

        try:
            txid = ltc_make_and_send(URL, hmac, wallet_id, outputs, feerate, total, memo, privkey)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())

    def handle_usdt(self, json_body):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        to_address = json_body.get('to_address')
        value = str(json_body.get('value', '0'))
        feerate = json_body.get('feerate', 0)
        total = json_body.get('total', False)
        privkey = json_body.get('privkey', '')
        memo = json_body.get('memo', '')
        if not (hmac and wallet_id and to_address, value):
            self.send_response(400)
            return

        try:
            txid = usdt_make_and_send(URL, hmac, wallet_id, to_address, value, feerate, total, memo, privkey)
        except BaseException as e:
            self.wfile.write(json.dumps({'code': 500, 'txid': '', 'error': str(e)}).encode())
            return

        self.wfile.write(json.dumps({'code': 200, 'txid': txid, 'error': ''}).encode())


if __name__ == '__main__':
    URL = 'https://testnet.sectoken.io/'

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', metavar='testnet', default=False, dest='testnet', help='use test network')
    parser.add_argument('-s', metavar='server', dest='server', required=True, help='server listen address')
    parser.add_argument('-p', metavar='port', dest='port', required=True, help='server listen port')
    args = parser.parse_args()
    if not bool(args.testnet):
        URL = 'main net url'

    server = HTTPServer((args.server, int(args.port)), SignatureShortcut)
    server.serve_forever()
