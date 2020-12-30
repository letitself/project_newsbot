# project_newsbot

[слайды](презентация.pdf)

Эта программа — бот для телеграмма
Имя бота — @oleg_panorama_bot
бот выполняет две команды
1. /random_article — Выдача рандомной свежей статьи с сайтов панорама/рбк/медуза 
(пользователь может выбрать, из какого источника получить статью отправкой ссобщения боту 
(rbc/panorama/meduza) или выбором соответствующей клавиши на кастомизированной клавиатуре)
2. /freq_pie — Выдача круговой диаграммы с наиболее частотными осмысленными словами из 
статей с сайта панорама за последнее время
К сожалению, он не лежит на сервере, поэтому вам придется скачать программы и необходимые 
библиотеки и запустить у себя на устройстве.
3. Необходимые библиотеки:
requests==2.7.0
beautifulsoup4==4.9.0
telebot==0.0.3
matplotlib==3.2.1
pyTelegramBotAPI==3.6.7
программа для запуска — panorama_main.py
необходимо иметь
штука которая считает частотность слов-frequency (3).py
штука которая строит график-plot_panorama.py
штука которая парсит панораму и медузу-rbc_meduza.py
