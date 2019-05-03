import os
import csv



csv_list = [file for file in os.listdir('.') if '.csv' in file]

final_dataset = []
for each_file in csv_list:
	print(each_file)
	with open(each_file, 'r', encoding='utf-8') as csvfile:
		conf_list = list(csv.reader(csvfile))
		
		final_dataset += conf_list
		
with open('final_iclr_dataset_2019.csv', 'w', newline='', encoding='utf-8') as csvfile:
	csv.writer(csvfile).writerows(final_dataset)