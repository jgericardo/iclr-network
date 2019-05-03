import os
import csv
from bs4 import BeautifulSoup
from tqdm import tqdm
import re


def replace_space(str_text):
	return re.sub(' +', ' ', str_text.text.strip().replace("\n", "").replace("\t", ""))

html_filepath = "iclr2019-poster-papers.html"
with open('{}'.format(html_filepath), 'r', encoding='utf-8') as html_file:
	html_file = html_file.read()
	soup_bowl = BeautifulSoup(html_file, "html.parser")

	dataset = []
	submissions_list = soup_bowl.find_all("li", class_="note ")
	for each_sub in submissions_list:
		sub_info = []
		sub_info.append("2019")
		sub_info.append("Poster")
		#print(each_sub)
		title = each_sub.find("h4")
		sub_info.append(replace_space(title))
		
		note_authors = each_sub.find("div", class_="note-authors")
		authors = note_authors.findAll("a")
		auth_list = []
		for each_author in authors:
			auth_list.append(replace_space(each_author).replace('*',''))
		sub_info.append('; '.join(auth_list))	
		dataset.append(sub_info)
		#print()
		
	with open('iclr2019-poster-papers.csv', 'w', newline='', encoding='utf-8') as csvfile:
		csv.writer(csvfile).writerows(dataset)
	
#print('Saving:', '{}-topics-refined.csv'.format(each_file.split('.')[1]))
#with open('.{}-topics-refined.csv'.format(each_file.split('.')[1]), 'w', newline='', encoding='utf-8') as csvfile:
#	csv.writer(csvfile).writerows(keep_list)
#with open('missing-topics-refined.csv', 'w', newline='', encoding='utf-8') as csvfile:
#	csv.writer(csvfile).writerows(missing_list)