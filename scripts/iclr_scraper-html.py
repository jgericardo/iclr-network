import os
import csv
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
import requests


def replace_space(str_text):
	return re.sub(' +', ' ', str_text.strip().replace("\n", "").replace("\t", ""))

page = requests.get("https://iclr.cc/Conferences/2019/Schedule?type=Poster")

soup_bowl = BeautifulSoup(page.content, "html.parser")

dataset = []
submissions_list = soup_bowl.find_all("div", class_="maincard")
for each_sub in submissions_list:
	sub_info = []
	sub_info.append("2019")
	sub_info.append("Poster")
	#print(each_sub)
	title = each_sub.find("div", class_="maincardBody")
	sub_info.append(replace_space(title.text))
	
	note_authors = each_sub.find("div", class_="maincardFooter")
	authors = note_authors.text.split(" · ")
	sub_info.append(replace_space('; '.join(authors)))
	dataset.append(sub_info)
	#print()
	
with open('iclr2019-poster-papers.csv', 'w', newline='', encoding='utf-8') as csvfile:
	csv.writer(csvfile).writerows(dataset)

#print('Saving:', '{}-topics-refined.csv'.format(each_file.split('.')[1]))
#with open('.{}-topics-refined.csv'.format(each_file.split('.')[1]), 'w', newline='', encoding='utf-8') as csvfile:
#	csv.writer(csvfile).writerows(keep_list)
#with open('missing-topics-refined.csv', 'w', newline='', encoding='utf-8') as csvfile:
#	csv.writer(csvfile).writerows(missing_list)