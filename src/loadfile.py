import logging
import pickle
import time

class LoadFile:
    def __init__(self, driver):
        self.driver = driver
    def loadfile(self):
        logging.info("Файл 'cookies.pkl' существует.")

        # Загружаем cookies
        try:
            with open("cookies.pkl", "rb") as file:
                cookies = pickle.load(file)
            logging.info("Cookies успешно загружены из файла 'cookies.pkl'")
        except (IOError, FileNotFoundError) as e:
            logging.info(f"Ошибка: Невозможно открыть файл 'cookies.pkl': {e}")
            return False
        except pickle.UnpicklingError as e:
            logging.info(f"Ошибка: Произошла ошибка при десериализации данных: {e}")
            return False
        except Exception as e:
            logging.error(f'Ошибка в файле cookies.pkl: {e}')
            return False


        # Устанавливаем cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # Обновляем страницу, чтобы применить cookies
        self.driver.refresh()
        time.sleep(5)
        return True
