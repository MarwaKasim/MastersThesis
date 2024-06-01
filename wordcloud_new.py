#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:18:46 2024

@author: marwakasim
"""

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#load datasets
skills_df = pd.read_csv('Job_Skills.csv')
descriptions_df = pd.read_csv('pædagog_cleaned.csv')
common_skills_df = pd.read_csv('Common_Skills.csv')

#convert common skills to a list and convert to lowercase for case-insensitive comparison
common_skills = set(common_skills_df['Common Skills'].str.lower().tolist())

#text processing to create a single string of all descriptions
all_descriptions = ' '.join(descriptions_df['Cleaned_Description'].dropna()).lower()

#count the frequency of each skill in the descriptions
skill_counts = {}
for skill in skills_df['Skills'].tolist():
    skill_lower = skill.lower()
    count = all_descriptions.count(skill_lower)
    if count > 0:
        skill_counts[skill_lower] = count
        
for skill, frequency in skill_counts.items():
    print(f"Skill: {skill}, Frequency: {frequency}")

#csv
skill_counts_df = pd.DataFrame(list(skill_counts.items()), columns=['Skill', 'Frequency'])
skill_counts_df.to_csv('Skill_Frequencies.csv', index=False)

#define a color function: red for common skills, blue for others
def custom_color_func(word, **kwargs):
    if word in common_skills:
        return "red" 
    else:
        return "blue"

#custom color function
wordcloud = WordCloud(width=800, height=400, background_color='white', color_func=custom_color_func).generate_from_frequencies(skill_counts)

#display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

