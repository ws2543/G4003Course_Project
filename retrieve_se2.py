
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


def getByCUI(cui, apikey, version='2016AA'):
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




f1 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/dis_hpo_congenital_heart_block+cui.txt")
f2 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/dis_hpo_down_syndrome+cui.txt")
f3 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/dis_hpo_neuroblastoma+cui.txt")

output1 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/rs_congenital_heart_block.txt","w")
output2 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/rs_down_syndrome.txt","w")
output3 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/rs_neuroblastoma.txt","w")

for line in f1:
    ll = line.strip().split("\t")
    if len(ll) == 3:
        for i in ll[2].split(","):
            if i != "":
                #i = i.strip()
                output1.write(ll[0])
                output1.write("\t")
                output1.write(i)
                output1.write("\t")
                #print type(i)
                #print len(i)
                ##a = getByCUI(i,'4d3b7f93-6c59-427a-accb-5f20a99b2d41')

                ##for y in a["semanticTypes"]:
                ##    output1.write(y["uri"].split("/")[7])
                ##    output1.write("|")
                ##    output1.write(y["name"])
                ##    output1.write(",")
                output1.write("\n")
    else:
        output1.write(ll[0])
        output1.write("\t")
        output1.write("NA")
        output1.write("\n")



for line in f2:
    ll = line.strip().split("\t")
    if len(ll) > 2:
        for i in ll[2].split(","):
            if i != "":
                output2.write(ll[0])
                output2.write("\t")
                output2.write(i)
                output2.write("\t")
                ##a = getByCUI(i,'4d3b7f93-6c59-427a-accb-5f20a99b2d41')

                ##for y in a["semanticTypes"]:
                ##    output2.write(y["uri"].split("/")[7])
                ##    output2.write("|")
                ##    output2.write(y["name"])
                ##    output2.write(",")
                output2.write("\n")
    if len(ll) == 2:
        output2.write(ll[0])
        output2.write("\t")
        output2.write("NA")
        output2.write("\n")


for line in f3:
    ll = line.strip().split("\t")
    if len(ll) > 2:
        for i in ll[2].split(","):
            if i != "":
                output3.write(ll[0])
                output3.write("\t")
                output3.write(i)
                output3.write("\t")
                ##a = getByCUI(i,'4d3b7f93-6c59-427a-accb-5f20a99b2d41')

                ##for y in a["semanticTypes"]:
                ##    output3.write(y["uri"].split("/")[7])
                ##    output3.write("|")
                ##    output3.write(y["name"])
                ##    output3.write(",")
                output3.write("\n")
    if len(ll) == 2:
        output3.write(ll[0])
        output3.write("\t")
        output3.write("NA")
        output3.write("\n")

f1.close()
f2.close()
f3.close()

output1.close()
output2.close()
output3.close()
























