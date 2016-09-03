#!/usr/bin/python
from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_features(documents):
    tfidf_vectorizer = TfidfVectorizer(analyzer='word')
    tfidf_vectorizer.fit_transform(documents)

    tfidf_features = tfidf_vectorizer.get_feature_names()
    tfidf_scores = tfidf_vectorizer.idf_

    return dict(zip(tfidf_features, tfidf_scores))
