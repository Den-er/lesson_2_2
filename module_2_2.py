#first, second и third
first = int(input("Введите число: "))
second= int(input("Введите число: "))
third= int(input("Введите число: "))
if first == second and third ==second and third == first:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print (0)