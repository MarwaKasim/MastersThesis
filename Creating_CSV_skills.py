#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:00:29 2024

@author: marwakasim
"""

import pandas as pd

#list of job skills
job_skills = ["kørekort", "tværfagligt", "socialfaglig", "tryghed", "selvstændig", "humor", "strategi",
              "dokumentation", "fleksibel", "mødestabil", "bevægelse", "motivation", "inkluderende",
              "etiske", "støtte", "udvikler", "empati", "handicaphjælp", "rummelighed", "rolig",
              "omsorg", "reflektere", "tilknytning", "imødekommende", "opfordrer", "tillid", 
              "kommunikation", "specialpædagog", "tålmodig", "musik", "pleje","anerkendende", "udfordrende",
              "familieformer", "mentor", "humør", "inspirere", "målrettet", "kreativ", "passionerede", "indkøb",
              "positivitet", "hjælpsomhed", "nærhed", "nærværende", "relationer", "neurorehabilitering",
              "samarbejde", "terapi", 
]

#list of curriculum skills
curriculum_skills = ["videnskabelig", "samarbejde", "bevægelse", "støtte", "omsorg", 
                     "kommunikation", "bidrage", "evaluere", "vurdering", "redegøre", "etiske",
                     "familieformer", "tværfagligt", "muliggør", "relationer", "etiske",
                     "specialpædagog", "inkluderende", "inklusion", "facilitere", "digitale", "reflektere",
                     "nytænkning", "demonstrere", "gennemførelse", "perspektivere", "tilrettelæggelse",
                     "deltagelse", "leg", "dokumentation", "musik", "kreativ", "beherske", "planlægning",
                     "dømmekraft", "fremstille", "udvikler", "forskning", "didaktiske", "sociokulturel"
   
]

#create df from the lists
df_job_skills = pd.DataFrame(job_skills, columns=["Skills"])
df_curriculum_skills = pd.DataFrame(curriculum_skills, columns=["Skills"])

#save to CSV
df_job_skills.to_csv("Job_Skills.csv", index=False)
df_curriculum_skills.to_csv("Curriculum_Skills.csv", index=False)

print("CSV files have been created successfully.")
