product_list = ["Огурцы", 50,"Помидоры", 40, "Масло", 40]  #список наименование и цена продуктов
def convert_list_to_dict(product_list):     #функция для конвертация список на Словарь
    product_dict = {product_list[i]: product_list[i + 1] for i in range(0, len(product_list), 2)}
    return product_dict

operation_with_list = True   #Бесконечный цикл для действие со списком
while operation_with_list:
        sorted_dict = convert_list_to_dict(product_list)
        for a,b in sorted_dict.items():    #Итерация для вывода словаря на экран
            print(a,b)
        print(f"\nОбшая  сумма  продуктов:   {sum(product_list[1::2])}-TJS")      # выбираем каждый второй элемент со списка и суммируем (целое число)
        operation_with_list = input('Выберите действия со списком: Добавить-add, Изменить-change, Удалить-delate, Завершение-Любой другой команда: ')  # Инструкция для пользователья
        if operation_with_list == "add":     # добавить элемент в список
            product_list.append(input('Ведите название продукта который хотите добавить: '))
            while True:
                try:        #try и except для того чтобы пользователь ввел только число для цена
                    product_list.append(int(input('Цена продукта: ')))
                    print("")
                    break
                except:
                    print("Попробуйте снова, пжалуйста введите целое число для цена: ")
        elif operation_with_list =="delate":     # для удаление со списка

            product_list.remove(input("Ведите название продукта который хотите удалить: "))
            while True:
                try:            #try и except для т ого чтобы пользователь ввел только число для цена
                    product_list.remove(int(input("Ведите цена продукта который хотите удалить: ")))
                    print("")
                    break
                except:
                    print("Попробуйте снова, пжалуйста введите целое число для цена: ")
        elif operation_with_list == "change":   # для изменение элемент списка
            while True:
                try:        #try и except для того чтобы пользователь ввел только число для цена
                    product_list[int(input("Ведите индекс продукта который хотите заменить: "))] = input('Ведите новое название для продукта на который хотите заменить: ')
                    print("")
                    break
                except:
                    print("Попробуйте снова, пжалуйста введите целое число для цена: ")

            while True:
                try:        #try и except для того чтобы пользователь ввел только число для цена
                    product_list[int(input("Ведите индекс цена продукта который хотите заменить: "))] = int(input("Ведите новое цена для продукта на который хотите заменить: "))
                    print("")
                    break
                except:
                    print("Попробуйте снова, пжалуйста введите целое число для цена: ")
        else:      # цикл остановиться при ввод неопределенной команда
            break









