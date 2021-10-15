number = int(input("Введите целое число: "))

revs_number = 0
n1 = number
if (number < 0):
    number=-number

while (number > 0):

    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10
if (n1 < 0):
    revs_number = -revs_number
print("Обратное чило: {}". format (revs_number))
