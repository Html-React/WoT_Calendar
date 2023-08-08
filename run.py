import time
import logging
from src.logic import calendar

def main():
    try:
        while True:
            timer = calendar()
            time.sleep(timer)
    except BaseException as error:
        logging.exception(f'BaseException: {error}')
        print(error)

if __name__ == "__main__":
    main()


