import time
import logging
from src import calendar


def main() -> None:
    try:
        while True:
            timer = calendar()
            logging.info(f'Вернулся таймер {timer}')
            time.sleep(timer)
    except BaseException as error:
        logging.exception(f'BaseException: {error}')
        print(error)


if __name__ == "__main__":
    main()
