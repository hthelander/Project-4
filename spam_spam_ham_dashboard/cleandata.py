import pandas as pd
import numpy as np


from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import re
import random


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


spam_response = ["../static/img/portfolio/responses/marx1.png",
            "../static/img/portfolio/responses/marx2.png",
            "../static/img/portfolio/responses/marx3.png",
            "../static/img/portfolio/responses/marx4.png",
            "../static/img/portfolio/responses/marx5.png",
            "../static/img/portfolio/responses/marx6.png",
            "../static/img/portfolio/responses/marx7.png",
            "../static/img/portfolio/responses/marx8.png",
            "../static/img/portfolio/responses/marx9.png"
            ]

ham_response = ["../static/img/portfolio/responses/quote1.png",
                "../static/img/portfolio/responses/quote2.png",
                "../static/img/portfolio/responses/quote3.png",
                "../static/img/portfolio/responses/quote4.png",]
   
    