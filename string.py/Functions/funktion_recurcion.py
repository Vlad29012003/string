# пример рекурсии
# def recurcion (avlue):
#     print (avlue)
#     if avlue < 10:
#         recurcion (avlue+1)
# recurcion(1)


# lambda - функция (анонимная, можно не присваивать ссылку  )
# def f(x):
#     return x **2
# print (f(3))
# aaa= lambda x: x**2
# print (aaa(3))

# aa = lambda a,b,c: a+b+c
# print (aa(2,4,5)

# пример ДЕКОРА ОРА 
# def fun_decoration (funk): 
#     def wrapper():
#         print ('i made something for incomming')
#         funk()
#         print ('я чтото делаю для выщова ')
#     return wrapper

# def some_funk ():
#     print ('вызов функции')
# f = fun_decoration (some_funk)
# f()

# задание 1
# f = lambda a,b,c: a*b*c
# g = 'обьем бассейна'
# print(g,f(34,44,55))

# залание 2 
# c = lambda a: 365 - a
# b =int (input('введите число  '))
# print (c(b))


def recurcion (avlue):
    print (avlue)
    if not avlue % 2 == 0 :
        recurcion(avlue+2)
        return avlue
recurcion (1)