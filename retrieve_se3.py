import requests
from pyquery import PyQuery as pq
from lxml import etree
import json
from collections import OrderedDict

uri="https://utslogin.nlm.nih.gov"
#option 1 - username/pw authentication at /cas/v1/tickets
#auth_endpoint = "/cas/v1/tickets/"
#option 2 - api key authentication at /cas/v1/api-key
auth_endpoint = "/cas/v1/api-key"

class Authentication:
    #def __init__(self, username,password):
    def __init__(self, apikey):
        #self.username=username
        #self.password=password
        self.apikey=apikey
        self.service="http://umlsks.nlm.nih.gov"
    
    def gettgt(self):
        #params = {'username': self.username,'password': self.password}
        params = {'apikey': self.apikey}
        h = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent":"python" }
        r = requests.post(uri+auth_endpoint,data=params,headers=h)
        d = pq(r.text)
        ## extract the entire URL needed from the HTML form (action attribute) returned - looks similar to https://utslogin.nlm.nih.gov/cas/v1/tickets/TGT-36471-aYqNLN2rFIJPXKzxwdTNC5ZT7z3B3cTAKfSc5ndHQcUxeaDOLN-cas
        ## we make a POST call to this URL in the getst method
        tgt = d.find('form').attr('action')
        return tgt
    
    def getst(self,tgt):
        params = {'service': self.service}
        h = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent":"python" }
        r = requests.post(tgt,data=params,headers=h)
        st = r.text
        return st


# In[58]:


def getByCUI(cui, apikey, version='2018AA'):
    '''
    '''
    uri = "https://uts-ws.nlm.nih.gov"
    content_endpoint = "/rest/content/"+version+"/CUI/"+cui
    #content_endpoint = "/rest/content/current"+"/CUI/"+cui+"/atoms"

    # get authentication granting ticket for the session
    AuthClient = Authentication(apikey)
    tgt = AuthClient.gettgt()

    # generate a new service ticket
    ticket = AuthClient.getst(tgt)

    query = { 'ticket':ticket }

    r = requests.get(uri+content_endpoint,params=query)
    r.encoding = 'utf-8'
    items = json.loads(r.text)
    jsonData = items["result"]

    return jsonData


f4 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/rs_congenital_heart_block.txt")
f5 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/rs_down_syndrome.txt")
f6 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/rs_neuroblastoma.txt")

output4 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/rs_congenital_heart_block1.txt","w")
output5 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/rs_down_syndrome1.txt","w")
output6 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/rs_neuroblastoma1.txt","w")

for line in f4:
    ll = line.strip().split("\t")
    if ll[1] == "NA":
    	output4.write(ll[0])
    	output4.write("\t")
    	output4.write("NA")
    	output4.write("\t")
    	output4.write("NA")
    	output4.write("\n")
    if ll[1] != "NA":
    	output4.write(ll[0])
        output4.write("\t")
        output4.write(ll[1])
        output4.write("\t")
                
        a = getByCUI(ll[1],'4d3b7f93-6c59-427a-accb-5f20a99b2d41')

        for y in a["semanticTypes"]:
            output4.write(y["uri"].split("/")[7])
            output4.write("|")
            output4.write(y["name"])
            output4.write(",")
        output4.write("\n")


for line in f5:
    ll = line.strip().split("\t")
    if ll[1] == "NA":
    	output5.write(ll[0])
    	output5.write("\t")
    	output5.write("NA")
    	output5.write("\t")
    	output5.write("NA")
    	output5.write("\n")
    if ll[1] != "NA":
    	output5.write(ll[0])
        output5.write("\t")
        output5.write(ll[1])
        output5.write("\t")
                
        a = getByCUI(ll[1],'4d3b7f93-6c59-427a-accb-5f20a99b2d41')

        for y in a["semanticTypes"]:
            output5.write(y["uri"].split("/")[7])
            output5.write("|")
            output5.write(y["name"])
            output5.write(",")
        output5.write("\n")

for line in f6:
    ll = line.strip().split("\t")
    if ll[1] == "NA":
    	output6.write(ll[0])
    	output6.write("\t")
    	output6.write("NA")
    	output6.write("\t")
    	output6.write("NA")
    	output6.write("\n")
    if ll[1] != "NA":
    	output6.write(ll[0])
        output6.write("\t")
        output6.write(ll[1])
        output6.write("\t")
                
        a = getByCUI(ll[1],'4d3b7f93-6c59-427a-accb-5f20a99b2d41')

        for y in a["semanticTypes"]:
            output6.write(y["uri"].split("/")[7])
            output6.write("|")
            output6.write(y["name"])
            output6.write(",")
        output6.write("\n")

f4.close()
f5.close()
f6.close()

output4.close()
output5.close()
output6.close()
