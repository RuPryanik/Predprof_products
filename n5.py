import csv  # импорт библиотеки для работы с csv

with open('products.csv', 'r', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter=';'))  # Записываем содержимое файла в список
    data_new = {}  # Создаём словарь для записи общих категорий
    for prod in data:  # Считаеи колличество товаров в категориях
        data_new[prod['Category']] = data_new.get(prod['Category'], 0) + float(prod['Count'])
    data_s = []  # Создаём список для сортировки категорий
    for prod in data_new:  # Заполняем список данными
        data_s.append({prod: data_new[prod]})
    min_s = []  # Создаём список с колиличеством товаров
    for prod in data_new:
        min_s.append(data_new[prod])
    min_s.sort()
    for i in range(10):  # Выводим нужные нам данные
        for prod in data_new:
            if data_new[prod] == min_s[i]:
                print(f'{prod}, {data_new[prod]}')
