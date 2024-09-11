# Задание 1 - Поиск багов на скриншоте 
Сравнение шкриншота с аналагичной страницей Avito (https://www.avito.ru/sankt-peterburg/avtomobili/bmw/x6/polnyy_privod-ASgBAgICA0Tgtg3klyjitg2~tCjutg3qtyg?cd=1&f=ASgBAgECA0Tgtg3klyjitg2~tCjutg3qtygCRcaaDBh7ImZyb20iOjAsInRvIjoxMDAwMDAwMH36jBQXeyJmcm9tIjoyMDIxLCJ0byI6MjAyNH0&radius=0&searchRadius=0).      
При условии что все фильтры со скриншота уже применены.

## Список багов

Заголовок и хлебные крошки 
Номер | Скрин | Кратное описание бага  | Приоритет
--|----------|--------------------| -------------
1 |![image](https://github.com/user-attachments/assets/2bd40102-e809-44f0-84d0-bb963ebc894e)|В заголовке присутствует лишний символ в количестве найденных предложений | low

Банер
Номер | Скрин | Кратное описание бага  | Приоритет
--|----------|--------------------| ------------- 
2 |![image](https://github.com/user-attachments/assets/b1f58daf-e25b-4433-b8c3-c4401cbbc3d8) |В баннере "Скидка на новое авто" присутсвует кнопка без текста внутри | high 


Фильтры
Номер | Скрин | Кратное описание бага  | Приоритет
--|----------|--------------------| -------------
3 |![image](https://github.com/user-attachments/assets/d717e919-3cbb-4cc3-9dea-6992d975995d)|При выбранном фильтре марки "BMW" отображаются и другие марки автомобилей| high 
4 |![image](https://github.com/user-attachments/assets/39317942-f981-4533-afcf-1c665cb683b2)|При выбранном фильтре привода "полный", отображаются автомобили с "передним" приводом | high 
5 |![image](https://github.com/user-attachments/assets/09fd6c2d-9151-4b7b-b301-e2c33b3c097c)|Отображение объявлений о продаже запчастей среди автомобилей (причем даже не той же марки)| high 
6 |![image](https://github.com/user-attachments/assets/46be55e2-aee6-448f-97bc-95a00560e2fe)|При выбранном фильтре года выпуска "от 2021 до 2024 года", отображаются автомобили других лет | medium
7 |![image](https://github.com/user-attachments/assets/91d73632-d461-46c1-a20f-ac7a0d3d7b41)|Выбраный фильтр локации "Санкт-Петербург" выводит оъявления не из Санкт-Петербургa | medium
8 |![image](https://github.com/user-attachments/assets/1c1f6a87-ed2b-4bbf-b5b2-b2c6f94a6a5a)|Орфографическая ошибка в фильтре "Поколение" (написано "покление") | low
9 |![image](https://github.com/user-attachments/assets/05d2cf2b-2d68-4220-8fc9-ad257c2a6869)|В фильтре выбора года число лет разбивается как тысячи (рубли) | low


Товары
Номер | Скрин | Кратное описание бага  | Приоритет
--|----------|--------------------| -------------
10|![image](https://github.com/user-attachments/assets/9ffb7a65-0d6f-4178-8d9e-a8666d3aeeb4)|В объявлении "Лобовое стекло Mercedes G63" съехала кнопка "Добавление в избранное" | high
11|![image](https://github.com/user-attachments/assets/e5f78ab9-7726-42d5-bfc0-be8de03d622f)|В объявлении BMW x6 3.0 AT 2021 не показывается картинка |  medium
12|![image](https://github.com/user-attachments/assets/6bc1a049-7cc7-48f5-bdcc-5ccde914b01b)|Сместилось фото из-за лейбла "только на авито" |  medium
13|![image](https://github.com/user-attachments/assets/2b594e76-ddbf-497f-9eb3-02a25e480c43)|В объявлении BMW x6 3.0 AT 2022 (белого цвета) метка "Соотвествует оценке" показывается под карточкой объявления | low
14|![image](https://github.com/user-attachments/assets/b93155fe-dd1c-452b-a8e7-143a906c1294)|Указан некорректный адрес | low
15|![image](https://github.com/user-attachments/assets/ef8c8368-6eb0-43e7-97f4-61bf51d5c4e0)|Неверное склонение в дате публикации| low
 
