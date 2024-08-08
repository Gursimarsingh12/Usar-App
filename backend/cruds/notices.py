import requests
from bs4 import BeautifulSoup
import html
from schemas.notices import notice_schema, notices_list
from dependencies import get_notices_collection
from fastapi import HTTPException

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
    try:
        notices_collection = await get_notices_collection()
        soup = fetch_webpage(url)
        notices = extract_notices(soup)
        await notices_collection.insert_many(notices)
        return notices_list(notices)
    except Exception as e:
        print(f"Error fetching or storing notices: {e}")
        raise HTTPException(status_code=500, detail="Error fetching or storing notices")

async def get_latest_notices():
    try:
        notices_collection = await get_notices_collection()
        await notices_collection.create_index([("title", 1), ("link", 1)], unique=True)

        soup = fetch_webpage(url)
        new_notices = extract_notices(soup)
        latest_notices = []

        existing_titles_links = await notices_collection.find(
            {}, {"title": 1, "link": 1}
        ).to_list(length=None)
        existing_set = {(doc["title"], doc["link"]) for doc in existing_titles_links}

        for notice in new_notices:
            if (notice["title"], notice["link"]) not in existing_set:
                latest_notices.append(notice)

        if latest_notices:
            await notices_collection.insert_many(latest_notices)

        return notices_list(latest_notices)
    except Exception as e:
        print(f"Error fetching or storing latest notices: {e}")
        raise HTTPException(status_code=500, detail="Error fetching or storing latest notices")

