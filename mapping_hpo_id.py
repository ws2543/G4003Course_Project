#!/usr/bin/env python
# coding: utf-8

# In[57]:


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
    content_endpoint = "/rest/content/"+version+"/CUI/"+cui+"/atoms?sabs=HPO"
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


# In[59]:

s1 = "congenital_heart_block"
s2 = "down_syndrome"
s3 = "neuroblastoma"


f = open("/Users/wenshen/Desktop/G4003_Project/output/10source/cui.txt")
cui_dic = OrderedDict()

for i in range(1,567):
    sp = str(i) + '_' + s1
    cui_dic[sp] = OrderedDict()

for i in range(1,558):
    sp = str(i) + '_' + s2
    cui_dic[sp] = OrderedDict()

for i in range(1,561):
    sp = str(i) + '_' + s3
    cui_dic[sp] = OrderedDict()

#cui_dic['congenital_heart_block'] = {}
#cui_dic['down_syndrome'] = {}
#cui_dic['neuroblastoma'] = {}
for line in f:
    ll = line.strip().split('\t')

    for j in cui_dic.keys():
        ss = "'" + j + "'"

        if ll[0] == ss:
            cui_dic[j][(ll[3])] = ll[2]
    
#    if ll[0] == "'down_syndrome'":
#        cui_dic['down_syndrome'][(ll[3])] = ll[2]
        
#    if ll[0] == "'neuroblastoma'":
#        cui_dic['neuroblastoma'][(ll[3])] = ll[2]


# In[60]:


#a = getByCUI('C0152021','4d3b7f93-6c59-427a-accb-5f20a99b2d41')


# In[61]:


#b = a[0]['code'].split('/')
#print b[8]


# In[70]:


hpo_dic = OrderedDict()

for i in range(1,567):
    sp = str(i) + '_' + s1
    hpo_dic[sp] = OrderedDict()

for i in range(1,558):
    sp = str(i) + '_' + s2
    hpo_dic[sp] = OrderedDict()

for i in range(1,561):
    sp = str(i) + '_' + s3
    hpo_dic[sp] = OrderedDict()

#hpo_dic['congenital_heart_block'] = {}
#hpo_dic['down_syndrome'] = {}
#hpo_dic['neuroblastoma'] = {}

#error_dic = {}
#error_dic['congenital_heart_block'] = {}
#error_dic['down_syndrome'] = {}
#error_dic['neuroblastoma'] = {}

for typ in cui_dic.keys():
    for cui in cui_dic[typ].keys():
        try:
            a = getByCUI(cui,'4d3b7f93-6c59-427a-accb-5f20a99b2d41')
            #for x in a:
            hpol = a[0]['code'].split('/')
            hpo_dic[typ][cui] = hpol[8]
        except:
            hpo_dic[typ][cui] = 'NA'


# In[78]:


#print error_dic


# In[75]:


#print len(hpo_dic['down_syndrome'])


# In[ ]:


output = open("/Users/wenshen/Desktop/G4003_Project/output/10source/HPO.txt",'w')

for typ in hpo_dic.keys():
    for cui in hpo_dic[typ].keys():
        output.write(typ)
        output.write("\t")
        output.write(cui)
        output.write("\t")
        score = cui_dic[typ][cui]
        output.write(score)
        output.write("\t")
        hpo = hpo_dic[typ][cui]
        output.write(hpo)
        output.write("\n")


# In[79]:


#hpo_dic


# In[ ]:


f.close()
output.close()

