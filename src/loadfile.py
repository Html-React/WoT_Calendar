import logging
import pickle
import time


class CookiesFile:
    def __init__(self, filename):
        self.filename = filename
        self.cookies = []

    def load_cookies(self):
        logging.info(f"Попытка загрузки cookies из файла '{self.filename}'.")
        try:
            with open(self.filename, "rb") as file:
                self.cookies = pickle.load(file)
            logging.info(f"Cookies успешно загружены из файла '{self.filename}'.")
            return True
        except (IOError, FileNotFoundError) as e:
            logging.info(f"Ошибка: Невозможно открыть файл '{self.filename}': {e}")
            return False
        except pickle.UnpicklingError as e:
            logging.info(f"Ошибка: Произошла ошибка при десериализации данных из файла '{self.filename}': {e}")
            return False
        except Exception as e:
            logging.error(f'Ошибка при загрузке cookies из файла {self.filename}: {e}')
            return False


class CookieLoader:
    def __init__(self, driver, filename):
        self.driver = driver
        self.filename = filename

    def load_cookies_and_apply(self):
        cookies_file = CookiesFile(self.filename)
        if cookies_file.load_cookies():
            for cookie in cookies_file.cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            time.sleep(5)
            return True
        else:
            return False
