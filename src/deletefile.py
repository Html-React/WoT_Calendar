import logging
import os

class DeleteFile:
    def __init__(self, file_name="cookies.pkl"):
        self.file_name = file_name

    def delete_file(self):
        try:
            os.remove(self.file_name)
            logging.info(f"Файл {self.file_name} удален успешно.")
        except OSError as e:
            logging.info(f"Ошибка при удалении файла:{self.file_name} {e}")