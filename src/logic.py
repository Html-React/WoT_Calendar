from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.env import TgKeys
import time
import logging
import os
import datetime
from src.loadfile import CookieLoader
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

    options.add_experimental_option('excludeSwitches', ['enable-logging']) # Отключает лишние логи

    # драйвер скачивается C:\Users\zak_x\.wdm\drivers\chromedriver\win64
    # посмотреть последнею версию драйвера https://googlechromelabs.github.io/chrome-for-testing/
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
                    load = CookieLoader(driver, "cookies.pkl")
                    result = load.load_cookies_and_apply()
                    if not result:
                        logging.info(f'Ошибка при взаимодествии с файлом cookies.pkl')
                        DeleteFile().delete_file()
                        return 2
                else:
                    logging.info(f'Файлу больше суток')

                    DeleteFile().delete_file()
                    return 2

            else:
                file = SavedFile(driver)
                result = file.savedfile()
                if not result:
                    return 2

            # Создание объекта BeautifulSoup
            soup = BeautifulSoup(driver.page_source, "html.parser")
            authentication = soup.find('span', class_="cm-user-menu-link_cutted-text")

            if authentication:
                logging.info(f'Аутентификация выполнена')

                # Нахождение элементов с классом ".c_item.c_default или .CalendarItem_base__D4guG.CalendarItem_default__pb-ED"

                selector = '.c_item.c_default, .CalendarItem_base__D4guG.CalendarItem_default__pb-ED'

                try:
                    element = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, selector)
                        )
                    )

                    element.click()
                    print(f'Активировал - {element.text}')
                    logging.info(f'Активировал - {element.text}')

                except TimeoutException:
                    elements = driver.find_elements(By.CSS_SELECTOR, selector)

                    if elements:
                        print(f'Элемент найден, но не кликабелен. Классы: {selector}')
                        logging.error(f'Элемент найден, но не кликабелен. Классы: {selector}')
                    else:
                        print(f'Элемент не найден. Классы: {selector}')
                        logging.warning(f'Элемент не найден. Классы: {selector}')

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
