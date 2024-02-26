import csv  # импорт библиотеки для работы с csv

with open('products.csv', 'r', encoding='utf-8-sig') as file:
    data = list(csv.DictReader(file, delimiter=';'))  # Записываем содержимое файла в список
    categ = input()
    while categ != 'молоко':  # Проверяем, можно ли дальще искать категории
        min_c = 99999
        min_pr = ''
        for prod in data:  # Находим нужную категорию и минимальное колличество(если такая категория есть
            if categ == prod['Category'] and min_c > float(prod['Count']):
                min_c = float(prod['Count'])
                min_pr = prod['product']
        for prod in data:  # Выводим нужные нам данные
            if categ == prod['Category'] and prod['product'] == min_pr and float(prod['Count']) == min_c:
                print(f"В категории: {categ} товар: {prod['product']} был куплен {prod['Count']} раз")
                break
        else:  # Если категории нет, выводим ошибку
            print('Такой категории не существует в нашей БД')
        categ = input()
