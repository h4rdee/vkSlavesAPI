# vkSlavesAPI
API wrapper for VK app Slaves <br>
You can write complicated bots on top of that or use it to code some kind of stats tracker or whatever you want to do

### Sample usage:
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

### Methods description:
`deleteAccount`: 
permanently deletes your account from the game (**WARNING**: this can't be undone!)

`getAccountInfo`: 
returns a dictionary with your account info

`getTopUsers`:
returns a dictionary with top 100 users

`getTopFriends`:
returns a dictionary with your friends top

`getUserInfoByID`:
returns a dictionary with user info by given user ID

`getUserSlaveListByID`:
returns a dictionary with all user slaves by given user ID

`buySlaveByID`:
buys slave by ID, returns a dictionary with user info for this ID or an error string with error message

`sellSlaveByID`:
sells slave by ID, returns a dictionary with user info for this ID or an error string with error message 

`jobSlaveByID`:
setting given slave a job by slave ID, returns a dictionary with user info for this ID or an error string with error message

`buyFetterByID`:
fetters given slave by slave ID, returns a dictionary with user info for this ID or an error string with error message


### Known issues:
`floodErr`: you have been banned for approx. 2 hours. Try to randomize and increase your delays. Don't call different API methods all at once <br>
`500` or `422`: try to update auth token
