import pandas as pd
import numpy as np


from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import re


def preprocess(text):
    corpus = []
    message=re.sub('[^a-zA-Z0-9]',' ',text) 
    # converting the message to lowercase
    message=message.lower()
    # message = np.asarray(message)
    corpus.append(message)
    with open('pickle2.pkl', 'rb') as pickle_file:
        content = pickle.load(pickle_file)
        words = content.transform(corpus)

    return(words)
    