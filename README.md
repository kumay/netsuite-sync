# netsuite

All credit gose to the original creater **jacobsvante**. 
https://codecov.io/gh/jacobsvante/netsuite


## Reason to Falk instead of freating PR.

I needed sync method instead of async.
Needed to implement some feature for SOAP client Eg: creating SalesOrder.

Make sync and async requests to NetSuite SuiteTalk SOAP/REST Web Services and Restlets

## Quality disclaimer

The project's API is intended for personal use and not up for production use.

## Installation

place "netsuite" directory on the project root of your python project.

Call module by 
```
import netsuite
```

TODO: pip installation

## Documentation


Example: calling addSalesOrdre Soap api
this will create sales order with customer with id=237, and ordering itesm with id=218 and id=219.

```
config = Config(account = "ACCOUNT ID", # Eg tstdrv00000000
                auth = TokenAuth(consumer_key = "consumer_key",
                                 consumer_secret = "consumer_secret",
                                 token_id = "token_id",
                                 token_secret = "token_secret"))
ns = NetSuite(config)

payload = {"entity": {"internalId":237},
           "itemList": [
                           {"item": {"item": {"internalId": 218} , "quantity": 1}},
                           {"item": {"item": {"internalId":219} , "quantity": 1}}
                       ]
           }

result = ns.soap_api.addSalesOrder(record=payload)

```


TODO: prepare documentation

This module follows the original interface
https://jacobsvante.github.io/netsuite/
