import random
n=100
numbers = list(range(1,n+1))
x=numbers.pop(random.randint(1,n+1))
print(x)

# numbers2 = list(range(1,n+1))
# print(sum(numbers2)-sum(numbers))
# Bu optimal yechim hisoblanmaydi. chunki siz yana xotiradan joy oldingiz.

summa = n*(n+1)/2
print(summa - sum(numbers))
# To'g'ri yechim!!!