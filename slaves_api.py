import requests
import json

class SlavesAPI:
    # Deletes your account
    def deleteAccount(self):
        request = requests.delete(
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/user",
            headers=self.headers
        )
        resultDict = json.loads(request.text)
        return resultDict

    # Get your account info 
    def getAccountInfo(self):
        request = requests.get(
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/start", 
            headers=self.headers
        )
        resultDict = json.loads(request.text)
        return resultDict

    # Get top 100 users
    def getTopUsers(self):
        request = requests.get(
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/topUsers", 
            headers=self.headers
        )
        resultDict = json.loads(request.text)
        return resultDict

    # Get your friends top
    def getTopFriends(self):
        request = requests.get(
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/topFriends", 
            headers=self.headers
        )
        resultDict = json.loads(request.text)
        return resultDict

    # Get user info by user ID
    def getUserInfoByID(self, ID):
        payload = { 'id': str(ID) }
        request = requests.get(
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/user",
             params=payload, headers=self.headers
        )
        resultDict = json.loads(request.text)
        return resultDict
    
    # Get user slaves by ID
    def getUserSlaveListByID(self, ID):
        payload = { 'id': str(ID) }
        request = requests.get(
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/slaveList", 
            params=payload, headers=self.headers
        )
        resultDict = json.loads(request.text)
        return resultDict

    # Buy slave by ID
    def buySlaveByID(self, ID):
        data = json.dumps({'slave_id': ID})
        request = requests.post(
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buySlave", 
            data=data, headers=self.headers
        )
        resultDict = json.loads(request.text)
        if 'error' in resultDict:
            return 'Error: ' + resultDict['error']['message']
        return resultDict

    # Job slave by ID
    def jobSlaveByID(self, ID, jobName):
        data = json.dumps({'slave_id': ID, 'name': jobName})
        request = requests.post(
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/jobSlave", 
            data=data, headers=self.headers
        )
        resultDict = json.loads(request.text)
        if 'error' in resultDict:
            return 'Error: ' + resultDict['error']['message']
        return resultDict
    
    # Buy fetter by ID
    def buyFetterByID(self, ID):
        data = json.dumps({'slave_id': int(ID)})
        request = requests.post(
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buyFetter", 
            data=data, headers=self.headers
        )
        resultDict = json.loads(request.text)
        if 'error' in resultDict:
            return 'Error: ' + resultDict['error']['message']
        return resultDict

    # Sale slave by ID
    def saleSlaveByID(self, ID):
        data = json.dumps({'slave_id': int(ID)})
        request = requests.post(
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/saleSlave", 
            data=data, headers=self.headers
        )
        resultDict = json.loads(request.text) # JSONDecodeError

        if 'error' in resultDict:
            return 'Error: ' + resultDict['error']['message']
        return resultDict

    def __init__(self, bearerToken):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.415',
            'content-type': 'application/json',
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'origin': 'https://prod-app7794757-c1ffb3285f12.pages-ac.vk-apps.com',
            'authorization': 'Bearer token'
        }
        return