import numpy as np
import sys
import array
#типы данных

# x=1
# print(type(x))
# print (sys.getsizeof(x))

# x= 'hello'
# print(type(x))

# x=True
# print(type(x))

# l1 = list([])
# print (sys.getsizeof(l1))

# l2 = list([1,2,3])
# print (sys.getsizeof(l2))

# l3 = list([1,"2",True])
# print (sys.getsizeof(l3))

# a1 =array.array('i',[1,2,3]) 
# print (sys.getsizeof(a1))
# print (type(a1))

##1.Какие еще существуют коды типов? i - int ...
##2.Напишите код  подобные приведенному выше (a1) но с другом типом

# a=np.array([1,2,3,4,5])
# print (type(a),a)

# a=np.array([1.23,4,5])
# print (type(a),a) ##повышающее приведение типов

# a=np.array([1.23,4,5], dtype=int)
# print (type(a),a)

# a = np.array([range(i,i+3) for i in [2,4,6]])
# print(a)

# a=np.zeros(10,dtype = int)
# print (a,type(a))

# print(np.ones((3,5) ,dtype = float))

# print(np.full((4,5), 3.1415))

# print(np.arange(0,20,2))

# print(np.eye(4))

##3. Напишите код для создания массива с 5 значениями, располагающимися через равными интервалы в диапозоне от 0 до 1

##4.  Напишите код для создания массива с 5 значениями, равномерно распределенными случайными значениями в диапозоне от 0 до 1
# 
# #  5.Напишите код для создания массива с 5 значениями, равномерно распределенными случайными значениями в диапозоне с мат. ожиданияем = 0 и дисперсией = 1

##6. Напишите код для создания массива с 5 случайными целими числами в [0,10)

###МАССИВЫ

np.random.seed(1)

x1 =np.random.randint(10,size=3)
x2  =np.random.randint(10,size=(3,2))
x3 =np.random.randint(10,size=(3,2,1))

# print(x1)
# print(x2)
# print(x3)

# print(x1.ndim, x1.shape,x1.size)
# print(x2.ndim, x2.shape,x2.size)
# print(x3.ndim, x3.shape,x3.size)

#Индекс с 0

# a = np.array([1,2,3,4,5])
# print(a[0])
# print(a[-2])

# a[1] = 20 
# print(a)

# a = np.array([[1,2],[3,4]])

# print(a)
# print(a[0,0])
# print(a[-1,-1])
# a[1,0]=100
# print(a)

# a = np.array([1,2,3,4])
# b =np.array([1.0,2,3,4])
# print(a)
# print(b)
# a[0]=10
# print(a)
# a[0]=10.123
# print(a)

## Срез [s:f:st] 01:shape:1]

# a= np.array([1,2,3,4,5,6])

# print(a[:3])
# print(a[2:])
# print(a[1:5])
# print(a[1:-1])
# print(a[1:6:2])
# print(a[1::2])

# print(a[::-1])

##7.Написать код для создания срезов для массива 3 на 4
##-первые две строки и три столбца
##-первые три строки и второй столбца
##-первые две строки и три столбца
##-третья строка

##8. Сделать срез как коппию

# a= np.arange(1,13)

# print(a)

# print(a.reshape(2,6))
# print(a.reshape(3,4))

##9.newaxis. Продемонстрируйте использоавание newaxis. для получения вектора-столбца и вектора- строки из массива

# x= np.array([1,2,3])
# y= np.array([4,5])
# z= np.array([6])

# print(np.concatenate([x,y,z]))

# x= np.array([1,2,3])
# y= np.array([4,5,6])
# r1 = np.vstack([x,y])
# print(r1)
# print(np.hstack([r1,r1]))

##10. Разобраться с методом dstack

##11
###Вычисления с массивами
#Векторизированная операция - независимо к каждому элементу

# x = np.arange(10)
# print(x)

# print(x*2+1)

# Универсальные функции


# print(np.add(np.multiply(x,2),1))

#- - / // ** %

##12. Привести пример использования всех универсальных функций

## np.abs, sin,cos,tan, exp, log,

# x=np.arange(5)
# y=np.empty(10)
# print(np.multiply(x,10,out=y[::2]))
# print(y)

# x = np.arange(1,5)

# print(x)
# print(np.add.reduce(x))
# print(np.add.accumulate(x))

##Векторные произведения
# x= np.arange(1,10)
# print(np.multiply.outer(x,x))
