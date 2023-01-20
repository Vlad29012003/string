# module OS.
# import os
# print(os.name)   название операционной системы
# print (os.getlogin()) название операционной системы
# print (os.uname()) информация операциооной системы

# import sys
# print(sys.platform) путь в котором вы назодитесь 
# print (sys.version) версия питона 

# from datetime import *
# print (datetime.now()) показывает точное время и дату 
# a = datetime (2023,1,13,12,9,12)
# print (a) задаеться полная да от голда до секуукнды (по вашему усмотрению )
# 
# b = time (11,34,56) задаетья нужное время 
# print (b)
# c = time (hour = 11,minute = 33,second= 12) жетально описывает время

# import time
# print ('agill')
# time.sleep (5)
# print ('hello') задержка в 5 секунд

# for i in range (5):
#     print ('agil pomochi po baratski')
#     time.sleep(3)

# d = date (2023,1,5)
# print (d)

# from datetime import *
# now = datetime.now()
# t = now.strftime("%H:%M:%S") формат сокращения по часу минут секунд
# print ('time:', t)


# s = now.strftime("%,%m,%d")
# print (s)

# import 
# my_list = ['agill','banana', 'apple','egida']
# print(my_list) 
# print (random.choice (my_list))

# import urllib.request модуль для открытия url адресов 
# responce = urllib.request.urlopen ('https://www.itcbootcamp.com/#/') 
# print (responce.read()) считываеться html код страницы 
# print (responce.getcode) код досьупа 200 что значит подходит для получения информации


# import csv
# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["ID", "Name", "Duration"])
#     writer.writerow([1, 'Aktan', 'Python'])
#     writer.writerow([2, 'Dima', 'JS'])
#     writer.writerow([3, 'Amal', 'Flutter'])
import random 

a = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
b = random.sample (a, 4)
print (b)