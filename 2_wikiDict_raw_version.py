import gzip
import shutil
import pickle

with gzip.open('zhwiki-latest-all-titles.gz', 'rb') as f_in:
	with open('zhwiki-latest-all-titles.txt', 'wb') as f_out:
		shutil.copyfileobj(f_in, f_out)

page_list = []
with open('zhwiki-latest-all-titles.txt', 'r', encoding='utf-8') as f:
	line = f.readline().replace('\n', '')
	while line != '':
		page_list.append(line.split('\t'))
		line = f.readline().replace('\n', '')

page_dict = dict()
for i in range(1, len(page_list)):
	page_title = page_list[i][1]
	if page_title not in page_dict.keys():
		page_dict[page_title] = 1
	else:
		page_dict[page_title] += 1




#物件序列化：使用Pickle
with open('corpus_wikidict_PAGETITLE.pkl', 'wb') as fp:
    pickle.dump(page_dict, fp)
fp.close()
    