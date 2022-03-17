import csv
import os

from Task.model.InfoSubject import InfoSubject


class InfoSubjectsCSV(object):
    def __init__(self):
        """Constructor"""
        self.__FILENAME = "InfoSubjects.csv"
        self.infoSubjects = list()
        self.checkingFile()

    def writeCSV(self):
        with open(self.__FILENAME, "a", newline="") as file:
            user = InfoSubject
            writer = csv.writer(file)
            writer.writerow(user)

    def add(self, infoSubject):
        with open(self.__FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(infoSubject.getTuple())
        self.infoSubjects.append(infoSubject)

    def deleteIndex(self, number):
        if number < 0:
            return "Номер пункта должен быть положительным числом"
        if len(self.infoSubjects) < number:
            return "Невозможно удалить запись {}, максимальный номер из списка: {}". \
                format(number, len(self.infoSubjects))
        element2 = self.infoSubjects[number]
        del self.infoSubjects[number]
        self.resetWriteFile()
        return "Удалена запись:\n{}".format(str(element2))

    def readCSV(self):
        with open(self.__FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                infoSubject = InfoSubject(row[0], row[1], row[2], row[3])
                self.infoSubjects.append(infoSubject)

    def checkingFile(self):
        if os.path.exists(self.__FILENAME):
            self.readCSV()
        else:
            print("Файл не существует")

    def resetWriteFile(self):
        with open(self.__FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            for infoSub in self.infoSubjects:
                writer.writerow(infoSub.getTuple())

    def getSorted(self):
        copyInfoSubjects = self.infoSubjects
        #5copyInfoSubjects.sort(key=custom_key)
        return copyInfoSubjects
