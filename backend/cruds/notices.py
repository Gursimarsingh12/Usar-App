import requests
from bs4 import BeautifulSoup
import html
from schemas.notices import notice_schema, notices_list
from dependencies import MongoDB

url = "https://sites.google.com/view/ggsipuedc/notice-board?authuser=0"

def fetch_webpage(url: str):
    webpage = requests.get(url=url)
    soup = BeautifulSoup(webpage.content, 'lxml')
    return soup

def extract_notices(soup):
    divs = soup.find_all('div', {'class': 'w536ob'})
    data = []

    for div in divs:
        data_code_content = div.get('data-code')
        if data_code_content:
            decoded_content = html.unescape(data_code_content)
            soup_decoded = BeautifulSoup(decoded_content, 'lxml')
            rows = soup_decoded.find_all('tr')
            for row in rows[1:]:
                columns = row.find_all('td')
                if len(columns) >= 2:
                    date = columns[0].text.strip()
                    link = columns[1].find('a')
                    if link is not None:
                        title = link.text.strip()
                        href = link.get('href')
                        data.append(notice_schema({'date': date, 'title': title, 'link': href}))
    return data

async def get_notices():
    soup = fetch_webpage(url)
    notices = extract_notices(soup)
    notices_collection = await MongoDB.get_notices_collection()
    await notices_collection.insert_many(notices)
    return notices_list(notices)

async def get_latest_notices():
    soup = fetch_webpage(url)
    new_notices = extract_notices(soup)
    latest_notices = []
    notices_collection = await MongoDB.get_notices_collection()

    for notice in new_notices:
        existing_notice = await notices_collection.find_one({"title": notice["title"], "link": notice["link"]})
        if not existing_notice:
            latest_notices.append(notice)
            await notices_collection.insert_one(notice)

    return notices_list(latest_notices)
