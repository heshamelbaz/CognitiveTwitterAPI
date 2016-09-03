#!/usr/bin/python
import preprocessor
import vectorizer

def cluster_documents(documents):
    documents = preprocessor.preprocess_documents(documents)
    documents = vectorizer.get_tfidf_features(documents)
    return documents
