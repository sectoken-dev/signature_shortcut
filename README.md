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

#### ETH_SINGLE

request:

```
curl "http://127.0.0.1:9999/eth_single" -H "Content-Type:application/json" -X POST -d '{"HMAC": "2E4YTcYTZmjNDEzNzNmMmNkYjZjOTYxODgxZjk=","wallet_id":"09f96f006bb97a95f461ab9208ebcaeb", "to_address": "0xa2465290580A948063B713cFf09dD550e4C4E3DB", "value":"1000","privkey":"79b0b266165f35c6c811ecfa0dd9813d3edb0076136435af8c8eb6ca656a634a"}'
```

response:

```
{
     "code": 200, 
     "data": {
         "txid": "0xc03c4a9dba55a239c165a4cbcf1eddcfa9cc7673ea1c6d492105d0145ff6f0ee"
     }
}
``` 


#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/eth.single.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#eth-single-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/eth.single.en.html#submit-transaction)

#### ETH_MULTI:

request:

```
curl "http://127.0.0.1:9999/eth" -H "Content-Type:application/json" -X POST -d '{"HMAC": "2E4YTcYTZmjNDEzNzNmMmNkYjZjOTYxODgxZjk=","wallet_id":"09f96f006bb97a95f461ab9208ebcaeb", "to_address": "0xa2465290580A948063B713cFf09dD550e4C4E3DB", "value":"1000","privkey":"79b0b266165f35c6c811ecfa0dd9813d3edb0076136435af8c8eb6ca656a634a"}'
```

response:

```
{
    "code": 200,
    "data": {
        "is_sent": true,
        "txid": "0xc99629ab2d9472aea0450f3f881e07d5c3d8d9444131430df2e7fb3a95dbb44b"
    }
}
```
#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/eth.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#l#eth-multi-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/eth.en.html#submit-signature)


#### BTC

request:
```
curl "http://127.0.0.1:9999/btc" -H "Content-Type:application/json" -X POST -d '{"HMAC": "mIzMmNlZ2Mg1MTYDZODc0MTQ4ZmRlZTE2NmI=","wallet_id":"140f268a2f5322b010990eceabf1bc40","outputs":{"address":"2NDDHXRhRqCgFWWx1u9yhnfdYitv2EMZTSt","value":"1000"}, "privkey":"d923a136aa3492b52b0b75757e565f837318ab6d406481241e98aa5f09accd62"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "ee1e39a44ed45db1693123439cb496c300194221a644a04883933c8adf141b8c",
        "is_sent": true
    }
}
```

#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/btc.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#btc-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/btc.en.html#submit-signature)


#### LTC

request:

```
curl "http://127.0.0.1:9999/ltc" -H "Content-Type:application/json" -X POST -d '{"HMAC": "mIzMmNlZ2Mg1MTYDZODc0MTQ4ZmRlZTE2NmI=","wallet_id":"140f268a2f5322b010990eceabf1bc40","outputs":{"address":"2NDDHXRhRqCgFWWx1u9yhnfdYitv2EMZTSt","value":"1000"}, "privkey":"d923a136aa3492b52b0b75757e565f837318ab6d406481241e98aa5f09accd62"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "ee1e39a44ed45db1693123439cb496c300194221a644a04883933c8adf141b8c",
        "is_sent": true
    }
}
```

#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/ltc.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#ltc-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/ltc.en.html#submit-signature)


#### BCH
request:

```
curl "http://127.0.0.1:9999/bch" -H "Content-Type:application/json" -X POST -d '{"HMAC": "mIzMmNlZ2Mg1MTYDZODc0MTQ4ZmRlZTE2NmI=","wallet_id":"140f268a2f5322b010990eceabf1bc40","outputs":{"address":"bchtest:pzve7xw36mdpffwwnyw6fw8t40y20n0am5kuwz8cwt","value":"1000"}, "privkey":"d923a136aa3492b52b0b75757e565f837318ab6d406481241e98aa5f09accd62"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "2b5c30a5253b6567ffaa4b338e9a442a94cb5be74b525b81708cd3c9563a8b92",
        "is_sent": true
    }
}
```

#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/bch.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#bch-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/bch.en.html#submit-signature)

#### USDT
request:

```
curl "http://127.0.0.1:9999/usdt" -H "Content-Type:application/json" -X POST -d '{"HMAC": "mIzMmNlZ2Mg1MTYDZODc0MTQ4ZmRlZTE2NmI=","wallet_id":"140f268a2f5322b010990eceabf1bc40","to_address":"2NDDHXRhRqCgFWWx1u9yhnfdYitv2EMZTSt","value":"1000", "privkey":"d923a136aa3492b52b0b75757e565f837318ab6d406481241e98aa5f09accd62"}'
```

response:

```
{
  "code": 200,
  "data": {
    "txid": "1c93e587fb3193969fb1f775835f07fb4517ffd24afd36df4b118ab52c9ba63f",
    "is_sent": true
  }
}
```

#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/usdt.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#usdt-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/usdt.en.html#submit-signature)





