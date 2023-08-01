import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import logging

class WebdriverVer:
    def __init__(self):
        self.url = "https://chromedriver.storage.googleapis.com/"
        self.files_data = []

    def get_xml_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            xml_data = response.content
            root = ET.fromstring(xml_data)
            self.files_data = []

            for contents_elem in root.findall(".//{http://doc.s3.amazonaws.com/2006-03-01}Contents"):
                key = contents_elem.find("{http://doc.s3.amazonaws.com/2006-03-01}Key").text
                if "chromedriver_win32" in key:
                    last_modified_str = contents_elem.find("{http://doc.s3.amazonaws.com/2006-03-01}LastModified").text
                    last_modified_date_time = datetime.fromisoformat(last_modified_str[:-1])
                    self.files_data.append((key, last_modified_date_time))
        else:
            logging.info("Не удалось получить XML данные.")

    def version(self):
        self.get_xml_data()

        if self.files_data:
            latest_file = max(self.files_data, key=lambda x: x[1])
            version = latest_file[0].split('/')[0]
            return version
        else:
            logging.info("Файлы с 'chromedriver_win32' в ключе не найдены.")