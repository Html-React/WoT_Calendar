import os
from typing import Final
from dotenv import load_dotenv
import logging

class TgKeys:
    load_dotenv()

    logging.basicConfig(level=20, filename="log.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s",
                        encoding='utf-8')

    if not os.path.isfile(".env"):
        logging.info("Файл '.env' не найден")
        raise FileNotFoundError("Файл '.env' не найден")


    PASSWORD = os.environ.get("PASSWORD")
    if not PASSWORD:
        logging.info("Пароль не найдено в файле '.env'")
        raise ValueError("Пароль не найдено в файле '.env'")

    PASSWORD: Final[str] = PASSWORD

    LOGIN = os.environ.get("LOGIN")
    if not LOGIN:
        logging.info("Логин не найдено в файле '.env'")
        raise ValueError("Логин не найдено в файле '.env'")

    LOGIN: Final[str] = LOGIN

    TIME = os.environ.get("TIME")
    if not TIME:
        logging.info("Таймер не найден в файле '.env'")
        raise ValueError("Таймер не найден в файле '.env'")

    TIME: Final[str] = TIME

