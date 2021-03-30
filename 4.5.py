import pickle
with open('All_changed.pkl', 'rb') as fp:
    test = pickle.load(fp)
    print(len(test))
    for i in range(0,5):
        print(test[0][i])