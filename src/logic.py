from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from src.env import TgKeys
import time
import logging
import os
import datetime
from src.loadfile import LoadFile
from src.savedfile import SavedFile
from src.deletefile import DeleteFile


def calendar() -> int:
    timing = int(TgKeys.TIME)
    options = webdriver.ChromeOptions()

    # Добавление заголовков в опции драйвера
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
        "Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")  # прячет запуск драйвера
    options.add_argument("--headless")  # прячет запуск браузера
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=options)  # сам находит нужный
    except ValueError as e:
        logging.info(f'По url такой драйвер не существует {e}')
        return timing
    try:

        if os.path.exists("cookies.pkl"):
            driver.get(
                "https://tanki.su/ru/daily-check-in/?utm_source=global-nav&utm_medium=link&utm_campaign=wot-portal")
            time.sleep(5)
        else:
            driver.get(
                "https://tanki.su/auth/oid/new/?next=/ru/daily-check-in/%3Futm_source%3Dglobal-nav%26utm_medium"
                "%3Dlink%26utm_campaign%3Dwot-portal")
            time.sleep(15)

        # Проверка наличия подключения
        if driver.title:

            logging.info(f'Страница успешно загружена')

            if os.path.exists("cookies.pkl"):
                # Получаем текущую дату
                current_date = datetime.datetime.now().date()

                # Получаем дату последнего изменения файла
                file_date = datetime.datetime.fromtimestamp(os.path.getmtime("cookies.pkl")).date()

                # Получаем разницу в днях
                data = (current_date - file_date).days

                if data < 1:
                    # Создаем экземпляр класса LoadFile
                    load = LoadFile(driver).loadfile()
                    if not load:
                        logging.info(f'Ошибка при взаимодествии с файлом cookies.pkl')
                        DeleteFile().delete_file()
                        return 60
                else:
                    logging.info(f'Файлу больше суток')
                    DeleteFile().delete_file()
                    return 60

            else:
                file = SavedFile(driver).savedfile()
                if not file:
                    return 60

            # Создание объекта BeautifulSoup
            soup = BeautifulSoup(driver.page_source, "html.parser")
            authentication = soup.find('span', class_="cm-user-menu-link_cutted-text")

            if authentication:
                logging.info(f'Аутентификация выполнена')

                # Нахождение элементов с классом "c_item c_complete"

                elements = soup.find('div', class_='c_item c_default')

                # Выполнение клика на первом найденном элементе, если элемент существует и является callable
                if elements:
                    elements = driver.find_element(By.CLASS_NAME, 'c_item.c_default')
                    elements.click()
                    print(f'Активировал - {elements.text}')
                    logging.info(f'Активировал - {elements.text}')
                else:
                    print(f'Активация задания не доступна')
                    logging.info(f'Активация задания не доступна')

                time.sleep(5)
            else:
                DeleteFile().delete_file()
                logging.info(f'Ошибка Аутентификации')

        else:
            logging.info(f'Ошибка подключения к странице')

    except Exception as ex:
        logging.error(f'Exception: {ex}')
        print(ex)

    driver.close()
    driver.quit()
    return timing
