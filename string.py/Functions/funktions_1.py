# def...<name>(args):
#     <body>
#     print('logic')
#     <name>(......)


# def send_text():
#     text = 'мы наконец то создаоои ланную функцию'
#     print (text)
# send_text()

# def counter():
#     a = int(input(':'))
#     b = int(input(":"))
#     print ("total",a+b)
# counter()

# def hello_name (from_name):
#     text = f'меня зовут {from_name}"'
#     print (text)
# hello_name('agill')
# hello_name ('nurzada') 

# def country (cyty = 'bishkek'):
#     print ('я из '+ cyty)
# country()
# country('talasa')
# country('new-yurk')



# глобальные и локальные переменные 
#  def num():
#     a,b = 1,2 local
#     print (a,b,c)

# a,b,c = 4,6,9 global
# num() 

# def hi():
#     name = 'agill'
#     print (name)

# name = 'nurzada'
# hi()

# print (name)

# numbers = [2,3,5,2,6,3,7,8,3,3,6,4]
# def num():
#     chet = []
#     nethet = []
#     for i in numbers:
#         if i  % 2 ==0:
#             chet.append (i)
#         else:
#             nethet.append(i)
#     print (chet,nethet)
# num()



# задание 1 
# def spisok ():
#     list_1 = ['name', 'age', '1', '19']
#     x = list_1[1::-1]
#     y = list_1 [3:1:-1]
#     print (x+y)
# spisok()

# задание 2
# def fibonachi():
#     f_1 =1
#     f_2 =1
#     a = int(input ('ввелите число  '))
#     for i in range (a):
#         f_1,f_2 = f_2, f_1 + f_2
#         print (f_2, end=' ')
# fibonachi()

# задание 3
# def method_1():
#     a = int (input (':'))
#     b = int (input(":"))
#     c = a + b
#     d = a - b
#     print (c)
# method_1()

# задание 4
# def name():
#     name = input('введите назван    ')
#     a = open (name,mode = 'w')
#     a.close ()
# b = name 
# print (b ())

