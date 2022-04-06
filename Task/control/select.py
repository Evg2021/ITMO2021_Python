from Task.view import show


def selectCategory(infoSubjects):
    print("Есть следующте категории: ", end="")
    setCategorys = set()
    for iSub in infoSubjects.infoSubjects:
        setCategorys.add(iSub.category)
    print(setCategorys)
    category = input('\nНазвание категории: ')
    show.showCategoryInfoSubjects(infoSubjects, category)


def selectDate(infoSubjects):
    print("Какие даты: ", end="")
    setDates = set()
    for iSub in infoSubjects.infoSubjects:
        setDates.add(iSub.dateBuy)
    print(setDates)
    dateBuy = input('\nВведите дату: ')
    show.showDateInfoSubjects(infoSubjects, dateBuy)


def deleteNumber(infoSubjects):
    index = input('\nКакой номер записи будем удалять?: ')
    if index == "end" or index == "'end'":
        print("Отмена")
    if not index.isdigit():
        print("ERROR!!!! Для удаление нужно ввести номер")
        print("Для отмены напишите 'end'")
        deleteNumber(infoSubjects)
    index = int(index) - 1
    print(infoSubjects.deleteIndex(index))

