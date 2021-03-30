from pymongo import MongoClient

import pickle
import numpy as np



def add_field_to_mongodb(collection_name, allfields_list):
    client = MongoClient('localhost', 27017)
    db = client['New_data_3']
    collection = db[collection_name]

    AllFields_array = np.array(AllFields_list)
    # print(AllFields_list[0][2], AllFields_list[1][2])
    # print('===', AllFields_array[:, 2])

    for i, _id in enumerate(AllFields_array[:, 2]):
        # print(_id, zipped_Q_segment_POS[i])

        collection.update_many({"_id": _id}, 
            {"$set": {
                "Q_WS": Q_word_sentence_list[i], 
                "A_WS": A_word_sentence_list[i], 
                "QA_WS": QA_word_sentence_list[i]
                }
            })


AllFields_list = []
with open('AllFields_list.pkl', 'rb') as fp:
    AllFields_list = pickle.load(fp)
fp.close()

# ---
Q_word_sentence_list = []
with open('Q_word_sentence_list.pkl', 'rb') as fp:
    Q_word_sentence_list = pickle.load(fp)
fp.close()

A_word_sentence_list = []
with open('A_word_sentence_list.pkl', 'rb') as fp:
    A_word_sentence_list = pickle.load(fp)
fp.close()

QA_word_sentence_list = []
with open('QA_word_sentence_list.pkl', 'rb') as fp:
    QA_word_sentence_list = pickle.load(fp)
fp.close()


# Word Segment (WS) write to mongdb
add_field_to_mongodb('ALL_NEW', AllFields_list, Q_word_sentence_list, A_word_sentence_list, QA_word_sentence_list)