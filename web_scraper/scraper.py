import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    tags = soup.find_all("span" ,text='citation needed')
    print(f'The Number Of Citations Needed {len(tags)}')

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
    for i in unique_list:
        section = i.find_parent('p')
        print(f'{counter}) Citation needed for: {section.text}')
        counter += 1

web_page_link = 'https://en.wikipedia.org/wiki/History_of_Mexico'

get_citations_needed_count(web_page_link)
get_citations_needed_report(web_page_link)