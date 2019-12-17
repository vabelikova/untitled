a = int(input('Введите х'))
b = int(input('Введите y'))
c = int(input('Введите z'))

if a > b and a > c:
    print ('x - наибольшее из чисел')
elif b > a and b > c:
    print ('y - наибольшее из чисел')
elif c > a and c > b:
    print ('z - наибольшее из чисел')
elif  a == b and a == c or b == a and b == c or c == a and c == b:
    print ('Числа равны')
