import os

from typing_extensions import final
import get_data
from ckiptagger import WS
from ckiptagger import construct_dictionary
import pickle
import re
from pandas import DataFrame
All = []
All_changed = []
# print("@@@@@")

# Get Data Row from Mongodb (Answer, Question, Q&A)
allfields_list= get_data.get_mongodb_row("New_data_3")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "1"   #默認值為 0 (顯示所有logs)，設置為 1 隱藏 INFO logs, 2 額外隱藏WARNING logs, 設置為3所有 ERROR logs也不顯示。
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def remove_punctuation(line):
    rule = re.compile("[^a-zA-Z0-9\\u4e00-\\u9fa5]")
    line = rule.sub('',line)
    return line

# Word Segment and save to XXX_word_sentence_list.pkl
def WordSegment_and_write2file(give):
    ws = WS("./data",disable_cuda=False)

    with open('WikiDict_plus_allfieldskeywordsDict.pkl', 'rb') as fp:
        WikiDict_plus_allfieldskeywordsDict = pickle.load(fp)
    fp.close()

    for i in [give]:
            # print(i)
            word_sentence_list = ws(
                i, 
                sentence_segmentation = True,
                segment_delimiter_set = {",", "。", ":", "?", "!", ";", "？", "，", "、", " ", "。", "！", "? ", "NULL","\n","\n3000","（","）","=","/"},
                recommend_dictionary = construct_dictionary(WikiDict_plus_allfieldskeywordsDict),
            )
            # print(word_sentence_list)

            # with open('allfields_list.pkl', 'wb') as fp:
            #     pickle.dump(word_sentence_list, fp)
            # fp.close()

            # print("1")
            All.append(word_sentence_list)
            # del word_sentence_list
            


            # with open("allfields_list.pkl",'rb') as f:
            #     final = pickle.loads(f.read())
                # print("2")
                # print(final)
                
            new_final = []
            for i in word_sentence_list:
                new_i = []
                # print(i)
                for j in i:
                    j = remove_punctuation(j)
                    # print(j)
                    if j != "" :
                        new_i.append(j)
                new_final.append(new_i)
                # print(new_final)
            # print("$$$$$",new_final)
            return new_final,word_sentence_list
            

'''
            paper_name =[]
            keyword = []
            abstract = []
            content = []
            reference = []
            print(new_final[0])
            for i in range(len(new_final)):
                paper_name.append(new_final[i][0])
                keyword.append(new_final[i][1])
                abstract.append(new_final[i][2])
                content.append(new_final[i][3])
                reference.append(new_final[i][4])
            print(paper_name)
            df = DataFrame (new_final)
            df.columns = ["paper_name","keyword","abstract","content","reference"]
            print (df.info())
'''

# with open('AllFields_list.pkl', 'wb') as fp:
#     pickle.dump(allfields_list, fp)
# fp.close()


# test01 = allfields_list[1]
# print(test01)
# WordSegment_and_write2file(test01)


test02 = []
# print("!!!!!")
# print(allfields_list[0])
for i in range(0,len(allfields_list)):
    test02.append(allfields_list[i])
# print(type(test02))
# print(len(test02))
word_sentence_list_list = []
for i in range (len(test02)):
    data = test02[i]
    print(f"第{i}次")
    new_final,word_sentence_list = WordSegment_and_write2file(data)
    All_changed.append(new_final)
    word_sentence_list_list.append(word_sentence_list)
    print(f"長度1:{len(All_changed)}")
    print(f"長度2:{len(word_sentence_list_list)}")
    with open('All_changed.pkl', 'wb') as fp:
        pickle.dump(All_changed, fp)
    fp.close()
    with open('allfields_list.pkl', 'wb') as fp:
        pickle.dump(word_sentence_list_list, fp)
    fp.close()
    # print(All_changed)
'''
with open('All_changed.pkl', 'wb') as fp:
    pickle.dump(All_changed, fp)
fp.close()
with open('allfields_list.pkl', 'wb') as fp:
    pickle.dump(word_sentence_list, fp)
fp.close()
'''

# WordSegment_and_write2file(test02)

# WordSegment_and_write2file(allfields_list)


# print(All_changed[-1])
# print(All_changed)

# with open('All_changed.pkl', 'wb') as fp:
#     pickle.dump(All_changed, fp)
# fp.close()
