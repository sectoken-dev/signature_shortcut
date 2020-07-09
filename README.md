# signature_shortcut


### Install Requirements

pip3 install requests

### Geting Started

vim config.py
    
  optional arguments:

    HOST            host of the deployed service

    NETWORK         use test or main network

    SIGNATIRE_HOST  host of the signature service         

    SERVER          server listen address

    PORT            server listen port


### Running

python3 server.py


### Examples

#### BTC

request:
```
curl "http://127.0.0.1:9999/btc" -H "Content-Type:application/json" -X POST -d '{"HMAC": "mIzMmNlZ2Mg1MTYDZODc0MTQ4ZmRlZTE2NmI=","wallet_id":"140f268a2f5322b010990eceabf1bc40","outputs":[{"address":"2NDDHXRhRqCgFWWx1u9yhnfdYitv2EMZTSt","value":"1000"}], "privkey":"d923a136aa3492b52b0b75757e565f837318ab6d406481241e98aa5f09accd62"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "ee1e39a44ed45db1693123439cb496c300194221a644a04883933c8adf141b8c",
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
curl "http://127.0.0.1:9999/ltc" -H "Content-Type:application/json" -X POST -d '{"HMAC": "mIzMmNlZ2Mg1MTYDZODc0MTQ4ZmRlZTE2NmI=","wallet_id":"140f268a2f5322b010990eceabf1bc40","outputs":[{"address":"2NDDHXRhRqCgFWWx1u9yhnfdYitv2EMZTSt","value":"1000"}], "privkey":"d923a136aa3492b52b0b75757e565f837318ab6d406481241e98aa5f09accd62"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "ee1e39a44ed45db1693123439cb496c300194221a644a04883933c8adf141b8c",
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
curl "http://127.0.0.1:9999/bch" -H "Content-Type:application/json" -X POST -d '{"HMAC": "mIzMmNlZ2Mg1MTYDZODc0MTQ4ZmRlZTE2NmI=","wallet_id":"140f268a2f5322b010990eceabf1bc40","outputs":[{"address":"bchtest:pzve7xw36mdpffwwnyw6fw8t40y20n0am5kuwz8cwt","value":"1000"}], "privkey":"d923a136aa3492b52b0b75757e565f837318ab6d406481241e98aa5f09accd62"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "2b5c30a5253b6567ffaa4b338e9a442a94cb5be74b525b81708cd3c9563a8b92",
    }
}
```

#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/bch.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#bch-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/bch.en.html#submit-signature)

#### DASH
request:

```
curl "http://127.0.0.1:9999/dash" -H "Content-Type:application/json" -X POST -d '{"HMAC": "mIzMmNlZ2Mg1MTYDZODc0MTQ4ZmRlZTE2NmI=","wallet_id":"140f268a2f5322b010990eceabf1bc40","outputs":[{"address":"8s3KT2Tyk7MVY4V5H9y6rPUwBUjuynxBAc","value":"1000"}], "privkey":"d923a136aa3492b52b0b75757e565f837318ab6d406481241e98aa5f09accd62"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "2b5c30a5253b6567ffaa4b338e9a442a94cb5be74b525b81708cd3c9563a8b92",
    }
}
```

#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/dash.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#dash-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/dash.en.html#submit-signature)


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
  }
}
```

#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/usdt.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#usdt-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/usdt.en.html#submit-signature)






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

* [build transaction](https://sectoken-dev.github.io/docs/v1/eth.single.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/v1/tools.en.html#eth-single-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/v1/eth.single.en.html#submit-transaction)

#### ETH_MULTI

request:

```
curl "http://127.0.0.1:9999/eth" -H "Content-Type:application/json" -X POST -d '{"HMAC": "2E4YTcYTZmjNDEzNzNmMmNkYjZjOTYxODgxZjk=","wallet_id":"09f96f006bb97a95f461ab9208ebcaeb", "to_address": "0xa2465290580A948063B713cFf09dD550e4C4E3DB", "value":"1000","privkey":"79b0b266165f35c6c811ecfa0dd9813d3edb0076136435af8c8eb6ca656a634a"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "0xc99629ab2d9472aea0450f3f881e07d5c3d8d9444131430df2e7fb3a95dbb44b"
    }
}
```
#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/eth.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#l#eth-multi-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/eth.en.html#submit-signature)



#### TRX

request:

```
curl "http://127.0.0.1:9999/trx" -H "Content-Type:application/json" -X POST -d '{"HMAC": "2E4YTcYTZmjNDEzNzNmMmNkYjZjOTYxODgxZjk=","wallet_id":"09f96f006bb97a95f461ab9208ebcaeb", "to_address": "TQ4UFMeQbSVPbXbKnEzCboPgMErMfpfXSi", "value":"1000","privkey":"260a5b01dd9b89b499cb4084fc9255fe8a0702985493305b0331642ea310856c"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "26a487ace638cece9e96e53a55642bb2fb51b02eb7882ca338beb5fe1d1b661f"
    }
}
```
#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/trx.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#l#trx-multi-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/trx.en.html#submit-signature)


#### XRP

request:

```
curl "http://127.0.0.1:9999/xrp" -H "Content-Type:application/json" -X POST -d '{"HMAC": "2E4YTcYTZmjNDEzNzNmMmNkYjZjOTYxODgxZjk=","wallet_id":"09f96f006bb97a95f461ab9208ebcaeb", "to_address": "rf9NFWbTmuYUsuPL6BfZMKyj7CC6BK3toH", "value":"1000","privkey":"df612e5004cc5234c8d4b21e33d0b785968278944440e40ca8f50055ca3dfa8f"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "9762ED6832209C115C5EAB8E54AB8BD50157FA76C71070750A0C2A547D7984CA"
    }
}
```
#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/xrp.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#l#xrp-multi-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/xrp.en.html#submit-signature)

#### XLM

request:

```
curl "http://127.0.0.1:9999/xlm" -H "Content-Type:application/json" -X POST -d '{"HMAC": "2E4YTcYTZmjNDEzNzNmMmNkYjZjOTYxODgxZjk=","wallet_id":"09f96f006bb97a95f461ab9208ebcaeb", "to_address": "GCTES7C7XYTRJ33PVRT277Q2CNK7E53KXZESW3TQ4NFES2OIK36EB5RT", "value":"1000","privkey":"932ce537292b82ea1cd12db7d960df3416cbb6597958283987b37f14342ab288a6497c5fbe2714ef6fac67affe1a1355f2776abe492b6e70e34a4969c856fc40"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "4db97e4842a68343b1fb508643c5c31a419bcc1825de96b2d8b44578153aeaaf"
    }
}
```
#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/xlm.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#l#xlm-multi-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/xlm.en.html#submit-signature)

#### EOS
request:

```
curl "http://127.0.0.1:9999/eos" -H "Content-Type:application/json" -X POST -d '{"HMAC": "2E4YTcYTZmjNDEzNzNmMmNkYjZjOTYxODgxZjk=","wallet_id":"09f96f006bb97a95f461ab9208ebcaeb", "outputs":  [{"account": "letmepass444", "value": 20}],"privkey":"09233039e65cd821a72faad9ad1809c724fd96a4b5c94fccc22fef4630a047b4"}'
```

response:

```
{
    "code": 200,
    "data": {
        "txid": "c41956c8dfa0592927e79cd414a6be3fcd18255c71b989927e28a2e785ab4a79"
    }
}
```
#### The program requests the following API

* [build transaction](https://sectoken-dev.github.io/docs/eos.en.html#build-transaction)
* [sign transaction](https://sectoken-dev.github.io/docs/tools.en.html#l#eos-multi-sign)
* [submit transaction](https://sectoken-dev.github.io/docs/eos.en.html#submit-signature)
