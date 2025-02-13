# Телеграм комиксы

Репозиторий предназначен для публикации комиксов с сайта [xkcd](https://xkcd.com/) через телеграм-бота в телеграм-канал.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### main.py

Для работы потребуется создать телеграм бота через [@BotFather](https://t.me/BotFather), получить его HTTP API токен, и положить его в переменную окружения TG_TOKEN.


Запуск осуществляется командой:

`python3 main.py *интервал времени между публикацией комиксов*`

При запуске скрипта запускается телеграм-бот, который с введённым интервалом времени(по умолчанию - 4 часа) отправляет комиксы в телеграм-канал с указанным chat_id.


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
