b = 0
while True:
    a = input("1-выдать, 2-сколько, 3-сброс, 0-выход: ")
    if a == "1":
        b = b + 1
    elif a == "2":
        print("выдано книг:", b)
    elif a == "3":
        b = 0
    elif a =="0":
        break
    else:
        print("-")