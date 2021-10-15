def chislonaoborot(x):
    strok = x
    x = abs(x)
    b = x
    d = 0
    while b > 0:
        a = x % 10
        b = x // 10
        d = d * 10 + a
        x = b
    if strok > 0:
        print("Обратное число: " + str(d))
    else:
        print("Обратное число: " + str(d * -1))
    return ""
try:
    x = int(input("Введите целое число: "))
    print(chislonaoborot(x))
except ValueError:
    print("Не пытайтесь меня обмануть. Введите целое число")
