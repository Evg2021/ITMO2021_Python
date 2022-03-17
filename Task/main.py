from Task.model.InfoSubjectsCSV import InfoSubjectsCSV
from Task.control.createInfoSubject import createInfoSubject
from Task.view import show
from Task.control import select
from Task.control import sorted

def main():
    infoSubjects = InfoSubjectsCSV()
    while (True):
        show.showMenu()
        valueMenu = input('Введите номер: ')
        if valueMenu == "1":
            infoSubject = createInfoSubject()
            infoSubjects.add(infoSubject)
            print(infoSubject)
        elif valueMenu == "2":
            show.showAllInfoSubjects(infoSubjects)
        elif valueMenu == "3":
            select.selectDate(infoSubjects)
        elif valueMenu == "4":
            select.selectCategory(infoSubjects)
        elif valueMenu == "5":
            sorted.sortedMinMax(infoSubjects)
        elif valueMenu == "6":
            select.deleteNumber(infoSubjects)
        elif valueMenu == "0":
            break
            print("КОНЕЦ! Спасибо за участие!")


main()