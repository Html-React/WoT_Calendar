# Автокликер ежедневного табель-календаря игры [МИР ТАНКОВ](https://tanki.su/ru/daily-check-in/?utm_source=global-nav&utm_medium=link&utm_campaign=wot-portal)

### Описание

   OS Windows

   Python 3.12

   Автокликер заходит раз в 5 часов на сайт, авторизуется и кликает на активную награду текущего дня

### Установка и запуск

1. Установка
    
    * скачать [Автокликер ](https://github.com/Html-React/WoT_Calendar/archive/refs/heads/master.zip) и распаковать в удобное место
    * скачать и установить [Python-3.12 (64-разрядная версия)](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe) или [Python-3.12 (32-разрядная версия)](https://www.python.org/ftp/python/3.12.0/python-3.12.0.exe)
    * запустить файл install.bat

2. Отредактируйте файл '.env':   

    * LOGIN=test@mail.ru
    * PASSWORD=test
    * TIME=18000 (период проверки значение в секундах можно изменить )

3. Запуск:

   * wot.bat
   * можно запускать скрытно
   * открыть папку автозапуска Windows (нажать Win+R и ввести команду shell:startup)
   * создать ярлык на файл wot.vbs
