import requests

class auto_topic():
    def __init__(self,api_url,bearer_token):
        self.api_url = api_url
        self.bearer_token = bearer_token

    def create(self,uid,cid,title,content):
        headers = {"Authorization": "Bearer %s"%self.bearer_token}
        topic = {'uid':uid,'cid':cid,'title':title,'content':content}
        response = requests.post(self.api_url,headers = headers,data=topic)
        return response

