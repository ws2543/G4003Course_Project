
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


f = open("/Users/wenshen/Desktop/G4003_Project/output/10source/HPO_freq+cui.txt")

data = OrderedDict()
data["congenital_heart_block"] = OrderedDict()
data["down_syndrome"] = OrderedDict()
data["neuroblastoma"] = OrderedDict()

for line in f:
    ll = line.strip().split("\t")
    if ll[0] == "congenital_heart_block":
        data["congenital_heart_block"][ll[1]] = []
        for i in ll[8].split(","):
            if i != "":
                data["congenital_heart_block"][ll[1]].append(i)

    if ll[0] == "down_syndrome":
        data["down_syndrome"][ll[1]] = []
        for i in ll[8].split(","):
            if i != "":
                data["down_syndrome"][ll[1]].append(i)

    if ll[0] == "neuroblastoma":
        data["neuroblastoma"][ll[1]] = []
        for i in ll[8].split(","):
            if i != "":
                data["neuroblastoma"][ll[1]].append(i)

f1 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/overlap_congenital_heart_block.txt")

overlap1 = []
for line in f1:
    ll = line.strip().split("\t")
    overlap1.append(ll[0])

f2 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/overlap_down_syndrome.txt")

overlap2 = []
for line in f2:
    ll = line.strip().split("\t")
    overlap2.append(ll[0])

f3 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/overlap_neuroblastoma.txt")

overlap3 = []
for line in f3:
    ll = line.strip().split("\t")
    overlap3.append(ll[0])



output1 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/ls_congenital_heart_block.txt","w")
output2 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/ms_congenital_heart_block.txt","w")

output3 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/ls_down_syndrome.txt","w")
output4 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/ms_down_syndrome.txt","w")

output5 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/ls_neuroblastoma.txt","w")
output6 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/ms_neuroblastoma.txt","w")


for i in data["congenital_heart_block"].keys():
    if i not in overlap1:
        for j in data["congenital_heart_block"][i]:
            output1.write(i)
            output1.write("\t")
            output1.write(j)
            output1.write("\t")
            a = getByCUI(j,'4d3b7f93-6c59-427a-accb-5f20a99b2d41')
            for ll in a["semanticTypes"]:
                output1.write(ll["uri"].split("/")[7])
                output1.write("|")
                output1.write(ll["name"])
                output1.write(",")
            output1.write("\n")
    
    if i in overlap1:
        for j in data["congenital_heart_block"][i]:
            output2.write(i)
            output2.write("\t")
            output2.write(j)
            output2.write("\t")
            a = getByCUI(j,'4d3b7f93-6c59-427a-accb-5f20a99b2d41')
            for ll in a["semanticTypes"]:
                output2.write(ll["uri"].split("/")[7])
                output2.write("|")
                output2.write(ll["name"])
                output2.write(",")
            output2.write("\n")


for i in data["down_syndrome"].keys():
    if i not in overlap2:
        for j in data["down_syndrome"][i]:
            output3.write(i)
            output3.write("\t")
            output3.write(j)
            output3.write("\t")
            a = getByCUI(j,'4d3b7f93-6c59-427a-accb-5f20a99b2d41')
            for ll in a["semanticTypes"]:
                output3.write(ll["uri"].split("/")[7])
                output3.write("|")
                output3.write(ll["name"])
                output3.write(",")
            output3.write("\n")
    
    if i in overlap2:
        for j in data["down_syndrome"][i]:
            output4.write(i)
            output4.write("\t")
            output4.write(j)
            output4.write("\t")
            a = getByCUI(j,'4d3b7f93-6c59-427a-accb-5f20a99b2d41')
            for ll in a["semanticTypes"]:
                output4.write(ll["uri"].split("/")[7])
                output4.write("|")
                output4.write(ll["name"])
                output4.write(",")
            output4.write("\n")


for i in data["neuroblastoma"].keys():
    if i not in overlap3:
        for j in data["neuroblastoma"][i]:
            output5.write(i)
            output5.write("\t")
            output5.write(j)
            output5.write("\t")
            a = getByCUI(j,'4d3b7f93-6c59-427a-accb-5f20a99b2d41')
            for ll in a["semanticTypes"]:
                output5.write(ll["uri"].split("/")[7])
                output5.write("|")
                output5.write(ll["name"])
                output5.write(",")
            output5.write("\n")
    
    if i in overlap3:
        for j in data["neuroblastoma"][i]:
            output6.write(i)
            output6.write("\t")
            output6.write(j)
            output6.write("\t")
            a = getByCUI(j,'4d3b7f93-6c59-427a-accb-5f20a99b2d41')
            for ll in a["semanticTypes"]:
                output6.write(ll["uri"].split("/")[7])
                output6.write("|")
                output6.write(ll["name"])
                output6.write(",")
            output6.write("\n")


f.close()
f1.close()
f2.close()
f3.close()
output1.close()
output2.close()
output3.close()
output4.close()
output5.close()
output6.close()































