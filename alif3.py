x = ["Tomato", 20,"Onion", 10, "Potatoe", 15]
def Convert(x):
    dd = {x[i]: x[i+1] for i in range(0,len(x),2)}
    return dd
dic  = Convert(x)
for a,b in dic.items():
    print(a,b)
print(f"Обшая  сумма  товаров:   {sum(x[1::2])}$")

nn = input('add, change, delate: ')
if nn == "add":
    x.append(input('name: '))
    x.append(int(input('price')))
    print(x)

print(f"Обшая  сумма  товаров:   {sum(x[1::2])}$")







