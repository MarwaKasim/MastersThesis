#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:48:54 2024

@author: marwakasim
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

#load the datasets from CSV files
df_job_skills = pd.read_csv("Job_Skills.csv")
df_curriculum_skills = pd.read_csv("Curriculum_Skills.csv")

#convert the df columns to sets
set_job_desc = set(df_job_skills['Skills'].dropna().str.lower())
set_curriculum = set(df_curriculum_skills['Skills'].dropna().str.lower())


#find common and different skills
common_skills = set_job_desc.intersection(set_curriculum)
unique_to_job_desc = set_job_desc.difference(set_curriculum)
unique_to_curriculum = set_curriculum.difference(set_job_desc)

#visualization using Venn Diagram with skills listed
plt.figure(figsize=(15, 15))
venn_diagram = venn2([set_job_desc, set_curriculum], ('Job description skills', 'curriculum skills'))

#labeling the sets with skills
venn_diagram.get_label_by_id('10').set_text('\n'.join(unique_to_job_desc))
venn_diagram.get_label_by_id('01').set_text('\n'.join(unique_to_curriculum))
venn_diagram.get_label_by_id('11').set_text('\n'.join(common_skills))

plt.title("Comparison of skills from job descriptions and curriculum")
plt.show()

#save common skills to a CSV file
common_skills_df = pd.DataFrame(list(common_skills), columns=['Common Skills'])
common_skills_df.to_csv('Common_Skills.csv', index=False)