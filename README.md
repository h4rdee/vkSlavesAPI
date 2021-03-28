# vkSlavesAPI
API wrapper for VK app Slaves

### Sample usage
```python
import random
import time
from slaves_api import SlavesAPI
SAPI = SlavesAPI('Bearer token')

for _ in range (1, 10000):
    randomID = random.randint(0, 2147483647)
    SAPI.buySlaveByID(randomID)
    SAPI.jobSlaveByID(randomID, 'job name')
    SAPI.buyFetterByID(randomID)
    time.sleep(2.5)
```
