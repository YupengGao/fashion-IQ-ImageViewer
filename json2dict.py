import json
import pickle

import gzip
json_path = "/Users/yupeng.gao@ibm.com/Downloads/meta_Clothing_Shoes_and_Jewelry.json.gz"

asin2attr_list = [
					"asin2attr.dress.test.json",
					"asin2attr.dress.train.json",
					"asin2attr.dress.val.json",
					"asin2attr.shirt.test.json",
					"asin2attr.shirt.train.json",
					"asin2attr.shirt.val.json",
					"asin2attr.toptee.test.json",
					"asin2attr.toptee.val.json",
					"asin2attr.toptee.train.json"
				]


target_list = [
					"dress.test.json",
					"dress.train.json",
					"dress.val.json",
					"shirt.test.json",
					"shirt.train.json",
					"shirt.val.json",
					"toptee.test.json",
					"toptee.val.json",
					"toptee.train.json"
				]

asin2url_list = ['asin2url.dress.txt',
				'asin2url.shirt.txt',
				'asin2url.toptee.txt',

				]

# def parse(path):
#   g = gzip.open(path, 'r')
#   for l in g:
#     yield eval(l)

# f = open("output.strict", 'w')
# new_dic = {}
# for line in parse(json_path):
# 	# print(line)
#   	asin = line['asin']
#   	if "title" not in line:
# 		continue
# 	title = line['title']
# 	if "image" not in line:
# 		continue
# 	images = line["image"]
# 	new_dic[asin] = {'title': title, 'imUrl':images}



# json_file = json.load(json_path)

# new_dic = {}

# for line in json_file:
# 	asin = line['asin']
# 	title = line['title']
# 	images = line['image']
# 	new_dic[asin] = {'title': title, 'images':images}

# pickle_out = open("dict.pickle","wb")
# pickle.dump(new_dic, pickle_out)
# pickle_out.close()
diction = open("dict.pickle","rb")
diction = pickle.load(diction)
	  

for i in range(len(asin2attr_list)):
	tag_json = open(asin2attr_list[i])
	url_file = open(asin2url_list[i//3])
	url_dic = {}

	for line in url_file:
		# print(line)
		tokens = line.split()
		# print(tokens)
		url_dic[tokens[0]] = tokens[1]
	# print(url_dic)
	

	# tag_json = open('asin2attr.dress.test.json')

	tag_file = json.load(tag_json)

	new_diction = {}

	for t in tag_file:
		# print(t)
		# input()
		if t in diction and t in url_dic:
			new_diction[t] = diction[t]
			new_diction[t]['tags'] = tag_file[t]
			new_diction[t]['imUrl'] = url_dic[t]

	pickle_out = open(target_list[i]+'.pt',"wb")
	pickle.dump(new_diction, pickle_out)
	pickle_out.close()




