b = 0
while True:
    a = input("1-выдать, 2-посмотреть, 3-сбросить, 4-вернуть, 0-стоп: ")
    if a == "1":
        b = b + 1
    elif a == "2":
        print("выдано:", b)
    elif a == "3":
        b = 0
    elif a == "4":
        if b > 0:
            b = b - 1
        else:
            print("книг нет")
    elif a == "0":
        break
    else:
        print("-")
