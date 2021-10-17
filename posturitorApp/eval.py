import pickle
import numpy as np
from preprocess import extractFeature 

ref_path = 'yujing_MBA_1/ref.jpg'

cand_path = 'yujing_MBA_1/A/3.jpeg'

def predict(cand_path, ref_path):
    res = []
    test_x = [extractFeature(cand_path, ref_path)]
    
    model1_path = 'models/slouch1.pkl'
    clf = pickle.load(open(model1_path, 'rb'))
    res.append(clf.predict(test_x))
    
    model1_path = 'models/slouch2.pkl'
    clf = pickle.load(open(model1_path, 'rb'))
    res.append(clf.predict(test_x))
    
    model1_path = 'models/unbalanced.pkl'
    clf = pickle.load(open(model1_path, 'rb'))
    res.append(clf.predict(test_x))
    
    return np.array(res).flatten()

def eval(cand_path, ref_path):
    res = predict(cand_path, ref_path)
    if res[0] == 1:
        print("Keep your chest up!")
    if res[1] == 1:
        print("Sit up straight!")
    if res[2] == 1:
        print("Balance your shoulders!")
    if sum(res) == 0:
        print("Your posture is correct! Keep it up!")


if __name__ == "__main__":
    eval(cand_path, ref_path)