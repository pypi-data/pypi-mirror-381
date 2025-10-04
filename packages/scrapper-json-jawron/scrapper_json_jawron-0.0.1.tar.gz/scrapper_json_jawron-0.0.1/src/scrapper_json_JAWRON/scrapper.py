from typing import List, Type, Generic, TypeVar
import re
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup, Tag

def get_element(root_element: Tag, rules: dict) -> list[Tag]|Tag|str:
    selector = rules.get('selector')
    attribute = rules.get('attribute', 'text')
    item_type = rules.get('item_type', 'single')

    if selector is None:
        print("ERROR: no selector.")
        return root_element

    if item_type == 'single':
        element = root_element.select_one(selector)
        if element is None:
            return ""

        if attribute == "text":
            return element.get_text(strip=True)
        elif attribute == "element":
            return element
        else:
            return element.get(attribute)
    elif item_type == 'list':
        elements = root_element.select(selector)
        return elements
    else:
        return root_element

def get_response(url: str) -> requests.Response:
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("ERROR: HTTP Error", e)
        raise Exception("HTTP Error")
    return response

T = TypeVar('T')

class Scrapper(Generic[T]):
    def __init__(self, rules: dict, result_class: Type[T]):
        self.rules = rules
        self.root_url = rules.get('url')
        self.result_class = result_class

    def scrap_list(self) -> List[T]:
        rules = self.rules
        response = get_response(self.root_url)

        entity_list = []
        if rules.get('type') == 'xml':
            tree = ET.fromstring(response.content)
            namespaces = rules.get('namespace')
            root = tree.find(rules.get('root'), namespaces) if rules.get('root') is not None else tree
            entries = root.findall(rules.get('entry'), namespaces)

            for entry in entries:
                entry_rules = rules.get("elements")
                item_dict = {}

                for key, item_rules in entry_rules.items():
                    item_element = entry.find(item_rules.get('selector'), namespaces)
                    if item_rules.get('attribute') == 'text':
                        item = item_element.text.strip() if item_element is not None else ''
                    else:
                        item = item_element.attrib[item_rules.get('attribute')] if item_element is not None else ''

                    if item_rules.get('prefix') is not None:
                        item = item_rules.get('prefix') + item
                    if item_rules.get('suffix') is not None:
                        item = item + item_rules.get('suffix')
                    item_dict[key] = item

                page_obj = self.result_class(**item_dict)
                entity_list.append(page_obj)
        elif rules.get('type') == 'html':
            soup = BeautifulSoup(response.content, "html.parser")
            root = get_element(soup, rules.get('root'))
            for entry in get_element(root, rules.get('entry')):
                item_dict = self.iterate_elements(entry, rules)
                page_obj = self.result_class(**item_dict)
                entity_list.append(page_obj)

        for index, article in enumerate(entity_list):
            entity_list[index] = self.clean_entity(article)
        return entity_list

    def scrap_entity(self, article_rules: dict, entity: T) -> T:
        url = entity.url
        response = get_response(url)

        soup = BeautifulSoup(response.content, "html.parser")
        content = get_element(soup, article_rules.get('content'))
        entity.content = content

        article = self.clean_entity(entity, clean_content=True)
        return article

    def iterate_elements(self, entry: Tag, rules: dict) -> dict:
        entry_rules = rules.get("elements")
        item_dict = {}

        for key, item_rules in entry_rules.items():
            item = get_element(entry, item_rules) if item_rules.get('selector') is not None else ''
            if item_rules.get('elements') is not None:
                item = self.iterate_elements(item, item_rules)
            if item_rules.get('prefix') is not None:
                item = item_rules.get('prefix') + item
            if item_rules.get('suffix') is not None:
                item = item + item_rules.get('suffix')
            if item_rules.get('remove') is not None:
                remove = item_rules.get('remove')
                for phrase in remove:
                    item = item.replace(phrase, '')
            if item_rules.get('replace') is not None:
                replace = item_rules.get('replace')
                for phrase in replace:
                    original, new = phrase.split('|')
                    if original != '' and new != '':
                        item = item.replace(original, new)

            item_dict[key] = item
        return item_dict

    def clean_entity(self, entity: T, clean_content: bool = False) -> T:
        if clean_content:
            entity.content = entity.content.strip().replace('\n', '').replace('\t', '').replace("Reklama", "")
            entity.content = re.sub(r' +', ' ', entity.content)
        else:
            entity.title = entity.title.strip().replace('\n', '').replace('\t', '')
            entity.description = entity.description.strip().replace('\n', '').replace('\t', '')
            entity.metadata = entity.metadata.strip().replace('\n', '').replace('\t', '')
        return entity