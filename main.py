from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def calendar() -> None:
    options = webdriver.ChromeOptions()
    # Добавление заголовков в опции драйвера
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")  # прячет запуск драйвера
    # options.add_argument("--headless") # прячет запуск браузера

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  # сам находит нужный

    cookies = [
        {'name': 'newbie_session', 'value': '1686598990912', 'domain': 'tanki.su'},
        {'name': 'csrftoken', 'value': 'Lmz2NmtoXKwOLzaXhBacmNytSJw9F28e', 'domain': 'tanki.su'},
        {'name': 'SL_G_WPT_TO', 'value': 'ru', 'domain': 'tanki.su'},
        {'name': 'tmr_lvid', 'value': '986b3b26b9ea88402ebcbfd080e9e409', 'domain': 'tanki.su'},
        {'name': 'tmr_lvidTS', 'value': '1686598993656', 'domain': 'tanki.su'},
        {'name': '_ga', 'value': 'GA1.1.1857542452.1686598994', 'domain': 'tanki.su'},
        {'name': '_ym_uid', 'value': '1678300691320577711', 'domain': 'tanki.su'},
        {'name': '_ym_d', 'value': '1686598994', 'domain': 'tanki.su'},
        {'name': 'cm.internal.bs_id', 'value': '0ebab9e2-d103-4457-46a0-feda8843d4c5', 'domain': 'tanki.su'},
        {'name': 'SL_GWPT_Show_Hide_tmp', 'value': '1', 'domain': 'tanki.su'},
        {'name': 'SL_wptGlobTipTmp', 'value': '1', 'domain': 'tanki.su'},
        {'name': 'uvt', 'value': '1', 'domain': 'tanki.su'},
        {'name': 'hsi', 'value': '1', 'domain': 'tanki.su'},
        {'name': 'cm.internal.spa_id', 'value': '19052718', 'domain': 'tanki.su'},
        {'name': 'cm.internal.realm', 'value': 'ru', 'domain': 'tanki.su'},
        {'name': 'mpvid', 'value': '1', 'domain': 'tanki.su'},
        {'name': '_ym_isad', 'value': '2', 'domain': 'tanki.su'},
        {'name': 'sessionid', 'value': 'gr2mrx9gttbcxt6i49wlctds4dagpsjs', 'domain': 'tanki.su'},
        {'name': '_ym_visorc', 'value': 'b', 'domain': 'tanki.su'},
        {'name': 'hlauth', 'value': '1', 'domain': 'tanki.su'},
        {'name': 'ref_domain', 'value': 'lesta.ru', 'domain': 'tanki.su'},
        {'name': 'newbie_lifetime', 'value': '1686598990912-1689170991058', 'domain': 'tanki.su'},
        {'name': 'authentication_confirmation_expires_at', 'value': '1689170666', 'domain': 'tanki.su'},
        {'name': 'WGAI',
         'value': 'eyJsb2dpbm5hbWUiOiAiIiwgInRpbWVzdGFtcCI6IDE2ODkxNzEwODQsICJjbGFuX25hbWUiOiBudWxsLCAiaXNfc3RhZmYiOiBmYWxzZSwgImNsYW5fYmFuIjogbnVsbCwgImdhbWVfYmFuIjogbnVsbCwgImNsYW5fdGFnIjogbnVsbCwgImNsYW5fY29sb3IiOiBudWxsLCAiaGFzX2ZyaWVuZHMiOiB0cnVlLCAic3BhX3N0YXRlIjogbnVsbCwgIm5pY2tuYW1lIjogIl9fX19fWmFLX19fX18iLCAic3BhX2lkIjogMTkwNTI3MTgsICJoYXNfY2xhbm1hdGVzIjogZmFsc2UsICJiYXR0bGVzX2NvdW50IjogMjkwMzYsICJjbGFuX2lkIjogbnVsbCwgImlzX3ByZW1pdW1fYWN0aXZlIjogZmFsc2V9',
         'domain': 'tanki.su'},
        {'name': 'hllang', 'value': 'ru', 'domain': 'tanki.su'},
        {'name': 'cm.options.user_id', 'value': '19052718', 'domain': 'tanki.su'},
        {'name': 'cm.options.user_name', 'value': '_____ZaK_____', 'domain': 'tanki.su'},
        {'name': '_ga_8BNTLSLSSR', 'value': 'GS1.1.1689170972.10.1.1689170992.0.0.0', 'domain': 'tanki.su'},
        {'name': '_ga_M4X9L4D1DD', 'value': 'GS1.1.1689170972.10.1.1689170992.0.0.0', 'domain': 'tanki.su'},
        {'name': 'reg_ref_domain', 'value': 'lesta.ru', 'domain': 'tanki.su'},
        {'name': 'tmr_detect', 'value': '0%7C1689170997709', 'domain': 'tanki.su'}
    ]

    try:
        driver.get("https://tanki.su/ru/daily-check-in/?utm_source=global-nav&utm_medium=link&utm_campaign=wot-portal")
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://tanki.su/ru/daily-check-in/?utm_source=global-nav&utm_medium=link&utm_campaign=wot-portal")
        time.sleep(5)

        # Создание объекта BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Нахождение элементов с классом "c_item c_complete"
        elements = soup.find_all('div', class_="c_item c_desable")
        # Вывод найденных элементов
        print(elements[0].text)

        # Выполнение клика на первом найденном элементе, если элемент существует и является callable
        if elements:
            first_element = elements[0]
            if first_element.has_attr('onclick'):
                first_element.click()
                print(f'Активировал')
            else:
                print(f'Не могу нажать')

        # for element in elements:
        #     print(element)

        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    while True:
        calendar()
        time.sleep(97200)