#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:10:00 2024

@author: marwakasim
"""

import pandas as pd
from bertopic import BERTopic


#load the dataset
df = pd.read_csv("pædagog_cleaned.csv")

#extract the text data from the df
documents = df["Cleaned_Description"].tolist()

#BERTopic with different parameters
model = BERTopic(embedding_model="distilbert-base-nli-mean-tokens", min_topic_size=4, top_n_words=45)


#fit BERTopic model on the documents
topics, probabilities = model.fit_transform(documents)

#get topic information
topic_freq = model.get_topic_freq()

#create lists to store topic and keyword data
topic_list = []
keyword_list = []

#get keywords for each topic and add them to the lists
for topic_id in topic_freq["Topic"]:
    keywords = model.get_topic(topic_id)
    keywords_str = ", ".join([kw[0] for kw in keywords])  #extracting only the first element from each tuple
    topic_list.append(topic_id)
    keyword_list.append(keywords_str)
    

#create a df from the lists
keywords_df = pd.DataFrame({"Topic": topic_list, "Keywords": keyword_list})

#save df to CSV file
keywords_df.to_csv("BERT_keywords2.csv", index=False)
