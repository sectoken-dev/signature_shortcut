import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from btc_request import make_and_send as b_make_and_send
from eth_single_request import make_and_send as es_make_and_send


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

        if self.path == '/eth_single':
            self.handle_eth_single(json_body)
        elif self.path == '/btc':
            self.handle_btc(json_body)

        self.send_response(404)
        return

    def handle_eth_single(self, json_body):
        hmac = json_body.get('HMAC')
        wallet_id = json_body.get('wallet_id')
        to_address = json_body.get('to_address')
        value = str(json_body.get('value', ''))
        coin_type = json_body.get('coin_type', 'ETH')
        feerate = json_body.get('feerate', 0)
        total = json_body.get('total', False)
        privkey = json_body.get('privkey', '')

        if not (hmac and wallet_id and to_address and value):
            self.send_response(400)
            return

        try:
            txid = es_make_and_send(URL, hmac, wallet_id, to_address, value, coin_type, feerate, total, privkey)
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
            txid = b_make_and_send(URL, hmac, wallet_id, outputs, feerate, total, memo, privkey)
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
