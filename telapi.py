import json                                 # importing the JSON library
import requests


######################### CLASS #########################
class telapi():

    URL   = 'https://api.telegram.org/bot{}/'     # Telegram bot API url + TOKEN

    def __init__(self, TOKEN):
        # print('Initializing the class!')
        self.URL.format(TOKEN)
        gtm = self.getme()
        if gtm:
            print('connection successfull to the API')
        else:
            raise Exception('Failed to test API connectivity!')

    def getme(self):
        try:
            resp  = requests.get(self.URL + 'getme')            # reading the url
            resp  = resp.json()                                 # converting the content to JSON                         # 
            return resp
        except Exception as Err:
            print(Err)
            return None

    def getupdates(self, uid:int=None):
        if uid:
            resp = requests.get(self.URL + 'getUpdates', {'offset': uid + 1})      # Giving the offset Telegram forgets all those messages before this update id
        else:
            resp = requests.get(self.URL + 'getUpdates')          # reading the url to get the current updates
        upds     = resp.json()
        newuid   = None                                             # converting the content to JSON
        if upds['result']:
            newuid = upds['result'][0]['update_id']               # Read the update id          
        return upds, newuid
    
    def sendmessage(self, chid, txt, repkey:dict=None):
        if repkey:
            replykey = json.dumps(repkey)
            data =  {'chat_id': chid, 'text': txt, 'reply_markup': replykey}
        else:
            data = {'chat_id': chid, 'text': txt}
        resp = requests.post(self.URL + 'sendMessage', data = data)
        resp = resp.json()
        return resp

    def delmsg(self, chid, msgid):
        data = {'chat_id': chid, 'message_id': msgid}
        resp = requests.post(self.URL + 'deleteMessage', data = data)
        resp = resp.json()
        return resp
    
    def sendoc(self, chid, pathtodoc, caption:str=None, repkey:dict=None):
        if repkey:
            replykey = json.dumps(repkey)
            data  = {'chat_id': chid, 'reply_markup': replykey}
        else:
            data  = {'chat_id': chid}
        data['caption'] = caption
        files = {'document': (pathtodoc, open(pathtodoc, 'rb'))}
        resp = requests.post(self.URL + 'sendDocument', files = files, data = data)
        resp = resp.json()
        return resp

if __name__=='__main__':
    TOKEN = '1259359519:AAGK-O0KTOXIUJ9MRc5_YZggPUldso0kfAg'
    inst  = telapi(TOKEN)
    inst.getme()