#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 01:18:44 2024

@author: marwakasim
"""

import pandas as pd
from bertopic import BERTopic

#load the dataset
df = pd.read_csv("modulbeskrivelser_new.csv", delimiter=';')

#process the modulbeskrivelser column
documents = [str(doc) for doc in df["Modulbeskrivelser"].tolist() if pd.notna(doc)]

model = BERTopic(embedding_model="distilbert-base-nli-mean-tokens", min_topic_size=2, top_n_words=70)

topics, probabilities = model.fit_transform(documents)

#get topic information and keywords
topic_freq = model.get_topic_freq()
topic_list = []
keyword_list = []
for topic_id in topic_freq["Topic"]:
    keywords = model.get_topic(topic_id)
    keywords_str = ", ".join([str(kw[0]) for kw in keywords if kw])
    topic_list.append(topic_id)
    keyword_list.append(keywords_str)

#create a df from the lists and save to CSV
keywords_df = pd.DataFrame({"Topic": topic_list, "Keywords": keyword_list})
keywords_df.to_csv("Modulbeskrivelser_keywords.csv", index=False)

