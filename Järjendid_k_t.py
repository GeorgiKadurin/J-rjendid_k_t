#30/02/23
slovo_list="Kvinka sloumo, v ananas idite"








#---------------------------------

a=int(input("введи позиции, которую хочешь убр"))
if a>0 and a<len(slovo_list):
    slovo_list.pop(a-1)
    print(slovo_list)
else:
    print("ei ole see postion")


#------------------------------------

a=input("Введи букву которую удалить ")
a=a.lower()
listcopy_list=[]
for t in (slovo_list):
    listcopy_list.append(t.lower())
print(listcopy_list)
h=listcopy_list.count(a)

if h>0:
    for i in range(h):
        listcopy_list.remove(a)
else:
    print("Такой буквы нет")
print(listcopy_list)

#---------------------------------

a=input("Введи букву ")
i=int(input("Введи номер поз"))
slovo_list.insert(i-1,a)
print(slovo_list)
#------------------------------


















1-6
список=[]
print("Выбери более понравившейся вариант от 1 до 6")
while True:
    print("1-слова большими")
    print("2-слова маленькими")
    print("3-Разбиение строки по разделителю ")
    print("4-Переводит первый символ строки в верхний регистр, а все остальные внижний ")
    print("5-Переводит символы нижнего регистра в верхний, а верхнего – в нижний")
    print("6-Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний")
    print("7-КОНЕЦ")
    pan_Am=float(input())
    if pan_Am==1:
        a=input("Введи букву/слово: ")
        print(a.upper())
        print(f"Добавили {a} ",список)
        
    elif pan_Am==2:
        b=input("Введи букву: ")
        print(b.lower())
        print(f"Добавили {b} ",список)

    elif pan_Am==3:
        s=input("Введи букву: ")
        print(s.split())
        print(f"Добавили {s} ",список)

    elif pan_Am==4:
        c=input("Введи букву: ")
        print(c.capitalize())
        print(f"Добавили {c} ",список)

    elif pan_Am==5:
        v=input("Введи букву: ")
        print(v.swapcase())
        print(f"Добавили {v} ",список)

    elif pan_Am==6:
        b=input("Введи букву: ")
        print(b.title())
        print(f"Добавили {b} ",список)

    elif pan_Am==7:
        break

      
 #7-9   
print()
print("сложение строк")
print()
S1 = str(input(""))
S2 = str(input(""))
print()
print(S1 + S2) 
print()
print("Повторение строки")
print()
print('цветы, ' * 3)
print()
print("Длина строки")
print()
s=len(input(""))
print(s)
print()

           
print()
print()
spisok=[] #Пустой список
numbers=[1,2,3,4,5]
abc=["A", "B", "C"]
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)



#Самостоятельная работа 
список_вещей=[]
a=input(" ") #Придумай какие вещи можно взять с собой в поездку
slovo_list=list(a)
print(a)

while True:
    print("1-добавить предмет в список")
    print("2-добавить предмеи на x - позицию")
    print("3-удалить предмет")
    
    awp=int(input())
    if awp==1:
        r=input("Введите названия предмета:")
        a.append(r)
        print(f"Добавили {r} новый список", a)
    elif awp==2:
        r=input("Введите предмет, который хотите добавить: ")
        i=int(input("Введиту позицию, куда хотите добавить предмет: "))
        a.insert(i-1,r) #0,1,2,3,4,5...
        print(a)
    elif awp==3:
        r=input("Введи букву, которую хочешь удалить")
        g=a.count(a)
        if g>0:
           for i in range(g):
                a.remove(r)
        else:
            print("Искомой буквы нет")
        print(a)
        break











while True:
    print("1-добавить букву в список")
    print("2-склеить список\n3-добавить букву на i - позицию")
    print("4-удалить элемент")
   
    valik=int(input())
    if valik==1:
        a=input("Введи букву")
        slovo_list.append(a)
        print(f"Добавили {a} новый список", slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("Введи букву, которую хочешь добавить")
        i=int(input("Введи позиции, куда хочешь добавить б"))
        slovo_list.insert(i-1,a) #0,1,2,3,4,5...
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить")
        n=slovo_list.count(a)
        if n>0:
           for i in range(n):
                slovo_list.remove(a)
        else:
            print("Искомой буквы нет")
        print(slovo_list)








