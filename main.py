# делаем срезы
#
# x = input()
#
# print(x[2])
# print(x[-2])
# print(x[:5])
# print(x[0:-2])
# print(x[::2])
# print(x[1::2])
# print(x[::-1])
# print(x[::-2])
# print(len(x))






# кол-во слов
#
# x = input()
#
# print(x.count(' ')+1)





# две половинки
#
# x = input()
#
# print(x[len(x)//2+len(x)%2:]+x[:len(x)//2+len(x)%2])





# первое и последнее вхождения
#
# x = input()
#
# print(x.find('f'), x.rfind('f'))




# Удаление фрагмента
#
# x = input()
# a = x[x.find('h') : x.rfind('h')+1]
#
# print(x.replace(a,''))





# замена подстроки
#
# x = input()
#
# print(x.replace('1','one'))





# удаление символа
#
# x = input()
#
# print(x.replace('@',''))





#Замена внутри фрагмента
#
# x = input()
#
# a = x[:x.find('h')+1]
# b = x[x.find('h')+1: x.rfind('h')]
# c = x[x.rfind('h'):]
# x = a+b.replace('h','H')+c
# print(x)





#Минимум из двух чисел
#
# x = int(input())
# y = int(input())
#
# if x>y:
#     print(x)
# else:
#     print(y)





#знак числа
#
# sign = int(input())
#
# if sign == 0:
#     print(0)
# elif sign > 0:
#     print(1)
# else:
#     print(-1)





#шахматная доска
#
# a =int(input())
# b =int(input())
# c =int(input())
# d =int(input())
#
# if (a+b)%2 == (c+d)%2:
#     print("YES")
# else:
#     print("NO")






#високосный год
#
# x = int(input())
#
# if x%4==0 and x%100!=0 or 100%x!=0 and x%100==0 or 100%x==0:
#     print('YES')
# else:
#     print('NO')
