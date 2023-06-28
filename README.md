# LCU Remote Client Library

This library functions as a proxy for interfacing with a remote LCU. Currently, the method to register an item is implemented.
It can be called like so:
```
from LCUClient import client
c = client.LCUClient()
id = "9912-30042" # identifier string
description = "An example of invocation of the registration method"
result = c.register(id, description)
```

The response is a message indicating successful invocation of the remote method.