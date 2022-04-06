from Task.model.InfoSubject import InfoSubject


def createInfoSubject():
    print("\n - - - - ->  Новый продукт")
    category = input('Добавьте категорию: ')
    product = input('Введите название: ')
    cost = input('Цена: ')
    dateBuy = input('Введите дату: ')
    return InfoSubject(category, product, cost, dateBuy)
