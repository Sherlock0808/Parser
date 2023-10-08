from bs4 import BeautifulSoup
import json


def get_html(file_path):
    HtmlFile = open(file_path, 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    soup = BeautifulSoup(source_code, 'html.parser')
    return soup


def save_json(list):
    dict_learning_id = list[0]
    dict_learning_content = list[1]
    with open('dict_learning_id.json', 'w', encoding='UTF-8') as file:
        json.dump(dict_learning_id, file, indent=4)
    with open('dict_learning_content.json', 'w', encoding='UTF-8') as file1:
        json.dump(dict_learning_content, file1, indent=4)
    return 'Done✅'
