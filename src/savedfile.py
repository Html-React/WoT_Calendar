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

    def _find_login_form(self):
        if self.update:
            return self.driver.find_element(By.CLASS_NAME, "cm-user-menu-link_cutted-text")
        else:
            return self.driver.find_element(By.ID, "id_login")

    def _fill_login_form(self):
        login_form = self._find_login_form()
        if not login_form:
            logging.info("Логин не найден")
            return False

        if not self.update:
            pass_form = self.driver.find_element(By.ID, "id_password")
            login_form.send_keys(TgKeys.LOGIN)
            pass_form.send_keys(TgKeys.PASSWORD)
            elements = self.driver.find_element(By.CLASS_NAME,
                                                'button-airy.button-airy__enter.js-auth-throbbing-element')
            cookie_banner = self.driver.find_element(By.ID, "cookie-banner")
            if cookie_banner:
                self.driver.execute_script("document.getElementById('cookie-banner').style.display='none';")
            elements.click()
            time.sleep(30)
        return True

    def _save_cookies_to_file(self, cookies):
        directory = os.getcwd()
        if not os.access(directory, os.W_OK):
            logging.info(f"Ошибка: Нет прав на запись в каталоге {directory}")
            return False

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

    def savedfile(self):
        if self.update:
            logging.info("Файл 'cookies.pkl' обновление")
        else:
            logging.info("Файл 'cookies.pkl' не найден.")

        if not self._fill_login_form():
            return False

        cookies = self.driver.get_cookies()
        return self._save_cookies_to_file(cookies)
