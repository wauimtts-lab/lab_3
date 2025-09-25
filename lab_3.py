#1
a = int(input("Введите a: "))
b = int(input("Введите b: "))

if a%3 ==0 and b %3 == 0:
    print( (a + b) // 3)
else:
    print ((a+b)*3)