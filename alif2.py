x = ["Tomato","Onion","Potatoe"]
y = [10,20,15]

for a in zip(x,y):
    print(a)

print(f"Обшая сумма товаров: {sum(y)}")

nn = input('Если хотите добавить новые продукты в списке напишите - ДА: ')
if nn == "ДА":
    print("")
    x.append(input('Напишите название продукта: '))
    y.append(int(input('Напишите цена продукта: ')))

    for a in zip(x, y):
        print(a)
    print(f"Обшая сумма товаров: {sum(y)}")







