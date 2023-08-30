import logging
from src.env import TgKeys
import time
from selenium.webdriver.common.by import By
import pickle
import os

class SavedFile:
    def __init__(self, driver, update=False):
        self.driver = driver
        self.update = update

    def savedfile(self):

        if self.update == True:
            logging.info("Файл 'cookies.pkl' обновление")
            login_form = self.driver.find_element(By.CLASS_NAME, "cm-user-menu-link_cutted-text")
            if login_form:
                pass
            else:
                logging.info("Логин не найден")
                return False
        else:
            logging.info("Файл 'cookies.pkl' не найден.")
            login_form = self.driver.find_element(By.ID, "id_login")
            if login_form:
                pass_form = self.driver.find_element(By.ID, "id_password")
                login_form.send_keys(TgKeys.LOGIN)
                pass_form.send_keys(TgKeys.PASSWORD)
                elements = self.driver.find_element(By.CLASS_NAME,
                                                    'button-airy.button-airy__enter.js-auth-throbbing-element')
                elements.click()
                time.sleep(30)
            else:
                return False



        # Читаем из браузера cookies
        cookies = self.driver.get_cookies()

        # Проверяем, есть ли права на запись в текущем каталоге
        directory = os.getcwd()
        if not os.access(directory, os.W_OK):
            logging.info(f"Ошибка: Нет прав на запись в каталоге {directory}")
            return False

        # Сохраняем cookies в файл
        try:
            with open("cookies.pkl", "wb") as file:
                pickle.dump(cookies, file)
            logging.info("Cookies успешно сохранены в файл 'cookies.pkl'")
            return True
        except (IOError, FileNotFoundError) as e:
            logging.info(f"Ошибка: Невозможно открыть или записать файл 'cookies.pkl': {e}")
            return False
        except pickle.PicklingError as e:
            logging.info(f"Произошла ошибка при сериализации данных: {e}")
            return False
