# signature_shortcut


### Install Requirements

pip3 install requests

### Geting Started

python3 server.py -h

    usage: server.py [-h] [-t testnet] -s server -p port

    optional arguments:

      -h, --help  show this help message and exit

      -t testnet  use test network

      -s server   server listen address

      -p port     server listen port


### Running

python3 server.py -t true -s 127.0.0.1 -p 9999


### Examples

eth_single:

```
curl "http://127.0.0.1:9999/eth_single" -H "Content-Type:application/json" -X POST -d '{"HMAC": "2E4YTcYTZmjNDEzNzNmMmNkYjZjOTYxODgxZjk=","wallet_id":"09f96f006bb97a95f461ab9208ebcaeb", "to_address": "0xa2465290580A948063B713cFf09dD550e4C4E3DB", "value":"1000","privkey":"79b0b266165f35c6c811ecfa0dd9813d3edb0076136435af8c8eb6ca656a634a"}'
```

#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/eth.single.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#eth-single-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/eth.single.en.html#submit-transaction)

btc:

```
curl "http://127.0.0.1:9999/btc" -H "Content-Type:application/json" -X POST -d '{"HMAC": "mIzMmNlZ2Mg1MTYDZODc0MTQ4ZmRlZTE2NmI=","wallet_id":"140f268a2f5322b010990eceabf1bc40","outputs":{"address":"2NDDHXRhRqCgFWWx1u9yhnfdYitv2EMZTSt","value":"1000"}, "privkey":"d923a136aa3492b52b0b75757e565f837318ab6d406481241e98aa5f09accd62"}'
```

#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/btc.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#btc-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/btc.en.html#submit-signature)

