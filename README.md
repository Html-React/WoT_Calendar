# Автокликер ежедневного табель-календаря игры [МИР ТАНКОВ](https://tanki.su/ru/daily-check-in/?utm_source=global-nav&utm_medium=link&utm_campaign=wot-portal)

### Описание

   OS Windows

   Python 3.11

   Автокликер заходит раз в 5 часов на сайт, авторизуется и кликает на активную награду текущего дня

### Установка и запуск

1. Установите зависимости
    
    * pip install -r requirements.txt

2. Отредактируйте файл '.env':

    * LOGIN=test@mail.ru
    * PASSWORD=test
    * TIME=18000 (период проверки значение в секундах можно изменить )

3. Запуск:

   python run.py
