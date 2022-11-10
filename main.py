import os
import pickle
import colorama
from colorama import Fore, Back, Style
colorama.init()

class Fari:

    def Vkl(self):
        self.fari = 'включены'

    def Vikl(self):
        self.fari = 'выключены'

class Car(Fari):

    def __init__(self, marka=None, color=None, model=None, box_type=None, engine_status="Выключен"):
        self.marka = marka
        self.model = model
        self.color = color
        self.fari = 'выключены'
        self.box_type = box_type
        self.engine_status = engine_status

class Mainvivod():
    def __init__(self):
        self.Vivod()

    def Vivod(self):
        while True:
            print(Back.MAGENTA + Fore.BLACK + 'Введите 1, если хотите добаить новый автомобиль ')
            print('Введите 2, если хотите редактировать информацию о некотором автомобиле ')
            print('Введите 3, если хотите посмотреть информацию о некотором автомобиле ')
            print('Введите 4, если хотите удалить автомобиль и все данные о нём')
            print('Введите 0, если хотите выйти из программы')
            what0 = input()
            print(Style.RESET_ALL)
            if what0 == '1':
                print(Fore.CYAN + 'Выбирите номер марки из списка или введите собственное значение')
                for i in range(len(spisokmarok)):
                    print(i + 1, ". ", spisokmarok[i], sep='')
                i = input()
                if (i.isdigit() == True) and (int(i) >= 0) and (int(i) <= len(spisokmarok)):
                    i = int(i)
                    mashinki.append(Car(marka=spisokmarok[i - 1]))
                elif (i.isdigit() == True):
                    print(Fore.RED + "Такого номера нет в списке")
                    continue
                else:
                    mashinki.append(Car(marka=i))
                pickle.dump(mashinki, open('mashinki.pickle', 'wb'))

            elif what0 == '2':
                if len(mashinki) == 0:
                    print(Fore.RED + 'Отсутствует информация о машинах')
                    continue
                else:
                    for i in range(len(mashinki)):
                        print(i + 1, '. ', mashinki[i].marka, sep='')
                    print(Fore.CYAN + 'Какую машину вы бы хотели изменить? Введите 0 для выхода')
                    i = input()
                    if (i.isdigit() == True) and (int(i) >= 0) and (int(i) <= len(mashinki)):
                        if int(i) == 0:
                            continue
                        else:
                            print(Fore.MAGENTA + '1. Изменить марку')
                            print('2. Изменить или добавить модель')
                            print('3. Изменить или добавить цвет')
                            print('4. Включить или выключить фары')
                            print('5. Изменить коробку передач')
                            print('6. Включить/выключить двигатель')
                            print('0. Выход')
                            what1 = input()
                            i = int(i) - 1
                            if what1 == '1':
                                print(Fore.CYAN + 'Введите марку')
                                mashinki[i].marka = input()

                            elif what1 == '2':
                                print(Fore.CYAN + 'Введите модель')
                                mashinki[i].model = input()

                            elif what1 == '3':
                                print(Fore.CYAN + 'Введите цвет')
                                mashinki[i].color = input()
                            elif what1 == '4':
                                while what2 == '':
                                    print(Fore.CYAN + '1. Включить')
                                    print(Fore.CYAN + '2. Выключить')
                                    what2 = input()
                                    if what2 == '1':
                                        mashinki[i].Vkl()
                                    if what2 == '2':
                                        mashinki[i].Vikl()
                            elif what1 == '5':
                                print(Fore.CYAN + 'Выберите тип коробки:\nМеханика - 1; Автомат - 2\n')
                                choise = int(input())
                                if choise == 1:
                                    mashinki[i].box_type = "Механика"
                                elif choise == 2:
                                    mashinki[i].box_type = "Автомат"
                                else:
                                    print("Введены неправильные данные, установлена механика по умолчанию!")
                                    mashinki[i].box_type = "Механика"
                            elif what1 == '6':
                                if "Выключен" == mashinki[i].engine_status:
                                    mashinki[i].engine_status = "Включен"
                                else:
                                    mashinki[i].engine_status = "Выключен"
                                print(f"Статус двигателя теперь {mashinki[i].engine_status}")
                            else:
                                neverno()
                            pickle.dump(mashinki, open('mashinki.pickle', 'wb'))
                    else:
                        neverno()

            elif what0 == '3':
                if len(mashinki) == 0:
                    print(Fore.RED + 'Отсутствует информация о машинах')
                    continue
                else:
                    for i in range(len(mashinki)):
                        print(i + 1, '. ', mashinki[i].marka, sep='')
                    print('0. Выход')
                    print(Fore.CYAN + 'Введите номер машины, данные о которой хотите посмотреть или введите 0 для выхода')
                    i = input()
                    if (i.isdigit() == True) and (int(i) >= 0) and (int(i) <= len(mashinki)):
                        if int(i) == 0:
                            continue
                        else:
                            i = int(i) - 1
                            if i == -1:
                                what0 = Mainvivod()
                            if mashinki[i].marka != None:
                                print(Fore.MAGENTA + 'Марка -', mashinki[i].marka)
                            if mashinki[i].model != None:
                                print(Fore.MAGENTA + 'Модель -', mashinki[i].model)
                            if mashinki[i].color != None:
                                print(Fore.MAGENTA + 'Цвет -', mashinki[i].color)
                            if mashinki[i].fari != None:
                                print(Fore.MAGENTA + 'Фары -', mashinki[i].fari)
                            if mashinki[i].box_type != None:
                                print(Fore.MAGENTA + 'Коробка -', mashinki[i].box_type)
                            if mashinki[i].engine_status != None:
                                print(Fore.MAGENTA + 'Двигатель -', mashinki[i].engine_status)
                            pickle.dump(mashinki, open('mashinki.pickle', 'wb'))
                    else:
                        neverno()

            elif what0 == '4':
                if len(mashinki) == 0:
                    print(Fore.RED + 'Нет машин для удаления')
                else:
                    for i in range(len(mashinki)):
                        print(i + 1, '. ', mashinki[i].marka, sep='')
                        print(Fore.CYAN + 'Введите номер машины, которую хотите удалить')
                        i = input()
                        if (i.isdigit() == True) and (int(i) >= 0) and (int(i) <= len(mashinki)):
                            if int(i) == 0:
                                continue
                            else:
                                i = int(i) - 1
                                del mashinki[i]
                        else:
                            neverno()
                        pickle.dump(mashinki, open('mashinki.pickle', 'wb'))
            elif what0 == "0":
                break
            else:
                neverno()

def neverno():
    print(Fore.RED + 'Было введено неверное значение')
def proverka1():
    if (os.path.exists("mashinki.pickle")==True):
        return True
    else:
        file = open('mashinki.pickle', 'a+')
        return False
def proverka2():
    with open('mashinki.pickle', mode="r") as file:
        if (os.path.getsize('mashinki.pickle') == 0) or (len(file.readline())==5):
            return []
        else:
            return pickle.load(open('mashinki.pickle', 'rb'))

proverka1()
mashinki = proverka2()
spisokmarok = ["Nissan", "Porsche", "Audi", "Hyundai", "Ford", "Volkswagen", "Honda", "BMW", "Mercedes-Benz", "Toyota"]
a = Mainvivod()