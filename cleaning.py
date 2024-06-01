#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:57:52 2024

@author: marwakasim
"""
import pandas as pd
import re
import spacy

#load the CSV file into a df
file_path = 'paedagog_jobindex.csv'
df = pd.read_csv(file_path)

#remove empty rows from the description column
df = df.dropna(subset=['Description'])

#convert the description column to string type to avoid any errors during processing
df['Description'] = df['Description'].astype(str)

#load the danish language model from spacy
nlp = spacy.load("da_core_news_sm")

#define a function to clean the text
def clean_text(Description):
    if not isinstance(Description, str):
        return ""  #return an empty string if the text is not a string type
    #remove URLs from the text, HTML tags, punctuation, numders and convert to lowercase
    Description = re.sub(r'https?://\S+|www\.\S+', '', Description)
    Description = re.sub(r'<.*?>', '', Description)
    Description = re.sub(r'[^\w\sæøåÆØÅ]', '', Description)
    Description = re.sub(r'\d+', '', Description)
    Description = Description.lower()
    return Description

#define a function to remove stopwords and additional words from the text
def remove_stopwords(Description):
    #process the text with spacy
    doc = nlp(Description)
    #define additional words to remove 
    additional_stopwords = ['ansøgning', 'børn', 'arbejde', 'søger', 'arbejder', 'skole', 'børnene', 'både', 'erfaring', 'praksis'
                            'unge', 'del', '2024', 'jobbet', 'job', 'timer', 'samt', 'hus', 'velkommen', 'ringe', 'enkelte', 'holder',
                            'evt.', 'evt', 'stilling', "hos", "stillingen", "drengen", "elever", "mennesker", 'behov', 'liv', 'fælles', 'faglige',
                            'gode', 'godt', 'gerne', 'arbejdet', 'ansættelsesvilkår', 'løn', 'borgere','fagligt', 'pædagogisk',
                            'hurtigst', 'muligt', 'cv', 'relevante', 'bilag', 'kommune', 'gældende', 'overenskomst', 'faglig',
                            'opgaver', 'voksne', 'arbejdsplads', 'hverdag', 'forældre', 'kollegaer', 'muligheder',  'dag', 'pædagogiske',
                            'hinanden', 'lyst', 'får', 'løbende', 'tæt', 'borgerne', 'år', 'stor', 'pædagogisk', ' kl. ', "pædagog",
                            'kl', 'midt', 'høj', 'mulighed', 'april', 'kvinder', 'by', 'modtaget', 'duos', 'skabe', 'se',
                            'to', 'nye', 'huset', 'højt', 'særlige', 'skolen', 'medarbejdere', 'ønsker', 'sfo', 'pædagoger',
                            'bakkevej', 'send', 'fast', 'faglig', 'borgeren', 'faglighed', 'fokus', 'leder', 'børnenes',
                            'klub', 'pension', 'institution', 'region', 'pigen', 'børnehuset', 'klubmedarbejder', 
                            'ser', 'spørgsmål', 'marjatta', 'weekend', 'plads', 'forskellige', 'unge', 'børnehuset', 'ansættelse', 'aarhus']
        
    #load danish city names
    danish_cities = ['aarhus', 'Aarhus' 'aabenraa', 'albertslund', 'allerød', 'assens', 'ballerup', 'billund', 'bornholm', 'brøndby',
                     'dragør', 'egedal', 'esbjerg', 'fanø', 'favrskov', 'faxe', 'fredensborg', 'fredericia', 'frederiksberg',
                     'frederikshavn', 'frederikssund', 'furesø', 'faaborg-Midtfyn', 'gentofte', 'gladsaxe', 'glostrup', 'greve',
                     'gribskov', 'guldborgsund', 'haderslev', 'halsnæs', 'hedensted', 'helsingør', 'herlev', 'herning', 'hillerød',
                     'hjørring', 'holbæk', 'holstebro', 'horsens', 'hvidovre', 'høje-taastrup', 'hørsholm', 'ikast-brande',
                     'ishøj', 'jammerbugt', 'kalundborg', 'kerteminde', 'kolding', 'københavn', 'køge', 'langeland', 'lejre',
                     'lemvig', 'lolland', 'lyngby-taarbæk', 'læsø', 'mariagerfjord', 'middelfart', 'morsø', 'norddjurs', 'nordfyns',
                     'nyborg', 'næstved', 'odder', 'odense', 'odsherred', 'randers', 'rebild', 'ringkøbing-skjern', 'ringsted',
                     'roskilde', 'rudersdal', 'rødovre', 'samsø', 'silkeborg', 'skanderborg', 'skive', 'slagelse', 'solrød',
                     'sorø', 'stevns', 'struer', 'svendborg', 'syddjurs', 'sønderborg', 'thisted', 'tønder', 'tårnby', 'vallensbæk',
                     'varde', 'vejen', 'vejle', 'vesthimmerlands', 'viborg', 'vordingborg']

    #rebuild the string without stopwords, additional words, and city names
    return ' '.join([token.text for token in doc if not token.is_stop and token.text.lower() not in additional_stopwords and token.text not in danish_cities])

#define a function to remove the last two sentences from the text
def remove_last_two_sentences(Description):
    #split the text into sentences
    sentences = re.split(r'[.!?]', Description)
    #remove the last two sentences
    cleaned_sentences = sentences[:-4]
    #join the remaining sentences back together
    cleaned_text = ' '.join(cleaned_sentences)
    return cleaned_text.strip()

#apply the remove_stopwords function to the description column
df['Cleaned_Description'] = df['Description'].apply(remove_stopwords)

#apply the remove_last_two_sentences function to the column
df['Cleaned_Description'] = df['Cleaned_Description'].apply(remove_last_two_sentences)

#apply the clean_text function to the column
df['Cleaned_Description'] = df['Cleaned_Description'].apply(clean_text)

#drop any rows where Cleaned_Description is empty
df_cleaned = df.dropna(subset=['Cleaned_Description'])

#save the cleaned df to a new csv file
df_cleaned.to_csv('pædagog_cleaned.csv', index=False)

