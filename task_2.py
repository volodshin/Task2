def kvadrat():
    number = int(input("Введіть число: "))
    P = number**2
    S = number * 4
    D = (2*number**2) ** 0.5
    print("Периметр: {} \nПлоща: {} \nДіагональ: {}".format(P, S, D))

print(kvadrat())