import csv  # импорт библиотеки для работы с csv

with open('products.csv', 'r', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter=';'))  # Записываем содержимое файла в список
    for prod in data:
        prod['total'] = float(prod['Price per unit']) * float(prod['Count'])  # Рассчитываем значения для нового столбца

with open('products_new.csv', 'w', encoding='utf-8-sig') as file:  # Создаём или перезаписывам нужный нам файл
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count'
                                                             'total'])
    writer.writeheader()  # Добовляем заголовки столбцов
    writer.writerows(data)  # Заполняем файл данными
