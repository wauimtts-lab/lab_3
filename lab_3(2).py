list1 = input("Введите города через пробел:").split()
list2 = input("Введите города через пробел:").split()

if len(set(list1 + list2))==6:
    result = list1 + list2
else:
    result = list(set(list1) - set(list2))
print(result)