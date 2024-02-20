import brotli
from bs4 import BeautifulSoup
import csv
import json
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "session=eyJuYW1lIjoiSGVsbG8ifQ.ZdKgZA.eCEDcmlw2XVblCbDw0QIEtwAL_Y"
}

def build_dictionary():
    response = requests.get("https://www.shakespearehigh.com/classroom/guide/page3.shtml", headers=headers)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    #print(soup.prettify())
    definitions = {}
    for strong in soup.find_all("strong"):
        term = strong.text
        if term == "An\r\n    On-line Shakespearean Glossary":
            continue
        sibling = strong.next_sibling
        definitions[term] = sibling
    final_copy = {}
    for key, value in definitions.items():
        value = str(value)
        key = key.replace("S\r\n        MORRIS", " ").replace("\r\n        ", " ")
        value = value.lstrip(":\xa0").replace("to\r\n", " ").replace("\r\n        ", " ").replace("\xa0 ", " ")
        value = value.strip()
        final_copy[key] = value
        
    return final_copy


def build_rows(file_path, word, definition):
    with open(file_path, 'a', newline='') as file:
        file.write(word + ",")
        file.write(definition + "\n")


def build_csv(csv_name):
    dictionary = build_dictionary()
    for key in dictionary.keys():
        build_rows(csv_name, key, dictionary[key])



build_csv("Shakespeare_glossary_dict.csv")



    










