import os
import csv
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
import sys



def replace_space(str_text):
	return re.sub(' +', ' ', str_text.text.strip().replace("\n", "").replace("\t", ""))

xml_filepath = sys.argv[1]
with open('{}'.format(xml_filepath), 'r', encoding='utf-8') as xml_file:
	xml_file = xml_file.read()
	soup_bowl = BeautifulSoup(xml_file, features="xml")

	dataset = []
	submissions_list = soup_bowl.find_all("hit")
	for each_sub in submissions_list:
		sub_info = []
		sub_info.append("2018")
		sub_info.append("Poster")
		#print(each_sub)
		title = each_sub.find("title")
		sub_info.append(replace_space(title))
		
		note_authors = each_sub.find("authors")
		if not note_authors is None:
			authors = note_authors.findAll("author")
			auth_list = []
			for each_author in authors:
				le_author = replace_space(each_author).replace('*','')
				le_author = re.sub('[0-9]', ' ', le_author)
				auth_list.append(le_author.strip())
			sub_info.append('; '.join(auth_list))	
		
		dataset.append(sub_info)
			#print()
		
	with open('{}.csv'.format(sys.argv[1]), 'w', newline='', encoding='utf-8') as csvfile:
		csv.writer(csvfile).writerows(dataset)
	
#print('Saving:', '{}-topics-refined.csv'.format(each_file.split('.')[1]))
#with open('.{}-topics-refined.csv'.format(each_file.split('.')[1]), 'w', newline='', encoding='utf-8') as csvfile:
#	csv.writer(csvfile).writerows(keep_list)
#with open('missing-topics-refined.csv', 'w', newline='', encoding='utf-8') as csvfile:
#	csv.writer(csvfile).writerows(missing_list)