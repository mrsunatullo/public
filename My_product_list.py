from os.path import exists

class My_List:
    def __init__(self):
        self.file_link = input("Введите адрес вашего файла: ")     #   '  C:\\2022Python\\MIXed\\Exercises 1\\1115.txt  '
        if not exists(self.file_link):
            raise FileNotFoundError('Путь к вашему файле не верный...')

        self.action_file()

    def action_file(self):
        choice = f'_________________________________________\n' \
                 f'- Для добавление новый продукта нажмите 1\n' \
                 f'- Для изменение цены продукта нажмите 2\n' \
                 f'- Для удаление продукта нажмите 3\n' \
                 f'- Для чтение полной информации файла нажмите 0\n' \
                 f'- Для выхода введите: exit\n\n' \
                 f' Введите то что вам нужно: '
        while True:
            self.action = input(choice)
            match self.action:
                case '0':
                    self.show_file()
                case '1':
                    self.add_to_file()
                case '2':
                    self.change_file()
                case '3':
                    self.delete_from_file()
                case 'exit':
                    exit()
                case _:
                    print("\t\t\t__________ \n\t\tНЕПРАВИЛЬНЫЙ ВЫБОР")


    def read_file(self) -> list:           # метод для чтение из файла
        with open(self.file_link, 'r') as file:
            return file.readlines()              # открывает файл и возврвшает по линиям


    def show_file(self):                   # метод 1 для возврашение элементов списка и обший стоимости товаров
        print(*self.read_file(), sep="")
        list_of_products = (''.join(self.read_file())).split()  # конвертируем сначала на сторока потом обрадно в список, для удаление лишных элементов
        sum = 0
        for price in list_of_products[1::2]:
            sum += float(price)
        print(f'Total price: {sum}$\n')
        self.action_file()

    def get_input(self):   # метод для получение ввода
        user_input = []
        user_input.append(input('Введите название продукта: '))     # добавляем назвение продукта
        while True:    # сделаем цикл до тех пор пользователь ввел число для цена
            try:
                user_input.append(float(input('Введите цена продукта: ')))
                return user_input   # возврашаем лист из одного продукта и цена. Пр- text = ['пиёз', 123123]
            except:
                print('Введите только числа для цены')

    def save_file(self, text):     # метод для сохранение данные с параметра на файл
        with open(self.file_link, 'w') as file:
            file.write(text)

    def formated_list(self, split_list): # метод для конвертации списка на строку для сохранение в текстовом файле
        result = list()
        for index in range(0, len(split_list), 2):
            result.append(f"{split_list[index]} {split_list[index + 1]}" + '\n')
        self.save_file(''.join(result))

    def add_to_file(self):  # метод для добавление новый запись в списке
        print('\n___ ДОБАВЛЕНИЕ ПРОДУКТОВ ___')
        user_input = self.get_input()
        more_lines = (''.join(user_input[0] + ' ' + str(user_input[1])) + '\n')   # проведем данные введеные пользователем в оределеныый формы для сохранение

        with open(self.file_link, 'a') as file:
            file.write(more_lines)
        print(self.show_file())
        self.action_file()

    def change_file(self):   # метод для изменение элементов списка
        print(*self.read_file(), sep="")
        splited_list = (''.join(self.read_file())).split()       # конвертируем список сначала на сторока потом обрадно в список, для удаление лишных элементов
        print('\n___ ИЗМЕНЕНИЕ ЦЕНЫ ПРОДУКТОВ ___')
        user_input = self.get_input()
        while True:
            if user_input[0] in splited_list:  # ишем первого введенного продукта в списке, если оно существует возвращаем его индекс
                index_item = splited_list.index(user_input[0])
                splited_list[index_item + 1] = str(user_input[1])   #  заменим следуший элемент по индесу списка на введенный пользователь цену
                self.formated_list(splited_list)
                return self.show_file()
            else:
                print('Продукт не существует в списке, \nпожалуйста убедитесь что вы ввели правильный название продукта')
                user_input = self.get_input()

    def delete_from_file(self):      # метод для удаление элемент из списка
        print(*self.read_file(), sep="")
        print('\n___ УДАЛЕНИЕ ПРОДУКТОВ ___')
        splited_list = ''.join(self.read_file()).split()
        user_input = self.get_input()  # метод self.get_input() возврашает лист в формате пр. text = ['пиёз', 123123]
        text = user_input
        while True:
            if text[0] in splited_list and splited_list[splited_list.index(str(text[0])) + 1] == str(text[1]):   # если первый элемент инпута находится в  списке а также его следующий элемент равен сo второй элементом инпута то их удаляем (удаляем продукта и цену)
                    splited_list.pop(splited_list.index(str(text[0])) + 1)  # сначала удаляем цену
                    splited_list.remove(text[0]) # удоляем название из списка
                    self.formated_list(splited_list)
                    return self.show_file()
            else:           # если пользователь ввёл неправильный продукт или цену цикл запускается снова
                print('Вы неправильно ввели название продукта или цены')
                user_input = self.get_input()
                text = user_input


if __name__ == '__main__':
    my_list = My_List()



