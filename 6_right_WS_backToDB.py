from pandas.core.indexes.api import all_indexes_same
from pymongo import MongoClient
import numpy as np
import pickle
import pandas as pd
from pandas import DataFrame
All_list = []
with open('All_changed.pkl', 'rb') as fp:
    All_list = pickle.load(fp)
fp.close()

# 定義變數
chi_paper_name_WS_list = []
chi_keyword_WS_list = []
abstract_WS_list = []
content_WS_list = []
reference_WS_list = []


for i in All_list:
    chi_paper_name_WS_list.append(i[0])
    chi_keyword_WS_list.append(i[1])
    abstract_WS_list.append(i[2])
    content_WS_list.append(i[3])
    reference_WS_list.append(i[4])

print(len(chi_paper_name_WS_list))
print(len(chi_keyword_WS_list))
print(len(abstract_WS_list))
print(len(content_WS_list))
print(len(reference_WS_list))

with open('chi_paper_name_WS_list.pkl', 'wb') as fp:
    pickle.dump(chi_paper_name_WS_list,fp)
fp.close()

with open('chi_keyword_WS_list.pkl', 'wb') as fp:
    pickle.dump(chi_keyword_WS_list,fp)
fp.close()

with open('abstract_WS_list.pkl', 'wb') as fp:
    pickle.dump(abstract_WS_list,fp)
fp.close()

with open('content_WS_list.pkl', 'wb') as fp:
    pickle.dump(content_WS_list,fp)
fp.close()

with open('reference_WS_list.pkl', 'wb') as fp:
    pickle.dump(reference_WS_list,fp)
fp.close()
all_list = []
all_list.append(chi_paper_name_WS_list)
all_list.append(chi_keyword_WS_list)
all_list.append(abstract_WS_list)
all_list.append(content_WS_list)
all_list.append(reference_WS_list)
print(len(all_list))

df = DataFrame(all_list).transpose()
df.columns =["chi_paper_name_WS","chi_keyword_WS","abstract_WS","content_WS","reference_WS"]
print(df.info())
print(df.head(5))
df.to_csv("all_data_WS.csv")
with open('All_WS_list.pkl', 'wb') as fp:
    pickle.dump(all_list,fp)
fp.close()

'''
def add_field_to_mongodb(collection_name, chi_paper_name_WS_list, chi_keyword_WS_list, abstract_WS_list, content_WS_list,reference_WS_list):
    client = MongoClient('localhost', 27017)
    db = client['110_conference']
    collection = db[collection_name]

    AllFields_array = np.array(All_list)
    # print(AllFields_list[0][2], AllFields_list[1][2])
    # print('===', AllFields_array[:, 2])

    for i, _id in enumerate(AllFields_array[:, 2]):
        # print(_id, zipped_Q_segment_POS[i])

        collection.update_many({"_id": _id}, 
            {"$set": {
                "Q_WS": Q_WS_list[i], 
                "A_WS": A_WS_list[i], 
                "QA_WS": QA_WS_list[i]
                }
            })

'''

# Word Segment (WS) write to mongdb
# add_field_to_mongodb('New_data_3', chi_paper_name_WS_list, chi_keyword_WS_list, abstract_WS_list, content_WS_list,reference_WS_list)