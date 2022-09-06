product_price = ["Огурцы", 50,"Помидоры", 40, "Масло", 40]  #список продуктов и цена
def convert(product_price):     #функция для конвертация список на Словарь
    protuct_dict = {product_price[i]: product_price[i + 1] for i in range(0, len(product_price), 2)}
    return protuct_dict

operation = True   #Бесконечный цикл для действие со списком
while operation:
        sorted_dict = convert(product_price)
        for a,b in sorted_dict.items():    #Итерация для вывода словаря на экран
            print(a,b)
        print(f"\nОбшая  сумма  продуктов:   {sum(product_price[1::2])}-TJS")      # выбираем каждый второй элемент со списка и суммируем (целое число)
        operation = input('Выберите действия для: \nДобавление-add, Изменение-change, Удаление-delate, Завершение-Любой другой команда: ')  # Инструкция для пользователья
        if operation == "add":     # добавить элемент в список
            product_price.append(input('Наименование: '))
            while True:
                try:        #try и except для того чтобы пользователь ввел только число для цена
                    product_price.append(int(input('Цена: ')))
                    print("")
                    break
                except:
                    print("Попробуйте снова, пжалуйста введите целое число: ")
        elif operation =="delate":     # для удаление со списка

            product_price.remove(input("Наименование: "))
            while True:
                try:            #try и except для т ого чтобы пользователь ввел только число для цена
                    product_price.remove(int(input("Цена: ")))
                    print("")
                    break
                except:
                    print("Попробуйте снова, пжалуйста введите целое число: ")
        elif operation == "change":   # для изменение элемент списка
            while True:
                try:        #try и except для того чтобы пользователь ввел только число для цена
                    product_price[int(input("index num: "))] = input('Наименование: ')
                    print("")
                    break
                except:
                    print("Попробуйте снова, пжалуйста введите целое число: ")

            while True:
                try:        #try и except для того чтобы пользователь ввел только число для цена
                    product_price[int(input("index num: "))] = int(input("Цена: "))
                    print("")
                    break
                except:
                    print("Попробуйте снова, пжалуйста введите целое число: ")
        else:      # цикл остановиться при ввод неопределенной команда
            break
            








