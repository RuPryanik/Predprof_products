import csv  # импорт библиотеки для работы с csv


def promo(product):  # Создаём функцию для генерации промокода
    date, month, year = product['Date'].split('.')
    promocode = product['product'][:2] + date + (product['product'][-2:])[::-1] + month[::-1]
    return promocode


with open('products.csv', 'r', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter=';'))  # Записываем содержимое файла в список
    for prod in data:
        prod['promocode'] = promo(prod)  # Рассчитываем значения для нового столбца

with open('product_promo.csv', 'w', encoding='utf-8-sig') as file:  # Создаём или перезаписывам нужный нам файл
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['Category', 'product', 'Date', 'Price per unit',
                                                             'Count', 'promocode'])
    writer.writeheader()  # Добовляем заголовки столбцов
    writer.writerows(data)  # Заполняем файл данными
