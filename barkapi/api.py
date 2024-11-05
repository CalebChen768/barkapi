import requests
from dotenv import load_dotenv
import os
from urllib.parse import quote

class BarkAPI:
    def __init__(self):
        load_dotenv()
        self.requestURL = os.getenv("BARK_API_URL")
        self.deviceID = os.getenv("BARK_DEVICE_ID")
        self.baseURL = f"{self.requestURL}/{self.deviceID}"

    def sendMsg(self, body, title=None, icon=None, sound=None, group=None, level=None):
        if title == None:
            body = quote(body)
            requestURL = f"{self.baseURL}/{body}"
        else:
            title = quote(title)
            body = quote(body)
            requestURL = f"{self.baseURL}/{title}/{body}"
        
        params = {}

        if icon != None:
            params["icon"] = icon
        if sound != None:
            params["sound"] = sound
        if group != None:
            params["group"] = group
        if level in ["timeSensitive", "passive", "active"]:
            params["level"] = level

        response = requests.get(requestURL, params=params)

if __name__ == "__main__":
    bark = BarkAPI()
    bark.sendMsg(title=None,
                 body="Hello, World!",
                 icon=None,
                 sound=None,
                 group=None,
                 level=None)
