import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    tags = soup.find_all("span" ,text='citation needed')
    return f'The Number Of Citations Needed {len(tags)}'

def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    tags = soup.find_all("span" ,text='citation needed')

    # getting unique p elements from the tags
    unique_list = []
    for item in tags: 
        if item not in unique_list: 
            unique_list.append(item) 

    counter = 1
    result = []
    for i in unique_list:
        section = i.find_parent('p')
        result.append(f'{counter}) Citation needed for: {section.text}')
        counter += 1
    return result
