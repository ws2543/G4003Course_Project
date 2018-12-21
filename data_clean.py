
from collections import OrderedDict
f = open("/Users/wenshen/Desktop/G4003_Project/hierarchy_data.txt")

data_dic = OrderedDict()
for line in f:
    line = line.strip()
    
    if line.startswith("id: "):
        ke = line[4:]
        data_dic[ke] = OrderedDict()
        continue
    
    if line.startswith("name: "):
        ll = line.split(": ")
        name = ll[1]
        data_dic[ke]["name"] = ll[1]
    
    if line.startswith("is_a: "):
        ll = line.split(": ")
        if ("is_a" in data_dic[ke].keys()):
            data_dic[ke]["is_a"].append(ll[1])  
        if not ("is_a" in data_dic[ke].keys()):
            data_dic[ke]["is_a"] = [ll[1]]  

output4 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/HPO_freq+cui1.txt", "w")

f1 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/HPO_freq+cui.txt")
hpo_case = OrderedDict()
hpo_case["congenital_heart_block"] = []
hpo_case["down_syndrome"] = []
hpo_case["neuroblastoma"] = []
for line in f1:
    ll = line.strip().split("\t")
    if ll[0] == "congenital_heart_block":
        hpo_case["congenital_heart_block"].append(ll[1])
    if ll[0] == "down_syndrome":
        hpo_case["down_syndrome"].append(ll[1])
    if ll[0] == "neuroblastoma":
        hpo_case["neuroblastoma"].append(ll[1])

    output4.write(ll[0])
    output4.write("\t")
    output4.write(ll[1])
    output4.write("\t")
    if ll[1] in data_dic.keys():
    	output4.write(data_dic[ll[1]]["name"])
    else:
    	output4.write("NA")
    output4.write("\t")
    output4.write(ll[2])
    output4.write("\t")
    output4.write(ll[3])
    output4.write("\t")
    output4.write(ll[4])
    output4.write("\t")
    output4.write(ll[5])
    output4.write("\t")
    output4.write(ll[6])
    output4.write("\t")
    output4.write(ll[7])
    output4.write("\n")
    
output5 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/dis_hpo_congenital_heart_block.txt", "w")
f2 = open("/Users/wenshen/Desktop/G4003_Project/output/old_v/dis_hpo_congenital_heart_block.txt")
hpo_dis_congenital_heart_block = []
for line in f2:
    ll = line.strip()
    hpo_dis_congenital_heart_block.append(ll)

    output5.write(ll)
    output5.write("\t")
    if ll in data_dic.keys():
    	output5.write(data_dic[ll]["name"])
    else:
    	output5.write("NA")
    output5.write("\n")



output6 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/dis_hpo_down_syndrome.txt", "w")
f3 = open("/Users/wenshen/Desktop/G4003_Project/output/old_v/dis_hpo_down_syndrome.txt")
hpo_dis_down_syndrome = []
for line in f3:
    ll = line.strip()
    hpo_dis_down_syndrome.append(ll)

    output6.write(ll)
    output6.write("\t")
    if ll in data_dic.keys():
    	output6.write(data_dic[ll]["name"])
    else:
    	output6.write("NA")
    output6.write("\n")



output7 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/dis_hpo_neuroblastoma.txt", "w")
f4 = open("/Users/wenshen/Desktop/G4003_Project/output/old_v/dis_hpo_neuroblastoma.txt")
hpo_dis_neuroblastoma = []
for line in f4:
    ll = line.strip()
    hpo_dis_neuroblastoma.append(ll)

    output7.write(ll)
    output7.write("\t")
    if ll in data_dic.keys():
    	output7.write(data_dic[ll]["name"])
    else:
    	output7.write("NA")
    output7.write("\n")


output1 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/overlap_congenital_heart_block.txt", "w")
output2 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/overlap_down_syndrome.txt", "w")
output3 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/overlap_neuroblastoma.txt", "w")



s1 = (set(hpo_case["congenital_heart_block"])).intersection(set(hpo_dis_congenital_heart_block))
s2 = (set(hpo_case["down_syndrome"])).intersection(set(hpo_dis_down_syndrome))
s3 = (set(hpo_case["neuroblastoma"])).intersection(set(hpo_dis_neuroblastoma))


hpo_case2 = OrderedDict()
hpo_case2["congenital_heart_block"] = OrderedDict()
hpo_case2["down_syndrome"] = OrderedDict()
hpo_case2["neuroblastoma"] = OrderedDict()

f1 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/HPO_freq+cui.txt")
for line in f1:
    ll = line.strip().split("\t")

    if ll[0] == "congenital_heart_block":
        hpo_case2["congenital_heart_block"][ll[1]] = []
        for i in range(2,8):
        	hpo_case2["congenital_heart_block"][ll[1]].append(ll[i])

    if ll[0] == "down_syndrome":
    	hpo_case2["down_syndrome"][ll[1]] = []
        for i in range(2,8):
        	hpo_case2["down_syndrome"][ll[1]].append(ll[i])
        
    if ll[0] == "neuroblastoma":
    	hpo_case2["neuroblastoma"][ll[1]] = []
        for i in range(2,8):
        	hpo_case2["neuroblastoma"][ll[1]].append(ll[i])
    


for i in s1:
	output1.write(i)
	output1.write("\t")
	if i in data_dic.keys():
		output1.write(data_dic[i]["name"])
	else:
		output1.write("NA")

	output1.write("\t")
	for j in hpo_case2["congenital_heart_block"][i]:
		output1.write(j)
		output1.write("\t")
	output1.write("\n")

for i in s2:
	output2.write(i)
	output2.write("\t")
	if i in data_dic.keys():
		output2.write(data_dic[i]["name"])
	else:
		output2.write("NA")

	output2.write("\t")
	for j in hpo_case2["down_syndrome"][i]:
		output2.write(j)
		output2.write("\t")
	output2.write("\n")


for i in s3:
	output3.write(i)
	output3.write("\t")
	if i in data_dic.keys():
		output3.write(data_dic[i]["name"])
	else:
		output3.write("NA")

	output3.write("\t")
	for j in hpo_case2["neuroblastoma"][i]:
		output3.write(j)
		output3.write("\t")
	output3.write("\n")


f.close()
f1.close()
f2.close()
f3.close()
f4.close()
output1.close()
output2.close()
output3.close()
output4.close()
output5.close()
output6.close()
output7.close()



















