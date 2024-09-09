# avito-tech_QA_24
# avito-tech_QA
### В репозитории содержатся файлы:
1) Папка task_2, - второе задание проекта
   - TESTCASES.md - тест-кейсы на пользовательские сценарии
   - auto_tests.ru - сам файл с автотестами
   - BUGS.md - баг-репорты
3) task_1.md - первое задание проекта

# Инструкция по запуску тестов Avito
### Установить:
1) Python с пакетный менеджер pip
   - Если у вас нет Python, скачайте и установите его с [официального сайта Python](https://www.python.org/). Рекомендуется использовать версию Python 3.7 или выше.
2) Браузер, совместимый с Playwright (по умолчанию, Chromium)
   - Если у вас нет, скачайте и установите его [Chrome](https://googlechromelabs.github.io/chrome-for-testing/#stable).


### Склонируйте репозиторий
Вы можете клонировать репозиторий с помощью команды git:
```
git clone https://github.com/AlexanderaIshchenko/avito-tech_QA.git
```
### Создать виртуальное окружение 
```
'python -m venv venv'
```
### Включить виртуальное окружение 
```
'source venv/Script/activate'
```
### Установите pytest-playwright
```
pip install pytest-playwright
playwright install
```
### Запустить тесты

После успешной установки зависимостей выполните следующие действрия для запуска тестов:
1) Откройте терминал
2) Перейдите в каталог с репозиторием, используя команду 'cd'
3) Запустите тест, выполнив соответсвующий python файл:
```
pytest test_auto_backend.py
```
Это запустит все тесты в файле по очереди
