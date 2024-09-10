# avito-tech_QA_24
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
git clone https://github.com/AlexanderaIshchenko/avito-tech_QA_24.git
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
### Скачайте ChromeDriver
__Для Windows__  
1. Скачайте [ChromeDriver](https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.119/win64/chrome-win64.zip).    
2. Разархивируйте его и положите файл `chromedriver.exe` в удобную директорию, например `C:\Users\mirov\Downloads\`.  
3. Добавьте путь к ChromeDriver в переменные среды:  
* Перейдите в "Параметры системы" → "Дополнительные параметры системы" → "Переменные среды".  
* В разделе "Переменные пользователя" найдите переменную `PATH` и добавьте путь к папке с `chromedriver.exe`.  
4. После этого проверьте снова:  
```
chromedriver --version
```  
Если все настроено правильно, эта команда должна показать версию установленного ChromeDriver.  
***
__Для Mac__  

Выполните следующие команды в терминале, чтобы установить ChromeDriver:
```
brew install chromedriver
```
Добавление в PATH (если путь не настроен):  
* После установки ChromeDriver его нужно добавить в `PATH`.

Откройте файл `~/.bashrc` (или `~/.bash_profile`):
```
nano ~/.bashrc
```
Добавьте строку:  
```
export PATH=$PATH:/path/to/chromedriver
```
Замените `/path/to/chromedriver` на фактический путь к ChromeDriver.  

Примените изменения:  
```
source ~/.bashrc
```
После этого проверьте снова:  
```
chromedriver --version
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
