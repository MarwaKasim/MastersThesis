#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:11:44 2024

@author: marwakasim
"""

import csv
import time
import requests
from bs4 import BeautifulSoup

#get links from each page
def get_links(page_link):
    response = session.get(page_link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
    else:
        print("Error: "+ response.status_code)

    return [link.get('href') for link in soup.select('a.seejobdesktop')]

#get data for each listing
def get_data(link):
    job_response = session.get(link)
    if job_response.status_code == 200:
        job_soup = BeautifulSoup(job_response.content, 'lxml')
    else:
        print("Error: ", job_response.status_code)
        return None

    data = {
        'Company/Kommune': '',
        'Title': '',
        'Description': '',
        'Publish Date': '',
        'Link': link
    }

    try:
        data['Company/Kommune'] = job_soup.select_one('a.vp-card__name').get_text(strip=True)
    except:
        print("Company/Kommune not found: ", link)
    try:
        data['Title'] = job_soup.select_one('h1').text
    except:
        print("Title not found: ", link)
    try:
        data['Description'] = job_soup.select_one('section.jobtext-jobad__body').get_text(strip=True)
    except:
        print("Description not found: ", link)
        
    try: 
        data['Publish Date'] = job_soup.select_one('time', datetime ='jix-toolbar__pubdate').text
    except:
        print("Publish date not found: ", link)

    return data

#main program
if __name__ == "__main__":
    session = requests.Session()

    base_link = 'https://www.jobindex.dk/jobsoegning/undervisning/paedagog?q=pædagog'

    #requesting base link to get 1st page links and total page count
    response = session.get(base_link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
    else:
        print("Error: ", response.status_code)
        exit()

    #1st page links
    links = [link.get('href') for link in soup.select('a.seejobdesktop')]

    total_pages = (int(soup.select_one('h1.jobsearch-header').get_text(strip=True).split()[0]) // 20) + 1
    print("Total Pages:", total_pages)

    #getting links from each page
    for page in range(2, total_pages + 1):
        page_link = base_link + f'&page={page}'
        links.extend(get_links(page_link))
        time.sleep(2)
        
    print("Total Link:", len(links))

    header = ['Company/Kommune', 'Title', 'Description', 'Publish Date', 'Link']
    with open("paedagog_jobindex.csv", mode='a', encoding='utf-8', newline='') as file:  #open file in append mode
        writer = csv.DictWriter(file, fieldnames=header)
        
        #scraping data from each link 
        for i, link in enumerate(links, start=1):
            if 'www.jobindex.dk' in link:
                print(str(i) + '-' + link)
                data = get_data(link)
                if data:
                    writer.writerow(data)
            time.sleep(2)

    session.close()
