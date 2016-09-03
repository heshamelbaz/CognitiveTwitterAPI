#!/usr/bin/python
import nltk
import re

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer('english')

def preprocess_documents(documents):
    return [ preprocess(document) for document in documents ]

def preprocess(document):
    sentences = nltk.sent_tokenize(document)
    words = [ 
            word 
            for sentence in sentences
            for word in nltk.word_tokenize(sentence)
            ]

    filtered_words = []
    for word in words:
        if re.search('[a-zA-Z]', word):
            filtered_words.append(word)

    stems = [ stemmer.stem(word) for word in filtered_words ]
    return ' '.join(stems)
