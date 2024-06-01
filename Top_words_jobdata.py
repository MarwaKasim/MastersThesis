#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:18:39 2024

@author: marwakasim
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#load the dataset
df = pd.read_csv('BERT_keywords2.csv')

#check unique topics
print("Unique topics in dataset:", df['Topic'].nunique())

#apply TF-IDF to documents
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Keywords'])

#convert the resulting sparse matrix to a DataFrame to see word scores per topic
feature_names = vectorizer.get_feature_names_out()
tfidf_df = pd.DataFrame(X.toarray(), columns=feature_names, index=df['Topic'])  

#define a function to get the top N words and their scores for each topic
def get_top_words_and_scores(row, top_n=7):
    top_indices = row.argsort()[-top_n:][::-1]  
    top_words = [feature_names[index] for index in top_indices]
    top_scores = [row[index] for index in top_indices]
    return pd.Series(top_words + top_scores)

#number of top words
top_n = 7

#apply the function to each row in the tfidf_df
top_words_scores_df = tfidf_df.apply(lambda row: get_top_words_and_scores(row, top_n=top_n), axis=1)
column_labels = [f"Word_{i+1}" for i in range(top_n)] + [f"Score_{i+1}" for i in range(top_n)]
top_words_scores_df.columns = column_labels

#save the df to CSV
top_words_scores_df.to_csv('Top_Words_Scores_Per_Topic2.csv', index=True)

#print to see the output format
print(top_words_scores_df.head())
