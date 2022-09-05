x = ["Огурцы", 50,"Помидоры ", 40, "Масло ", 40]
nn = True
while nn:
        def Convert(x):
            dd = {x[i]: x[i+1] for i in range(0,len(x),2)}
            return dd
        dic  = Convert(x)
        for a,b in dic.items():
            print(a,b)
        print(f"\nОбшая  сумма  продуктов:   {sum(x[1::2])}-TJS")

        nn = input('add, change, delate: ')
        if nn == "add":
            x.append(input('Наименование: '))
            x.append(int(input('Цена: ')))
            print("")
        elif nn =="delate":
            x.remove(input("Наименование: "))
            x.remove(int(input("Цена: ")))
        elif nn == "change":
            x[int(input("index num: "))] = input('Наименование: ')
            x[int(input("index num: "))] = int(input("Цена: "))

        else:
            break








