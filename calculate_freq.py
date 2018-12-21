
from collections import OrderedDict
import collections
f = open("/Users/wenshen/Desktop/G4003_Project/output/10source/HPO.txt")

data = OrderedDict()
data['congenital_heart_block'] = []
data['down_syndrome'] = []
data['neuroblastoma'] = []

for line in f:
	ll = line.strip().split('\t')
	if ll[0].split('_')[1] == "congenital":
		data['congenital_heart_block'].append(ll[3])

	if ll[0].split('_')[1] == "down":
		data['down_syndrome'].append(ll[3])

	if ll[0].split('_')[1] == "neuroblastoma":
		data['neuroblastoma'].append(ll[3])

sum_count1 = len(data['congenital_heart_block'])
sum_count2 = len(data['down_syndrome'])
sum_count3 = len(data['neuroblastoma'])

f.close()
#for i in set(data['congenital_heart_block']):

d1 = collections.Counter(data['congenital_heart_block'])
d2 = collections.Counter(data['down_syndrome'])
d3 = collections.Counter(data['neuroblastoma'])

d1_sorted = d1.most_common(len(set(data['congenital_heart_block'])))
d2_sorted = d2.most_common(len(set(data['down_syndrome'])))
d3_sorted = d3.most_common(len(set(data['neuroblastoma'])))


f2 = open("/Users/wenshen/Desktop/G4003_Project/output/10source/HPO.txt")
data_dic = OrderedDict()
data_dic["congenital_heart_block"] = OrderedDict()
data_dic["down_syndrome"] = OrderedDict()
data_dic["neuroblastoma"] = OrderedDict()

for line in f2:
    ll = line.strip().split("\t")
    if ll[0].split("_")[1] == "congenital":
        if ll[3] in data_dic["congenital_heart_block"].keys():
        	if ll[1] not in data_dic["congenital_heart_block"][ll[3]]:
        		data_dic["congenital_heart_block"][ll[3]].append(ll[1])
        if not ll[3] in data_dic["congenital_heart_block"].keys():
            data_dic["congenital_heart_block"][ll[3]] = [ll[1]]

    if ll[0].split("_")[1] == "down":
        if ll[3] in data_dic["down_syndrome"].keys():
        	if ll[1] not in data_dic["down_syndrome"][ll[3]]:
        		data_dic["down_syndrome"][ll[3]].append(ll[1])
        if not ll[3] in data_dic["down_syndrome"].keys():
            data_dic["down_syndrome"][ll[3]] = [ll[1]]

    if ll[0].split("_")[1] == "neuroblastoma":
        if ll[3] in data_dic["neuroblastoma"].keys():
        	if ll[1] not in data_dic["neuroblastoma"][ll[3]]:
        		data_dic["neuroblastoma"][ll[3]].append(ll[1])
        if not ll[3] in data_dic["neuroblastoma"].keys():
            data_dic["neuroblastoma"][ll[3]] = [ll[1]]


output = open("/Users/wenshen/Desktop/G4003_Project/output/10source/HPO_freq+cui.txt","w")

#for i in d1.keys():
for i in d1_sorted:
	output.write("congenital_heart_block")
	output.write("\t")
	output.write(i[0])
	output.write("\t")
	output.write(str(i[1]))
	output.write("\t")
	output.write(str(566))
	output.write("\t")
	output.write(str(sum_count1))
	output.write("\t")
	freq1 = float(i[1])/float(566)
	output.write(str(freq1))
	output.write("\t")
	freq2 = float(i[1])/float(sum_count1)
	output.write(str(freq2))
	output.write("\t")
	for j in data_dic["congenital_heart_block"][i[0]]:
		output.write(j)
		output.write(",")
	output.write("\n")

for i in d2_sorted:
	output.write("down_syndrome")
	output.write("\t")
	output.write(i[0])
	output.write("\t")
	output.write(str(i[1]))
	output.write("\t")
	output.write(str(557))
	output.write("\t")
	output.write(str(sum_count2))
	output.write("\t")
	freq1 = float(i[1])/float(557)
	output.write(str(freq1))
	output.write("\t")
	freq2 = float(i[1])/float(sum_count2)
	output.write(str(freq2))
	output.write("\t")
	for j in data_dic["down_syndrome"][i[0]]:
		output.write(j)
		output.write(",")
	output.write("\n")

for i in d3_sorted:
	output.write("neuroblastoma")
	output.write("\t")
	output.write(i[0])
	output.write("\t")
	output.write(str(i[1]))
	output.write("\t")
	output.write(str(560))
	output.write("\t")
	output.write(str(sum_count3))
	output.write("\t")
	freq1 = float(i[1])/float(560)
	output.write(str(freq1))
	output.write("\t")
	freq2 = float(i[1])/float(sum_count3)
	output.write(str(freq2))
	output.write("\t")
	for j in data_dic["neuroblastoma"][i[0]]:
		output.write(j)
		output.write(",")
	output.write("\n")

f2.close()
output.close()































