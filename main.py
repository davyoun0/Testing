#Programming languages: Java, C++, Python
#Python is used for Data Science or Machine Learning (AI)

#Variables
# 4 main types of variables:
# 1. Integer(int) --> negative, zero, positive numbers, -3, 0, 1,999
# x=5
# print(x)
# print(type(x))

# 2. Float(float) --> decimal number, ex) -3.14, 0.0
# 3. String(str) --> a text: character/letter, word, sentence, paragraph...
# 4. Boolean --> True or False

# x = 5
# y = 3.14
# print(y)
# print(type(y))
# z = "Hello"
# print(z)
# print(type(z))
# b = True
# b2 = False
# print(b2)
# print(type(b2))
# print(x + y)
# print(x * y)
# print(int(x / y))

# % - Modulo (Mod), A % B --> the remainder when i divide A by B
# print(x % y)
# print(11 % 3)

# // -> returns the quotient
# print(11 // 3)

# && --> exponent/power
# print(2 ** 3)
# print(3 ** 2)

# Rules for Variable name
# 1. Variable name cannot contain white spaces
# student name = "Scott"
# student_name = "Scott"
# 2. Variable name can contain digits(numbers), but it cannot start with digits
# 2student = "Jason", Error
# student2 = "Jason"
# 3. Variable name shouldn't contain special characters other than '_'
# 4. Variable name usually start with lower case.
# 5. Variable name should be meaningful.

# input --> input is for getting a value from the user
# x = input("Enter a number: ")
# print(x)
# name = input ("What is your name? ")
# age = input("How old are you? ")
# print ("Hello", name, "You are", age, "years old")
# if you get value using input, then the variable type is String

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# print(x+y)

# x= float(input("Enter a number: "))
# print(x**2*3.14)

# x= int(input ("Enter the temperature in Celsius: "))
# print ("Here is the Farenheit-", x*9/5+32)

# name= input ("What is your name? ")
# age= input ("How old are you? ")
# hobby= input("What's your favorite hobby?")
# # print("Hello,", name,".", "You are", age, "nice to meet you")
# # print("Hello "+name+" You are "+str(age)+" years old")
# print(f"Hello, {name}, You are {age} years old, You like {hobby} Please know that Davy always loves you")

# Conditionals --> giving options
# Indentation is very important in python
# Indentation is used to define the structure and hierarchy of code blocks
# if (condition):
# '=' vs '=='
# '=' when we assign a value to a variable
# '==' is to check whether to values are same or not
# '!=' --> not equal
# x = 3
# if x > 5:
#     print (x)
#     print("Bye")

# x = 3
# if x > 10:
#     print("x is big")
# else:
#     print ("x is small")

# x=11
# if x%2 == 0:
#     print("even")
# else:
#     print("odd")

# x=7
# if x>10:
#     print("Big")
# elif x>5:
#     print("Mid")
# elif x>2:
#     print("Mid")
# else:
#     print ("Small")

# x=90
# if x>=90:
#     print("A")
# elif x>=80:
#     print("B")
# elif x>=70:
#     print("C")
# elif x>=60:]
# []

#     print("D")
# else:
#     print("F")
# Logical Operator
# Not, And, Or
# Boolean = ONLY True or False
# print(True and False) = False
# 여기서 and, or 은 완전 다른 개념
# x y notx xandy xory
# t t f       t   t
# t f f       f   t
# f t t       f   t
# f f t       f   f
# and = always all true
# or = one of them true

# if x>10 or x<5:
#     print ("x is in the range between 5~10 (exclusive)")
# x=20
# if x%4 ==0 or x%7 ==0:
#     print("x is divisible by either 4 or 7")

# #nested if
# x=50
# if x<100:
#     if x%10==0:
#         print("x is multiple of ten, less than 100")

# x=99
# if x== 100:
#     print("A+")
# if x>=90:
#     if x%10 >=7:
#         print("A+")
#     elif x%10 >=3:
#         print("A")
#     else:
#         print ("A-")
# if x>=80:
#      if x%10 >6:
#         print("B+")
#     elif x%10 >3:
#         print("B")
#     else:
#         print ("B-")
# if x>=70:
#      if x%10 >=7:
#         print("C+")
#     elif x%10 >=3:
#         print("C")
#     else:
#         print ("C-")
# else:
#     print ("F")

# x = 76
# if x==100:
#     print("A+")
# if x >= 90 and x <100:
#     print("A")
#     if x % 10 < 3:
#         print ("-")
#     elif x % 10 > 6:
#         print ("+")
# if x >= 80 and x < 90:
#     print("B")
#     if x % 10 < 3:
#         print ("-")
#     elif x % 10 > 6:
#         print ("+")
# if x >= 70 and x < 80:
#     print("C")
#     if x % 10 < 3:
#         print ("-")
#     elif x % 10 > 6:
#         print ("+")
# else:
#     print("F")
# LOOPS 반복하는
#  for or while
# #for -> limited number of times
# #while -> condition
# for i in range(10):
#     print (i)
# range n s s se

# f=1
# for i in range (1,5):
#     f=f*1

# f=1
# for i in range(1,5):

#     print("original f", f)
#     print("equation", f, "*", i)
#     f=f*1
#     print("result f", f)
#     print()
# factorial

# count = 1
# while count <=10:
#     print(count)
#     count += 1

# x = int(input("Enter a number(0to finish): "))
# while x !=0:
#     print(x)
#     x=int(input("Enter a number(0 to finish): "))

# x = int(input("Enter a number(0to finish): ")) while x !=0:
#      break
#     else:
#         print(x)
# while True:
#     x= int(input("Enter a number(0 to finish): "))
#     if x ==0:
#         break
#         print(x)
#     elif x>0:
#         print(x)
#     else:
#         continue
#         print(x)
# print ("loop finished")

# import random

# x=random.randint(1,10)

# while True:
#     guess = int(input("guess the number: "))
#     if guess <x:
#         print ("UP")
#     elif guess >x:
#         print ("DOWN")
#     else:
#         print ("CORRECT")
#         break

# import random
#
# x = random.randint(1, 100)
# count = 10
# while count > 0:
#     guess = int(input("guess the number: "))
#     count = count - 1
#     if guess < x:
#         print("UP")
#     elif guess > x:
#         print("DOWN")
#     else:
#         print("CORRECT")
#         break
#     print("remaining count(s): ", count)
#
# for i in range(10, 0, -1):
#     print("you have", i, "tries remaining")

# DAY 2 logical operators not and or nested if statement for while loops for-limited while - unlimited (condition) break continue
# 0~4
# range(n), 0 to n-1
#for i in range(0,4): #0~3
# print(i)
# 0 to 100, only even number
# for i in range(0,100,3):
#     print (i)

# x = 8
# for i in range (2,x) :
#     if x % i == 0:
#         print("False")
#         break
#     else:
#         print("True")
#         break
# x = 8
# is_prime = True
# for i in range (2,x) :
#     if x % i == 0:
#         is_prime = False
#         break
# print(is_prime)

# x=1234
# count=0
# while x>0:
#     x=x//10
#     count = count = 1
# print(count)
#
# x=5992
# y=0
# s=0
# while x>0:
#     y = x%10
#     s += y
#     x = x//10
# print (s)
#
# simple version:
#
# x=5992
# s=0
# while x>0:
#     s += x%10
#     x = x // 10
# print(s)

# Nested Loops

# for i in range(2,10):
#     s = 0
#     for j in range(i,i*10,i):
#         s=s+1
#         print(i,"x", s, "=", j)
#
# for i in range(2,10):
#     for j in range (1,10):
#         print(f"{i} X {j} = {i*j}")

# s=""
# for i in range (1,6):
#         s = s + "*"
#         print(s)
#
# for i in range (1,6):
#         for j in range (i):
#                 print("x", end="")
#         print()

#function
#create function
#def function_name(parameters):
# def example(a):
#         return 2*a
#
# b = example(10)
# print(b)

# def isPrime(n):
#         for i in range(2,n):
#                 if n % i == 0:
#                         return False
#         return True

# create a function that find n-th prime number
# def nthPrime(n):
#         count = 0 # count is for counting the number of prime numbers
#         number = 2
#         while count < n:
#                 if isPrime(number) == True:
#                         count+=1
#                 number +=1
#         return number - 1
# print(nthPrime(3))
#
# x=4782
# Write a program that find the largest digit in integer x
# 4782 = 8
# 8898 = 9
# 1234 = 4
# If you get the answer, then try to convert your program to function

# string is one of the types of variable
# mystr[index], index indicates the location of element(letter)
# index starts from 0
# mystr = "Hello, World"
# print(mystr[0]) # H
# print(mystr[5]) # ,
# print(mystr[6]) #
# print(len(mystr)) # len returns the number of characters
#
# str1 = "abc"
# str2 = "def"
# print (str1+str2) # You can concatenate two string using '+'

# String Slicing --> you can extract a substring from a string using slicing
# str[starts:end] --> starts to end -1
# subs = mystr[0:5]
# print (subs) #Hello
# # String Method --> String method is used to manipulate and work with strings
# mystr2 = "Hello, my name is Scott"
#  # str.lower() --> convert your string to all upper cases
# lower_mystr2 = mystr2.lower()
# # str.upper() --> convert your string to all upper cases
# upper_mystr2 = mystr2.upper()
# print(upper_mystr2)
# # str.strip() --> removes leading and trailing whitespaces from the string
# mystr3= "Hello, World!"
# print(len(mystr3)) #15
# mystr3 = mystr3.strip()
# print(len(mystr3)) #13
# print (mystr3)
# name = input("Enter your name: ").strip()
# # name = name.strip()
# if name == "Scott":
#         print("Your name is Scott")
# else:
#         print("Your name is not Scott")
# #splits --> splits the string into substrings based on a delimiter
#
# str1= "Apple Carrot Melon"
# a,b, c = str1.split() # splits the string by whitespace
# print(a)
# print(b)
# print(c)
#
# time = "11:30"
# hour,minute = time.split (":")
# print(hour)
# print(minute)
# #replace --> you can replace some substring into another substring
# str123 = "Hello, World!"
# str123 = str123.replace("Hello" , "Bye") #replace "Hello" to "Bye"
# print(str123)
# # Case sensitivity
# # "Hello" and "hello" are different words
# print("Hello" == "hello") #False
#
# # Program that prompts the use for an mathematics expression and then calculates and outputs
# # the result
# # Assuming there are spaces between numbers and operators
# # 5 + 5 --> 10
# 14 - 7 --> 7
# expression = input("Enter an expressions: ")
# x,y,z = expression.split()
# if y == "+":
#         print(int(x) + int(z))
# elif y == "-":
#         print(int(x) - int(z))
# elif y == "x":
#         print(int(x) x int(z))
# elif y == "/":
#         print(int(x) / int(z))
# elif y == "%":
#         print(int(x) % int(z))

# Variables
# Snake Case
student_name = "Scott"
# Camel Case
studentName = "Scott"
# Write a program that get the name of a variable in Camel case and outputs the name in snake case
#
# name = "Scott"
# variable_name = input("Enter a variable name: ")
#
# for i in name:
# print(name[i].isupper())
#         if name[i].isupper() == False:
#                continue
#         elif name[i].isupper() == True:
#                variable_name.replace (i, "_")

# name = "scottName"
# for i in name:
#         if i.isupper() == True:
#                 name = name.replace(i, "_"+i.lower())
# print ("SNAKE",name)

# message = input("What is your message?: ").strip()
#
# if message [0] == "b" or message [0] == "B" and message[1] == "y" and message[2] == "e":
#         print("$0")
#         break
# if message[0] == "b" or message[0] == "B":
#         print("$50")
# else:
#         print("$200")
#
# variable = input("Enter a message: ").lower().strip()
# if variable [0:3] == "bye":
#         print("$0")
# elif  variable [0] == "b":
#         print("$50")
# else:
#         print("$200")
# Write a program to get the time from the user. 7:40
# if the time is between 7:00-8:00, then print breakfast
# if the time is between 12:00-14:00, then print lunch
# if the time is between 17:00-19:00, then print dinner
# you need to split into hours and minutes
# then, you need to convert the time into decimal number
# 7:30 --> 7.5
# 7:20 -->
# time = input("Enter the time: ")
# if time[0] == "7":
#         print ("breakfast")
# if time[0:2] == "12" or time[0:2] == "13":
#         print ("lunch")
# if time[0:2] == "17" or time[0:2] == "18":
#         print ("dinner")
# else:
#         print ("It's not a meal time.")
#
# time = input("Enter the time in 24-hour format")
# hour, minute = time.split(":")
# converted_time = int(hour) + int(minute)/60
# if 7<= converted_time <=8:
#         print ("breakfast")
# elif 12<= converted_time <=14:
#         print ("lunch")
# elif 17 <= converted_time <=19:
#         print ("dinner")
# else:
#         print ("Not a meal time")

# message = input("Enter a text: ").lower().strip()
#
# for i in message:
#         if (i) == ("a"):
#                 message=message.replace(i,"")
#         if (i) == ("e"):
#                 message = message.replace(i, "")
#         if (i) == ("i"):
#                 message = message.replace(i, "")
#         if (i) == ("o"):
#                 message = message.replace(i, "")
#         if (i) == ("u"):
#                 message = message.replace(i, "")
# print (message)

# plate = input("Enter a vehicle plate: ")
#
# isValid=True
# for i in plate:
#         if plate.isalnum() == False:
#                 isValid = False
#         if plate[0:2].isalpha() == False:
#                 isValid = False
#         if len(plate) > 6 or len(plate) < 2:
#                 isValid = False
# j = 0
# for i in range(0,len(plate)):
#         if plate[i].isdigit() == True:
#                 if plate[i] == '0':
#                         isValid = False
#                         break
#                 else:
#                         break
#         j+=1
# for c in range(j,len(plate)):
#         if plate[c].isalpha() == True:
#                 isValid = False
# print(isValid)
#
# n=5
# for i in range(1,n+1):
#         for j in range(n-1): # range 0 to n-2
#                 print (" ", end=" ")
#         for k in range(i,0,-1):
#                 print (k, end=" ")
#         for m in range(2, i+1):
#                 print(m, end=" ")
# strings are really delicate data type to work with.

# message = input("Enter a message: ")
# for i in range(len(message)):
#      print(message[-i-1])
#
# s= "abcdefghijklmnop"
#
# print (s[3:len(s)-3:2])

# def firstlast (s):
#      print(s[0]+s[-1])
#
# firstlast ("asdfasdfjlk")
#
# #string is immutable 바꿀수 없음 print(s[d]) s[d] = 'z' print(s[d]) 이거 안됨
#
# s = "d"

# Getting a string made of the first 2 and the last 2 characters of a given string.
# If the string is less than 2, return the empty string instead.
#
# if (len(s) <2)
#      print ("")
# else:
#      print (s[0:2] + s[-2] + s[-1])
#      또는 (s[0:2] + s[-2:])

# Get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself.

# s = "restart"
# char = s[0]
# s = s.replace(char, '$')
# answer = char + s[1:]
# print (answer)
#
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
#
# sample input : abc
# sample output 1 : abcing
# sample input : string
# sample output 2 : stringly

# s = "studying"
# if len(s) < 3:
#      print(s)
# else:
#      if s[-3:] == "ing":
#           s += "ly"
#      else:
#           s+="ing"
# print(s)
#
# s = input("Enter your SSN: ")
#
# print(s[-7])
#
# if s[-7:].startswith('1') or s[-7:].startswith('2'):
#     print ("Born before 2000")
# else:
#     print ("Born after 2000")
#
# if s[-7].startswith ('1') or s[-7].startswith ('3'):
#     print ("Male")
# else:
#     print ("Female")
#

# s = 'abcd'
# print (s.upper())
#
# capitalize(): will only capitalize the first character
#
# isalpha() : tests whether the string is only alphabets
#
# isdigit(_ : tests whether the string is only numbers

# s = input("Enter a palindrome: ")
#
# for i in range(0, int(len(s)/2)):
#     if (s[i] != s[len(s)-1-i]):
#         print ("It is not a palindrome.")
#         break
#     else:
#         print ("It is a palindrome.")

# str = "abcdefg"
# new_str = ""
#
# i=0
# while i < len(str):
#     if (i%2 == 1):
#         i+=1
#         continue
#     new_s += str[i]
#     i+=1
# print (new_str)

# str = "abcdefg"
# n=1
#
# for i in str:
#     if len(str) % 4 == 0:
#         print (str[::-1])
#         break
#     else:
#         print ("x")
#         break

s = "Hi My name is David"
# count = 0
# for i in s:
#     if i == " " :
#         count += 1
# print (count)

# if s == " ":
#     print (0)
# elif s[0] == " ":
#     if s [len(s)-1] == " ":
#         print(s.count(" ")-1)
#     else:
#         print(s.count(" "))
# elif s[len(s)-1] == " ":
#     print (s.count(" "))
# else:
#     print (s.count(" ")+1)
#
# a = 1

# a = [1,2,3,4]
#
# for i in range(len(a)):
#     print(a[i])

# a = [1,2,3,4,5,6,7,8]
# max(a)
# min(a)

# a = [12,3,6,1234,39,59]
#
# sum_i = 0
# for i in range (len(a)):
#     sum_i += a[i]
#
# print (sum_i/len(a))
#
# print(sum(a)/len(a))

# a = [12,6,8]
# max_a = max(a)
# min_a = min(a)
# middle = 0
# for i in a:
#     if i!=max_a and i!=min_a:
#         middle = i
# if min_a+middle > max_a:
#     print ("legal triangle")
# else:
#     print ("not legal")
#
# if a[0] + a[1] > a[2] and a[1] + a[2] > a[0] and a[1] + a[2] > a[0]:
#     print( "legal triangle")
# else:
#     print ("No")

# a = [1,2,[3,4,[5,6],7], 8]
#
# print (a[2])
# print (a[2][2][0])
#
# a = [1, 2, [3, 4, [5, 6, 7, 8, 9, 10], 11], 12]
# print (a[2][2][1:4])
#
# a= [1,2,3]
# b=[4,5,6]
# c=[7,8,9]
# d = a+b+c
# print(d)
#
# e = [a,b,c]
# print(d[0])
# print(e[0])
#
# a = [1,2,3]
# for i in range (len(a)):
#     a[i] = a[i]*100
# print (a)

# a=[1,2,3,4]
# print(a)
# del a[1]
# print(a)
# a.append(5)
# print(a)
#
# a=[]
# for i in range(1,101):
#     a.append(i)
# print(a)
# 리스트에서 특정 자리에 숫자 더하려면 insert(a,b)
# a = the index where you want to insert b = what you wnat to insert

# a = [1,2,4]
# a.insert (2,3)
# print (a)
# a.insert(2,[100,101])
# print(a)
# a=[1,2,1234,572378,3,9,1324,123]
# print(a)
# a.sort()
# print(a)
# print(a.reverse())

# google kickstart, leetcode, codeforces, 백준 boj 올림피아드 지금 entry level 에서 algorithmic problem solving
# PS (problem solving) PS coding code forces 너무 어렵 백준 단게별로 풀어보기 leetcode -> easy problems

# a = [1,2,3,4,5,6,7]
# 1: remove function --> remove(i) : removes the element at ith index
# 2:
lst = []

# for i in range(len(a)):
#     if i != 0 and i!=4 and i!= 5:
#        lst.append(a[i])
#
# list1 = [1,2,3,4,5,6]
# list2 = [6,7,8,9,10,11]
#
# duplicate = False
# for x in list1: #for i in range(len(list1)) difference
#     for y in list2:
#         if x == y:
#             print ("Duplicates!")
# a = [1,2,3,4,5]
# a.reverse()
# print (a)
#
# reversed_list = []
# for i in range(len(a)):
#     reversed_list.append(a(-i)) #we don't have to do this! ;python provides us with a fuction for that
#
# delete = index number로 지우기. Remove = 그놈 지우기
#
# a = [1,2,3,4,5]
# del a[3]
# print(a)
#
# a.remove(4)
# print(a)

# l = [1,2,3,9,4,5,9,2,9,0]
#
# # if (9 not in l):
# #     print ("We can't find it.")
# # elif (9 in l):
# #     print (l.index(9))
#
# for i in range(len(l)):
#     if l[i] == 9:
#         print (i)
#
# a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(a)
# print(a.pop())
# print(a)

# tuple - also a way to store multiple data in a single variable

# a = (1,2,3,4,5,6,7)
# print (type(a)) = tuple
# tuple = immutable 튜플은 안바뀜 리스트는 바뀜 바꾸기 싫은거 쓰고 싶으면 tuple

l = [3,5,6,2,234,5939,122]
# l.sort()
# print(l[-2])
# print(int(len(l)/2))

# a = l.sort()
# if l == a:
#     print ("It is sorted")
# else:
#     print ("It is not sorted") 리스트는 == 쓰지말자 나중에 복잡

# program that outputs the maximum value in a list of integers.

# import random
# empty = []
# for i in range(15):
#     empty.append(random.randint(1,100))
# print (empty)

# maxi = -9999
# for i in empty:
#     if i>maxi:
#         maxi = i
# print(maxi)
# print(max(emptu))

# a = [1,2,2,2,3,3,5,6,7,7]
# anotherlist = []
#
# for value in a:
#     if value not in anotherlist:
#         anotherlist.append(value)
# print(anotherlist)

# Dictionary
# Python version of Hash map
# Hash Map

# access the value with key

# sean = {'name': 'Sean', 'Birthday': '1999-10-25', 'gender': 'male', 'height': '193', 'shoe size': '7.5'}
#
# print (sean['name']) #이러면 sean 이 프린트됨
#sean['weight'] = "68kg"
# del sean['height']

# a=[1,2,3,4,5]
# d={1:1, 2:2, 3:3, 4:4}

# a[1] # a is a list [1] ==> index 1
# d[1] # d is a dictionary [1] ==> key 1
#
# a ={(1,2,3):"a"} #We can use tuple as a key
# a ={[1.2.3]:"a"} #But we can NOT use list as a key

# sean.keys()
#
# type(1)
# type(sean.keys()) #special niche type
# type(list(sean.keys()))
# sean.items()
# sean.values()
# sea['birthday'] = sean.get('birthday')
# weight 없는데 sean['weight'] 하면 에러나고 sean.get('weight') 하면 none 나옴
# sean.get('weight', "Not here") 하면 낫히어 나옴
# 'weight' in sean 하면 false 나오고 'height' in sean 하면 true 나옴

# a = ['Hi', 'My', 'Name', 'Is']
# result = {}
# for i in a:
#     result [i] = len(i)
#
# print(result)
# d = {1: "one", 2:"Two", 3: "Three", 4: "Four"}
#
# newdict = {}
# for i in d.keys():
#     newdict[d[i]] = i
# print(newdict)

# a = [1,2,2,3,2,3,1,5,4]
# # result = {1:[-, 6], 2: [1,2,4], 3:[3,5], 4:[8], 5:[7]}
# result = {}
# for i in range (len(a)):
#     if a[i] in result.keys():
#         result [a[i]].append(i)
#     else:
#         result[a[i]] = [i]
# print (result)
#
# s = "Hello"
# newdict = {}
# for char in a:
#     if char in newdict:
#         pass
#     else:
#         newdict [char] = s.count(char)
# print(newdict)

# import random
# sample = []
# for i in range(20):
#     sample.append(random.randint(1,100))
#
# div = []
# for i in sample:
#     div.append(i%29)
#
# unique = []
# for i in div:
#     if i not in unique:
#         unique.append(i)
#
# print (len(unique))

# d1 = {'a':1, 'b':2, 'c':3,}
# d2 = {'c':3, 'd':4, 'a':1}
#
# answer = {}
# for a in d1.keys():
#     if a in d2:
#         if d1[a] == d2[a]:
#             answer[a] = d1[a]
# print (answer)

# input = [['A', 'B', 'C', 'D', 'E'],
# ['a', 'b', 'c', 'd', 'e'],
# ['0', '1', '2', '3', '4'],
# ['F', 'G', 'H', 'I', 'J'],
# ['f', 'g', 'h', 'i', 'j']
#          ]
# s = ""
# for i in range (5):
#     for j in range (5):
#         s+=input[j][i]
# print (s)

# Write a python program that sums all the elements in a 2D list
# input_2d_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# series = 0
# for i in range(len(input_2d_list)):
#     for j in range(len(input_2d_list[0])):
#         series+=input_2d_list[i][j]
#
# summ = sum(element for row in input_2d_list for element in row)
# print (summ)

#Write a python program that adds the diagonal elements of a 2D list. Assume that the list is always square(nxn).
# input_2d_list = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
#
# n = len(input_2d_list)
#
# diag = 0
# for i in range(n):
#     diag+= input_2d_list[i][i]
#
# print (diag)

# s1 = "beard"
# s2 = "bread"
# d1 = {}
# d2 = {}
# for c in s1:
#     d1[c] = s1.count(c)
# for c in s2:
#     d2[c] = s2.count(c)

# def name_of_the_function(input_parameter):
    #funciton body

# def addOne(x):
#     return x+1
#
# a=5
# b-addOne(a)
#
# A function may or may not have a parameter. Also, a function may or may not have a return statement.
#
# z = 30
# def b() :
#     global z
#     z+=1
#
# b()
# print (z)
#
# x = 5
# def out():
#     x=10
#     def inner():
#         x = 20
#         print(x)
#     inner()
#     print(x)
#
# print(x)
# out()
#
# x = 5
# def out():
#     x=10
#     inner()
#     print(X)
# def inner ():
#     x = 20
#     print(x)
#
# print (x)
# out()
# print (x)

# z = 30 #global variable
# def h():
#     global z
#     z = z*10
# def g():
#     z = 50 #local variable
#     h()
#     print(z)
#
# g()
# print(z)

# a = 15
# def outer():
#     a = 10
#     def inner():
#         a = 20
#         def reallyinner():
#             global a
#             a = 30
#         print (a)
#     inner()
#     print(a)
#
# outer()
# print(a)
#
# print (1)

# LEGB Rule
# L: Local
# E: Enclosed Function Locals
# G: Global
# B: Built-in functions
#
# L->E->G->B
#
# a = [1,2,3,4]
# sum(a)
#
# sum = 0
# for i ina:
#     sum+=i
#
# del sum
#
# print(sum(a))

# def square(x):
#     return x**2
#
# print(square(2))
#
# a = lambda x : x*x
# print(a(2))

# (lambda x:x**2)(4)
#
# c = (lambda: print("Hi"))
# c()

# lst = [8,2,3,75,5,6,7]
# lst2 = []
# def sq(lst):
#     for i in lst:
#         i = i*i
#         lst2.append(i)
# sq(lst)
# print(lst2)

# map(function,list)

# print(list(map(lambda x: x**2, [1,2,3,4,5,6,7])))
#
# list(filter(lambda x : x%2 == 0,[1,2,3,4,5,6,7]))
#
# list(filter(lambda x : x<3,[1,2,3,4,5,6,7]))

# import functools
# a = [1,2,3,4,5,6,7,8]
# cumulsum = functools.reduce(lambda x,y: x+y, a)
#
# print(cumulsum)

# factorial = lambda n: functools.reduce(lambda x,y : x*y, range(1,n+1))

# d = int(input())
# try:
#     a = 99/d
#     print(a)
# except:
#     print("Error! But we did not crash")
#
# d = int(input())
# try:
#     a = 99/d
#     print(a)
# except:
#     print("Error! But we did not crash")
#
# a = [1,2,3,4,5]
# index = int(input("Input: "))
# try:
#     print(a(index))
# except:
#     print("Index out of range")
# else:
#     print("Program run successful")
# finally:
#     print("Restart?")

# Indentation error
# Logical error
# Zero-division
# Wrong parameter
# Name Error
# Syntax Error

# list_of_lists = [[1,2,3], [4,5,6,7,8], [9], [10, 11, 12, 13, 14, 15]]
#
# new_list = []
#
# for i in list_of_lists:
#     if len(i)>=5:
#         new_list.append(i)
#
# print(new_list)
#
# filtered_list = list(filter(lambda lst:len(1st)>=5, list_of_lists))
#
# print(filtered_list)
#
# Get the average of the list using reduce() and lambda
#
# import functools
#
# nums = [10,20,30,40,50,60]
#
# average = functools.reduce(lambda x,y: x+y, nums)/len(nums)
#
# print(average)
#
# from functools import reduce
#
# nums = [10,20,30,40,50,60]
# average = functools.reduce(lambda x,y: x+y, nums)/len(nums)
# print(average)

# Take a list of lists and filter out the lists that have lengths less than n.

# list_of_lists = [[1,2,3], [4,5,6,7,8], [9], [10, 11, 12, 13, 14, 15]]
#
# outer = lambda n : list(filter(lambda lst: len(lst)>=n, list_of_lists))
#
# n = int(input("N: "))
#
# filtered = outer(n)
#
# print(filtered)
#
# def outer(n):
#     return list(filter(lambda lst: len(lst)>=n, list_of_lists))
#
# n = int(input("N :"))
#
# filtered = outer(n)
#
# print (filtered)
#
# n = 20
#
# print("A") if n<15 else print("B")

# from functools import reduce
# nums = [10, 2, 9, 15, 37, 8, 26]
#
# max_val = reduce(lambda x,y: x if x>y else y, nums)
# print (max_val)
#
# 11 = [1,2,3,4,5,6,7]
# 12 = [6,7,8,9,10]
#
# common = list(filter(lambda x: x in 11, 12))
#
# print (common)
#
# fibonacci

# from functools import reduce
#
# fibonacci = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0,1])
#
# print (fibonacci(10))

# f = open('링크', 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()
#
# f = open('링크', 'r')
# lines = f.readlines()
# print(lines)
# for line in lines:
#     line - line.strip()
#     print(line)
# f.close()

#List Comprehension

# d = [i for i in range(15) if i%2 == 0]
#
# table = [i*j for i in range(1,10) for j in range(1,10)]
#
# #zip
#
# capital = ("Seoul", "DC", "Tokyo")
# country = ("Korea", "USA", "Japan")
# z = zip(country, capital)
#
# print(list(z))
#
# for a, b in zip(capital, country):
#     print ("I live in ", a, "which is the capital of", b)
#
# d = dict(zip(country, capital))

# lst = ["A", "B", "C", "D"]
#
# enum = enmerate(lst)
#
# print(list(enum))
#
# for i in enumerate(lst, 3):
#     print(i)

# RECURSION

# def hello():
#     print("Hello, world")
#     hello ()
#
# hello()
# 이러면 무한대로 냐온다

# def hello(count):
#     if count == 0:
#         return
#     print("Hello World", count)
#     count-=1
#     hello(count)
#
# hello(5)
# first = 1
# second = 1
# def fibonacci(n):
#     if n == 0 or n==1: #base case
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2) #recursion
#
# print (fibonacci(6))

# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)
# n=12345
# sum=0
# for c in str(n):
#     sum+=int(c)
# print(sum)
# def sod(n):
#     if sod(n) == 0:
#         return 1
#     return n+sod(n%10 // 10)
# print(sod(12345)) 이건 안됨
#
# def digit_sum(x):
#     if x ==0:
#         return 0
#     return x%10 + digit_sum(x//10)
#
# def digit_sum(x):
#     if x < 10:
#         return x
#     return x % 10 + digit_sum(x // 10)

#Object Oriented Programming

# Abstraction, Encapsulation, Polymorphism, Inheritance

#4 pillars of OOPs

# Class

# Object --> #attribute, behaviour
#OOP -> Interaction between objects

# class Car():
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#     def get_brand(self):
#         return self.brand
#     def get_color(self):
#         return self.color
#     def __str__(self):
#         return "My car is "+self.color+" "+self.brand
#
# # Getter vs Setter
# class Human():
#     def __init__(self, name, age, nationality): #constructor
#         self.name = name
#         self.age = age
#         self.nationality = nationality
#         print(self.name, "is born!")
#
#     def __add__(self, other):
#         print(self.name,"and",other.name,"are getting married")
#
#     def __str__(self):
#         s = "Hello, I am "+ self.name
#         s1 = "I am "+str(self.age)+" years old"
#         s2 = "I am " + self.nationality
#         return s+"\n"+s1+"\n"+s2
#
#     def buy_car(self, brand, color):
#         newCar = Car(brand, color)
#         print(self.name, "buys a car")
#         print(newCar)
#
#     def sing(self):
#         print(self.name, "sings\nLALALALALA~~~")
#     def eat(self):
#         print(self.name, "eats\nchump")
#     def get_name(self): #getter #Method
#         return self.name
#     def get_age(self): #getter
#         return self.age
#     def get_natiuonality(self):
#         return self.nationality
#     def set_name(self, name):
#         self.name = name
#     def set_age(self, age):
#         self.age = age
#     def set_nationality(selfself, nationality):
#         self.nationality = nationality
# # def __del__(self): #destructor
#     #     print(self.name, "is killed :(")
#
# david = Human("David", 16, "Korean")
# mat = Human("Matthew", 16, "K-American")
#
# print(david)
#
# david = Human("David", 16, "Korean")
# david.buy_car("Porsche", "Blue")
#
# mat = Human("Matthew", 16, "K-American")
# mat.buy_car("Porsche", "Grey")
#
# class Korean ():
#     legal_drinking_age = 20
#     def __init__(self, name, age, SSN):
#         self.name = name
#         self.__age = age
#         self.__SSN = SSN
#     def able_to_drink(self):
#         return self.__age>= Korean.legal_drinking_age
#     def authenticate(self, id):
#         return self.__SSN == id
#     def get_age(self): #__를 해놓으면 get을 하는게 유일한 방법
#         return self.__age
#     def set_age(self, age): #__를 해놓으면 set을 하는게 유일한 방법
#         self.__age = age
#
# sean = Korean("승호", 24, 123456)
# david = Korean("정욱", 16, 324324)
# mat = Korean("윤호", 16, 342523)
#
# print(sean.able_to_drink())
# print(david.able_to_drink())
#
# print(mat.get_age()) #only way to get age
# mat.set_age(18)
# print(mat.get_age())
#
# david.age = 35
# print(david.able_to_drink())
# print(mat.__SSN)

# 1. Define your own object. Dog, Cat, Human, Laptop, 김치찌개,... whatever is fine.
#
# 2. Make a constructor with at least 3 attributes. For instance, a dog may have "name", "breed", "age" as its attributes.
#
# 3. Define a getter method for all the attributes.
#
#     3-1. Use encapsulation for at least one of the attributes.
#
# 4. Define at least one behaviour of the object. For instance, a 김치찌개 may have boil(), which prints "보글보글."
#
# 5. Create at least 2 instances of the object.

# class Athlete():
#     def __init__(self, name, sports, team):
#         self.__name = name
#         self.sports = sports
#         self.team = team
#
#     def set_sports(self, sports):
#         self.sports = sports
#     def get_sports(self):
#         return self.sports
#     def set_team(self, team):
#         self.team = team
#     def get_team(self):
#         return self.team
#     def set_name(self, name):
#         self.__name = name
#     def get_name(self):
#         return self.__name
#     def listens(self):
#         print(self.__name, "listens to the music before game")
#
# David = Athlete("정욱", "basketball", "Nets")
# Messi = Athlete("메시", "soccer", "FCB")
#
# David.listens()
# print(David.get_sports())
# Messi.listens()
#
# #Exceptions: Thins that go wrong within our program (Error)
#
# try:
#     x = int(input("Enter a number"))
# except ValueError: #When we get the ValueError from the code under try
#     print("x is not an integer")
#
# While True:
#     try:
#         age = int(input("Enter your age: "))
#     except ValueError:
#         print("This is not the corect age.")
#         print("Enter Again!")
#     else:
#         print("Your age: ",age)
#         break

#assert to test functions in python
# def example(a,b):
#     return a,b
# assert example(2,3) == 5
# assert example(-10,-2) == -12

# while True:
#     fraction = input("Enter a fraction: ")  # s/k
#
#     X, Y = fraction.split("/")
#     try:
#         X = int(X)
#         Y = int(Y)
#     except ValueError:
#         print("Enter Again!")
#     else:
#         try:
#             X/Y
#         except ZeroDivisionError:
#             print("Enter Again!")
#         percentage = X / Y * 100
#         if percentage <= 1:
#             print ("Empty")
#         elif percentage > 99:
#             print ("Full")
#         elif X>Y:
#             print("Enter Again!")
#         else: print(percentage)
#         break

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sing(self):
#         print("LALALA~~~~")
# class Student(Human):
#     """Sub Class"""
#     def __init__(self, name, age, school):
#         self.name = name
#         self.age = age
#         self.school = school
#
# david = Student("David", 15, "Episcopal")
# print(david.name)
# print(david.age)
# print(david.school)
#
# david.sing()

#스태틱 메또드, 이건 따로 파일 만들어서 하자
# class ABC:
#     def add_instance_method(self, a,b):
#         return a+b
#     @classmethod
#     def add_class_method(cls, a,b):
#         return a+b
#     @staticmethod
#     def add_static_method(a,b):
#         return a+b
#
# #따로 파일을 만들어서 여기다가 import 하는거임
#
# from static_method import ABC
# print(ABC.add_instance_method(None, 1,2))
# print(ABC.add_class_method(3,5))
# print(ABC.add_static_method(3,5)))
#
# a = ABC()

# class Lang:
#     default_language = "English" #class variable
#     def __init__(self):
#         self.show = "Languagee: " + self.default_langauge
#     @classmethod
#     def class_my_lang(cls):
#         return cls():
#     @staticmethod
#     def static_my_lang():
#         return Lang()
#     def print_language(self):
#         print(self.show)
# class KoreanLang(Lang):
#     default_language = "Korean"
#
# from lang import *
#     a = KoreanLang.static_my_lang()
#     b = KoreanLang.class_my_lang()
#
#     print("A(static method): ")
#     a.print_language()
#
#     print("B(clss method): ")
#     b.print_language()

#ABC abstract class

# from abc import *
#
# class StudentBase(metaclass=ABCMeta):
#     @abstractmethod
#     def study(self):
#         pass
#
#     @abstractmethod
#     def go_to_school(self):
#         pass
#
#     @abstractmethod
#     def go_home(self):
#         pass
#
# class Student(StudentBase):
#     def study(self):
#         print("Studying")
#     def go_to_school(self):
#         print("Urghhhh")
#     def go_home(self):
#         print("YEAHHHH")
# class HighschoolStudent(StudentBase)
#     def study(self):
#         print("Studying SAT")
#     def go_to_school(self):
#         print("Urghhhh")
#     def go_home(self):
#         print("YEAHHH")
# class CollegeschoolStudent(StudentBase):
#     def study(self):
#         print("Studying GRE")
#     def go_to_school(self):
#         print("Urghhhh")
#     def go_home(self):
#         print("YEAHHH")
#
#
# a = Student()
# a.study()
# b = CollegeStudent()
# b.study()
# a = [1,2,3,4,5]
# for i in range(len(a)):
#     print(a[i])
# a = [1,2,3,4,5]
# print(type(a))
# a = iter(a)
# print(type(a))
# a.__next__()
# a.__next__()
#
# a = [1,2,3,4,5,6]
#
# a=iter(a)
# while True:
#     try:
#         print(a.__next__())
#     except:
#         break
#
# class OurIterator:
#     def __init__(self, data):
#         self.data = data
#         self.position = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.positaion>=len(self.data):
#             raise StopIteration
#         result = self.data[self.position]
#         self.position +=1
#         return result
# if __name__ == "__main__":
#     i = OurIterator([1,2,3,4,5,6,7])
#     for item in i:
#         print(item)
#for loop 은 별게 아니다 iterator을 이해하면 이런식으로 강제로 뜯어 고칠 수 있다.

# for i in range (1,11):
#     print(i)

# def least_coin(n, coin_list): #Greedy Algorithm 탐욕법
#     coin_list.sort(reverse=True)
#     num_coins = 0
#     index = 0
#
#     while n>0:
#         if coin_list[index] <= n:
#             num_coins += 1
#             n -= coin_list[index]
#         else:
#             index += 1
#         if index >= len(coin_list):
#             break
#         if n==0:
#             return num_coins
# print (137, [1,5,10,25,30,100])

# def lease_coin_DP(n, coin_list):
#     dp = [float('inf')]*(n+1)
#     dp[0] = 0
#     for i in range(1, n+1):
#         for coin in coin_list:
#             if coin<=i:
#                 dp[i] = min(dp[i], dp[i-coin]+1)
#     return dp[n] if dp[n]!= float('inf') else -1

#Create a list that contains 5 of your favorites foods in string
#Create a function called show() that prints out all the foods from that list
#Display foods on your screen

# a = ["kimchi","pasta","rice"]
# def show():
#     for foods in a:
#         print(foods)
# show()

from tkinter import *
import random

#version 1 (random without options)

# window = Tk() #this code first creates tkinder
#window.mainloop() #actually runs the program

# window = Tk()
# window.geometry("100x40")
# label = Label(window, text = "Hello")
# label.pack
# window.mainloop()

# food_list = ["strawberry", "Rice", "Chicken", "Pasta", "Pizza", "Ramen", "Sushi"]
#
# def pick():
#     food = random.choice(food_list)
#     label["text"] = "You should try" + food + " today!" #Changing the message from the label

## Frontend

# win = Tk()
# win.geometry("350x100")
# label = Label(win, text = "Click button to get menu recommendation!")
# button = Button(win, text= "Get recommendations :)")
#
# label.pack()
# button.pack()

# window.mainloop()
#
# food_list = [["Kimchi fried Rice", "Bibimbap", "Bulgogi", "Fried Chicken"],
#              ["Mapo Tofu", "Malatang", "Dimsum"],
#              ["Pizza", "Pasta", "Salad", "Burgers and fries"],
#              ["Sushi", "Ramen", "Curry", "Gyudon"],
#              ["Pho", "Nashi Goreng"]]
#
# def pick():
#     opt = options.get().lower()
#     food = ""
#     if opt == "Korean":
#         food = random.choice(food_list[0])
#     elif opt == "Chinese":
#         food = random.choice(food_list[1])
#     elif opt == "Western":
#         food = random.choice(food_list[2])
#     elif opt == "Japanese":
#         food = random.choice(food_list[3])
#     elif opt == "Asian":
#         food = random.choice(food_list[4])
#     else:
#         label["text"] = "You might have entered wrong option, please try again!"
#         return
#
#     label["text"] = "You should try " + food + " today!"
#     label2["text"] = "Rate my recommendation! 1~4"
#
# def rate():
#     #.isdigit() -> True / False if the string is number
#     if options2.get().isdight() != True:
#         label2["text"] = "You should put in numbers"
#         return
#     opt = int(options2.get())
#     if opt >= 4:
#         label2["text"] = "Thank you!"
#     elif opt >= 1 and opt < 4:
#         label2["text"] = "I'll try better next time"
#     else:
#         label2["text"] = "That's not a valid rating"
#
# win = Tk()
# win.geometry("350x100")
# label = Label(win, text = "Enter your option for food and click the button.")
# food_opt = Label(win, text = "Options: Korean/ Chinese/ Western/ Japanese/ Asian")
# options = Entry(win)
# button = Button(win, text = "Get recommendations :",command = pick)
# label2 = Label(win, text = "Get recommendations first!")
# options2 = Entry(win)
# button2 = Button(win, text = "Submit", command=rate)
# # rate = rate(win, text = "Rate my recommenmdation! 1~4")
#
# label.pack()
# food_opt.pack()
# options.pack()
# button.pack()
# label2.pack()
# options2.pack()
# button2.pack()
# win.mainloop()
# rate.pack()

#version 3 (random with options, dictionary, add more options to the list)

# import random
# from tkinter import *
#
# ##Backend
#
# food_list = {"korean" : ["Kimchi Fried Rice", "Bibimbap", "Bulgogi"],
#              "chinese" : ["Mapo Tofu", "Malatang", "Dimsum"],
#              "western" : ["Pizza", "Sandwich", "Pasta", "salad"],
#              "japanese" : ["Sushi", "Ramen", "Curry", "Gyudon"],
#              "asian" : ["Pho", "Nashi Goreng"]}
#
# def pick():
#     opt = options.get().lower()
#     #in operator I-> checks if left element is inside the right list
#     if opt in food_list.keys():
#         label["text"] = "You should try " + random.choice(food_list[opt]) + " today!"
#     else:
#         label["text"] = "You might have entered wrong option, please try again!"
#         return
#
# ##Frontend
#
# win = Tk()
# win.geometry("350x100")
# label = Label(win, text = "Enter your option for food and click the button.")
# food_opt = Label(win, text= "Options: Korean/Chinese/Western/japanese/Asian")
# options = Entry(win)
# button = Button(win, text = "Get recommendations :)", command = pick)
#
# label.pack()
# food_opt.pack()
# options.pack()
# button.pack()
#
# win.mainloop()

#Rock Paper Scissor Game

import random
from tkinter import *
#
# ## Backend
#
# options_list = ["rock", "paper", "scissor"]
#
# def pick():
#     computer_option = random.choice(options_list)
#     user_option = options.get().lower()
#
#     if user_option == "rock" and computer_option == "scissor":
#         label["text"] = "You won! The winning choice was rock!"
#     elif user_option == "rock" and computer_option == "paper":
#         label["text"] = "You lost! The winning choice was scissor!"
#     elif user_option == "scissor" and computer_option == "paper":
#         label["text"] = "You won! The winning choice was scissor!"
#     elif user_option == "scissor" and computer_option == "rock":
#         label["text"] = "You lost! The winning choice was paper!"
#     elif user_option == "paper" and computer_option == "rock":
#         label["text"] = "You won! The winning choice was paper!"
#     elif user_option == "paper" and computer_option == "scissor":
#         label["text"] = "You lost! The winning choice was rock!"
#     elif user_option == computer_option:
#         label["text"] = "It is tied!"
#     else:
#         label["text"] = "You might have entered wrong option, please try again!"
#         return
#
#
# ## Frontend
#
# win = Tk()
# win.geometry("350x100")
# label = Label(win, text = "Let's play Rock Paper Scissor!")
# rps_options = Label(win, text = "Options: Rock/Paper/Scissor")
# options = Entry(win)
# button = Button(win, text = "Play Game :)", command = pick)
#
# label.pack()
# rps_options.pack()
# options.pack()
# button.pack()
#
# win.mainloop()

#backend
# drink_dict = {(1, "Coke"): 2000, (2,"Sprite") : 2000, (3,"Cafe Americano") : 3000, (4,"Water") : 1000, (5,"Orange Juice") : 2500}
# balance = 0
#
# def purchase():
#     global balance
#     choice = int(opt.get())
#     for tuple in drink_dict.keys():
#         if choice in tuple:
#             choice = tuple
#             break
#         else:
#             continue
#     else:
#         lbl["text"] = "Wrong option!"
#         return
#
#     if balance >= drink_dict[choice]: #Comparing the balance with the price of that item
#         balance -= drink_dict[choice]
#         lbl["text"] = "Balance: " + str(balance)
# def update():
#     global balance #global keyword is used to use variable outside our function
#     display_text = "Things you can buy. \n\n"
#
#     #.keys() --> only pick keys from dictionary
#     #.values() -> only pick values from dictionary
#     #.items() -> pick keys and values together from dictionary
#     for keys, values in drink_dict.items():
#         display_text += str(keys[0]) + ". " + keys[1] + ": " + str(values) + "\n"
#     menu["text"] = display_text
#
#     select["text"] = "options"
#     balance += int(opt.get()) #amount that user put in
#
#     btn_buy["command"] = purchase #re-connect frotend button to different function
#
#     lbl["txt"] = "Balance: " + str(balance)
#
# #Frontend
#
# win = Tk()
# win.geometry("400x300")
# menu = Label(win, text = "Click below button to insert money and display menu")
# select = Label(win, text = "Insert Money")
# opt = Entry(win)
# lbl = Label(win, text ="")
# btn_buy = Button(win, text = "buy", command = update)
#
#
# menu.pack()
# select.pack()
# opt.pack()
# lbl.pack()
# btn_buy.pack()
#
# win.mainloop()

#Homework
#1. Improve backend part, show up "Not enough balance" if our balance is lower than the item price
#2. Improve backend part, taek care of the error if user put in "Text" and show new message that says
# "only numbers are accepted"

# win = Tk()
# win.geometry("300x200")
#
# score = 0
# answer = random.randint(1,20)
#
# entry = Entry(win)
# btn = Button(win, text = "Start Game", command=start)
# inst = Label(win, text = "") #Instruction
# lbl = Label(win, text = "Number of Guesses = 0")
#
# entry.pack()
# btn.pack()
# inst.pack()
# lbl.pack()
#
# win.mainloop()
#
# def start():
#     #button text should change to "submit"
#     btn["text"] = "submit" #["text"] will change the displayed message
#     btn["command"] = game #["command"] will connect button to different function
#     #the empty label we created, should now have a new text "Guess the number"
#     inst["text"] = "Guess the number"
#
# def game():
#     guess = int(entry.get()) #.get() will be able to save the value from the user (this will be String type in the beginning)
#     global score #global is used to get the variable we created outside of our function
#     score += 1
#     if answer > guess: #Condition where our answer is bigger than players guess
#         #Display "UP" in our instruction
#         inst["text"] = "UP"
#         lbl["text"] = "Number of Guesses = " + str(score)
#     elif answer < guess:  # Condition where our answer is lower than players guess
#         # Display "DOWN" in our instruction
#         inst["text"] = "DOWN"
#         lbl["text"] = "Number of Guesses = " + str(score)
#     else:  # Condition where player's choice is equal to the answer
#         # Display "You got it correct!" in our instruction
#         inst["text"] = "You got it Correct!"
#         lbl["text"] = "Number of Guesses = " + str(score)
#         btn["text"] = "Finish Game"
#         btn["command"] = repeat
# def repeat():
#     btn["text"] = "submit"
#     inst["text"] = "Do you wanna repeat?"
#     lbl["text"] = "Y/N"
#
# def go():
#     if entry.get() == "Y":
#         inst["text"] = "Guess the number"
#         lbl["text"] = "Number of Guesses = 0"
#         answer = random.randint(1, 5)
#         score = 0
#         btn["command"] = game
#         inst["text"] = "Guess the number"
#         lbl["text"] = "Number of Guesses = 0"
#     else:
#         win.destroy() #terminate entire program

    #If the user's choice is Y
    #change the text of "inst" to "Guess the number"
    #change the text of "lbl" to "Number of Guesses = 0"
    #Hint:
    #To get user's input, use get() method from the variable "entry"

for row in range (0,4):
    for col in range(0,6):
        print("*", end ="") #printing 6 stars on a single line
    print("") #printing new line
for row in range (4,6):
    for col in range(0,6):
        print("$", end ="")
    print("")

import random
from tkinter import *
#
# lst1 = [1,2,3,4] #list of integers
# lst2 = ["string1", "string2", "string3"] #list of string
# lst3 = [False, False, True] =
#
# # for numbers in lst1:
# # print(numbers)
#
# for index in range(0,4):
#     print(lst1(index))

# 2D list

lst_2D = [[1,2,3], [4,5,6]]

#3D list

lst_3D = [[[1,2,3]]]

# print(lst_2D[0]) #[1,2,3]
# print(lst_2D[0][1]) #2

#print #3 from 3D list
# print(lst_3D[0][0][2])
#
# for lst in lst_2D:
#      print(lst)
#      for numbers in lst:
#          print(numbers)

# sum = 0
# lst = [1,2,3,4]
#
# for numbers in lst:
#     sum += number
#
# print(sum)

#Homework #1

# lst_2D = [[1,2,3], [4,5,6]]
#you need to print out sum of all the elements from lst_2D
#output : 21

#empty shape
# shape = [[0,0,0],
#          [0,1,0],
#          [1,1,1]]
#
# for row in range (0,3):
#     for col in range (0,3):
#         if shape[row][col] == 1:
#             print(row, col)
#
# for our tetris game, we will use list of booleans to represent tetris blocks
#     shape = [[0,0,0],
#              [0,1,0],
#              [1,1,1]]
#0 represents False
#1 represnts true

# shape = [[False,False,False],
#         [False,True,False],
#         [True,True,True]]

#Homework 2

#Create all the shapes with boolean 2D_list

# shapeA = [[False, False, False, False],
#          [False, False, False, False],
#          [True, True, True, True]]
#
# shapeB = [[False, False, False],
#           [True, False, False],
#           [True, True, True]]
#
# shapeC = [[False, False, False],
#           [False, False, True],
#           [True, True, True]]
#
# shapeD = [[False,False],
#            [True,True],
#            [True,True]]
#
# shapeE = [[False, False, False],
#           [False, True, True],
#           [True, True, False]]
#
# shapeF = [[False, False, False],
#           [False, True, False],
#           [True, True, True]]
#
# shapeG = [[False, False, False],
#           [True, True, False],
#           [False, True, True]]
# #Shape A
# #Shape B
# #Shape C
# #Shape D
# #Shape E
# #Shape F
# #Shape G
#
# #Homework #3
# #Create a function called "make_block" that takes in alphabet,
# #return the shape that is equal to that alphabet
#
# def make_block():
#

#def make_block(alphabet):
#

#print(make_block("A"))

import random
from tkinter import *

# lst1 = [1,2,3,4] #list of inegers
# lst2 = ["string1", "string2", "string3"] #list of string
# lst3 = [False, False, True] #list of boolean

# for numbers in lst1:
#     print(numbers)

# for index in range(0,len(lst1)):
#     print(lst1[index])

# len() method will return number of elements from a list


# 2D list
# lst_2D = [[1,2,3], [4,5,6]]

# 3D list
# lst_3D = [[[1,2,3]]]

# print(lst_2D[0]) #[1,2,3]
# print(lst_2D[0][1]) #2

# print #3 from 3D list
# print(lst_3D[0][0][2])

# Nested For Loop
# for lst in lst_2D:
#     print(lst)
#     for numbers in lst:
#         print(numbers)


# In-Class Assignment
# print out the sum of all the elements from the list
# lst = [1,2,3,4]

# output
# 10

# sum()
# Hint
# Make a variable that can add numbers

# sum = 0
# for number in lst:
#     sum += number

# print(sum)

# Homework #1
# lst_2D = [[1,2,3], [4,5,6]]
# You need to print out sum of all the elements from lst_2D
# output : 21

# sum = 0

# for lst in lst_2D:
#     print(lst) # [1,2,3] (done)
#                # [4,5,6]
#     for numbers in lst:
#         sum += numbers
# 1. sum will now be 6 (1 + 2 + 3)
# 2. sum will now be 21 (6 + 4 + 5 + 6)

# print(sum)


# empty shape
# shape = [[0,0,0],
#          [0,1,0],
#          [1,1,1]]

# for row in range(0,3):
#     for col in range(0,3):
#         if shape[row][col] == 1:
#             print(row, col)


# For our tetris game, we will use list of booleans to reprsent tetris blocks
# shape = [[0,0,0],
#          [0,1,0],
#          [1,1,1]]

# 0 represents False
# 1 reprsents True

# shape = [[False,False,False],
#          [False,True,False],
#          [True,True,True]]

# Homework #2.
# Create all the shapes with boolean 2D_list

# shapeA = [[False, False, False,False],
#           [False, False, False,False],
#           [True, True, True,True]]

# shapeB = [[False, False, False,False],
#           [True, False, False,False],
#           [True, True, True,False]]

# shapeC = [[False, False, False,False],
#           [False, False, False,True],
#           [False, True, True,True]]

# shapeD = [[False, False, False,False],
#           [True, True, False,False],
#           [True, True, False,False]]

# shapeE = [[False, False, False,False],
#           [False, True, True,False],
#           [True, True, False,False]]

# shapeF = [[False, False, False,False],
#           [False, True, False,False],
#           [True, True, True,False]]

# shapeG = [[False, False, False,False],
#           [False, True, True,False],
#           [False, False, True,True]]

# A = [[False, False, False,False],
#      [False, False, False,False],
#      [True, True, True,True]]


# Homework #3
# Create a function called "make_block" that takes in alphabet,
# return the shape that is equal to that alphabet

# def make_block(alphabet):
#     #Write Code
#     if alphabet == 'A':
#         return shapeA

#     if alphabet == 'B':
#         return shapeB

#     if alphabet == 'C':
#         return shapeC

#     if alphabet == 'D':
#         return shapeD

#     if alphabet == 'E':
#         return shapeE

#     if alphabet == 'F':
#         return shapeF

#     if alphabet == 'G':
#         return shapeG


# print(make_block('G'))

# without any arguments, randomly choose blocks whenever the function is called
# block_list = ['shapeA', 'shapeB', 'shapeC', 'shapeD', 'shapeE', 'shapeF']
# def make_block():
#     next_block = random.choice(block_list)
#     #random.choice({container}) -> wil pick random element from the container
#     if next_block == 'shapeA':
#         return shapeA

#     if next_block == 'shapeB':
#         return shapeB

#     if next_block == 'shapeC':
#         return shapeC

#     if next_block == 'shapeD':
#         return shapeD

#     if next_block == 'shapeE':
#         return shapeE

#     if next_block == 'shapeF':
#         return shapeF

#     if next_block == 'shapeG':
#         return shapeG

# print(make_blockimport random
# from tkinter import *
#
# # lst1 = [1,2,3,4] #list of inegers
# # lst2 = ["string1", "string2", "string3"] #list of string
# # lst3 = [False, False, True] #list of boolean
#
# # for numbers in lst1:
# #     print(numbers)
#
# # for index in range(0,len(lst1)):
# #     print(lst1[index])
#
# # len() method will return number of elements from a list
#
#
# # 2D list
# # lst_2D = [[1,2,3], [4,5,6]]
#
# # 3D list
# # lst_3D = [[[1,2,3]]]
#
# # print(lst_2D[0]) #[1,2,3]
# # print(lst_2D[0][1]) #2
#
# # print #3 from 3D list
# # print(lst_3D[0][0][2])
#
# # Nested For Loop
# # for lst in lst_2D:
# #     print(lst)
# #     for numbers in lst:
# #         print(numbers)
#
#
# # In-Class Assignment
# # print out the sum of all the elements from the list
# # lst = [1,2,3,4]
#
# # output
# # 10
#
# # sum()
# # Hint
# # Make a variable that can add numbers
#
# # sum = 0
# # for number in lst:
# #     sum += number
#
# # print(sum)
#
# # Homework #1
# # lst_2D = [[1,2,3], [4,5,6]]
# # You need to print out sum of all the elements from lst_2D
# # output : 21
#
# # sum = 0
#
# # for lst in lst_2D:
# #     print(lst) # [1,2,3] (done)
# #                # [4,5,6]
# #     for numbers in lst:
# #         sum += numbers
# # 1. sum will now be 6 (1 + 2 + 3)
# # 2. sum will now be 21 (6 + 4 + 5 + 6)
#
# # print(sum)
#
#
# # empty shape
# # shape = [[0,0,0],
# #          [0,1,0],
# #          [1,1,1]]
#
# # for row in range(0,3):
# #     for col in range(0,3):
# #         if shape[row][col] == 1:
# #             print(row, col)
#
#
# # For our tetris game, we will use list of booleans to reprsent tetris blocks
# # shape = [[0,0,0],
# #          [0,1,0],
# #          [1,1,1]]
#
# # 0 represents False
# # 1 reprsents True
#
# # shape = [[False,False,False],
# #          [False,True,False],
# #          [True,True,True]]
#
# # Homework #2.
# # Create all the shapes with boolean 2D_list
#
# # shapeA = [[False, False, False,False],
# #           [False, False, False,False],
# #           [True, True, True,True]]
#
# # shapeB = [[False, False, False,False],
# #           [True, False, False,False],
# #           [True, True, True,False]]
#
# # shapeC = [[False, False, False,False],
# #           [False, False, False,True],
# #           [False, True, True,True]]
#
# # shapeD = [[False, False, False,False],
# #           [True, True, False,False],
# #           [True, True, False,False]]
#
# # shapeE = [[False, False, False,False],
# #           [False, True, True,False],
# #           [True, True, False,False]]
#
# # shapeF = [[False, False, False,False],
# #           [False, True, False,False],
# #           [True, True, True,False]]
#
# # shapeG = [[False, False, False,False],
# #           [False, True, True,False],
# #           [False, False, True,True]]
#
# # A = [[False, False, False,False],
# #      [False, False, False,False],
# #      [True, True, True,True]]
#
#
# # Homework #3
# # Create a function called "make_block" that takes in alphabet,
# # return the shape that is equal to that alphabet
#
# # def make_block(alphabet):
# #     #Write Code
# #     if alphabet == 'A':
# #         return shapeA
#
# #     if alphabet == 'B':
# #         return shapeB
#
# #     if alphabet == 'C':
# #         return shapeC
#
# #     if alphabet == 'D':
# #         return shapeD
#
# #     if alphabet == 'E':
# #         return shapeE
#
# #     if alphabet == 'F':
# #         return shapeF
#
# #     if alphabet == 'G':
# #         return shapeG
#
#
# # print(make_block('G'))
#
# # without any arguments, randomly choose blocks whenever the function is called
# # block_list = ['shapeA', 'shapeB', 'shapeC', 'shapeD', 'shapeE', 'shapeF']
# # def make_block():
# #     next_block = random.choice(block_list)
# #     #random.choice({container}) -> wil pick random element from the container
# #     if next_block == 'shapeA':
# #         return shapeA
#
# #     if next_block == 'shapeB':
# #         return shapeB
#
# #     if next_block == 'shapeC':
# #         return shapeC
#
# #     if next_block == 'shapeD':
# #         return shapeD
#
# #     if next_block == 'shapeE':
# #         return shapeE
#
# #     if next_block == 'shapeF':
# #         return shapeF
#
# #     if next_block == 'shapeG':
# #         return shapeG
#
# # print(make_block()) ())

#OOP review
#Object Oriented Programming

#What is Object Oriented Programming?
#Person can have lots of different characteristics (eye colors, name, and etc)
#Person can perform different tasks(teach...study...etc)
#We can apply same concept into programming world, we call this "Object"

#To create an object, follow 3 steps
#1. Create a class
#2. think of what that class should have (characteristcs)
#3. Think of what that class can do (action)

#class (name of the class):
#

# class Student:
#     #attribute (characteristics of your object)
#     age = 14
#
#     #constructor (initialize values to your object)
#     def __init__(self,name,glasses):
#         self.name = name
#         self.glasses = glasses
#     #Class method (action)
#
#     def __str__(self):
#         message = "This is Student class, the name of this object is " + self.name
#         return message
#     def study(self):
#         message = self.name + " is studying"
#         return message
#
#     #class method
#     def changeName(self,friend,new_name):
#         friend.name = new_name
#
# student1 = Student("John", True)
# student2 = Student("Sam", False)

# print(student1)
# print(student1.name)
# print(student1.study())
# print(student2.name)
# student1.changeName(student2,"David")
# print(student2.name)

# print(student1.age)
# print(student2.age)

#print(student1.age)
#print(student2.age)

#attributes are shared by all object (example: age)
#constructor is customized attributes for individual object
#method is a special function made only for that object
#__str__ is a method to print out customized message
#__repr__ is a method to print out customized message for the object but __str__ have higher priority

#*args

# def printName(arg1,arg2):
#     print(arg1,arg2)

# def printName(*args):
#     for names in args:
#         print(names)
#
# printName("Sunny","David","Sam","John")

#Create a class of Warrior #1
#Warrior can be initialized with name, power, country, and weapon
#For the country, warriors were all born in Korea

#If we print out Warrior object using print(), display message "This is Warrior Class! name is {warrior_name}" #2

#Warriors can fight with other Warrios, create a method called battle(self, fighter) #3
#If warrior my object is fighting have bigger power, my object lose the battle -> print out "I lost!"
#-> extra work : also display power difference of your object and fighter, subtract 
#If my object have higher power -> print out "I won!"
#If my object have same power -> print out "We can't fight!"

#binary converter

#00000000
#00000001 -> 2^0 -> 1
#00000011 -> 2^1 + 2^0 = 3

# #Backend
# def print_selection():
#     val = 0
#     power = 0
#     #varlist is where all the integer values are in
#     #cbList is where
#     for v in varlist:
#         if v.get() == 1:
#             cv["text"] = '1'
#             val += 2 ** power
#         else:
#             cb["text"] = '0'
#         power += 1
#
#     1["text"] = str(val)
# #Frontend
#
# window = Tk()
# window.title('Binary Converter')
# window.geometry('100x300')
#
# l = Label(window, bg= 'white', width=20, text='empty')
# l.pack() #pack method puts the lavbel on top of the window (layer)
#
# numFrame = Frame(window) #Frame is like a window only for the numbers
# #[0,0,0,0,0,0,0,0]
# varList = []
#
#
# var1 = IntVar(window,0)
# var2 = IntVar(window,0)
# var3 = IntVar(window,0)
# var4 = IntVar(window,0)
# var5 = IntVar(window,0)
# var6 = IntVar(window,0)
# var7 = IntVar(window,0)
# var8 = IntVar(window,0)
#
# varList.append(var1)
# varList.append(var2)
# varList.append(var3)
# varList.append(var4)
# varList.append(var5)
# varList.append(var6)
# varList.append(var7)
# varList.append(var8)
#
# cbList = [] #list for checkbbox
# c1 = Checkbutton(numFrame, text = '0', variable=var1, onvalue=1, offvalue = 0)
# c1.pack()
# c2 = Checkbutton(numFrame,text = '0', variable=var2, onvalue=1, offvalue = 0)
# c2.pack()
# c3 = Checkbutton(numFrame,text = '0', variable=var3, onvalue=1, offvalue = 0)
# c3.pack()
# c4 = Checkbutton(numFrame,text = '0', variable=var4, onvalue=1, offvalue=0)
# c4.pack()
# c5 = Checkbutton(numFrame,text = '0', variable=var5, onvalue=1, offvalue=0)
# c5.pack()
# c6 = Checkbutton(numFrame,text = '0', variable=var6, onvalue=1, offvalue=0)
# c6.pack()
# c7 = Checkbutton(numFrame,text = '0', variable=var7, onvalue=1, offvalue=0)
# c7.pack()
# c8 = Checkbutton(numFrame,text = '0', variable=var8,  onvalue=1, offvalue=0)
# c8.pack()
#
#
# numFrame.pack()
# window.mainloop()

import tkinter as tk

#Lambda Function

#Lambda is anonymous function we make to simplify our code

#Create a function that adds three to the input

#def addThree(n):
#   return n+3

# print(addThree(3))

#template of using lambda
#lambda (argument) : function result

#the advantage of using lambda is we can use variable like a function

# n = lambda input : input + 3
# print(n(3))

# def addTwo(a,b):
#   return a + b

# print(addTwo(1,2))

# n = lambda input1, input2 : input1 + input2
#print(n(1,2))

m = lambda input : input + 15
n = lambda input1, input2: input1*input2

print(m(10))
print(n(12,4))

def solution(lst):
    res = []
    for numbers in lst:
        res.append(numbers*3)
    return res

lamb = lambda lst=[1,2,3,4,5] : solution(lst)
print(lamb())

#write a lambda function that filters even numbers
#your input will be [2,3,5,6,9,12,16]
#output will be 2, 6, 12, 16

#Hint:
#1. Create a function first, that takes in list as an input and returns a new list that only have even numbers
#2. Use Lambda to provide input to that function and print out the result
#3. %2 == 0 -> filter out even numbers

# lst = [2,3,5,6,9,12,16]


# def evenFilter(lst):
#     newLst = [] #new list that will only contain even numbers
#     for numbers in lst:
# def evenFilter(lst):
#     newLst = [] #new list that will only contain even numbers
#     for numbers in lst:
#         if numbers % 2 == 0:
#             newLst.append(numbers)
#     return newLst

#print(evenFilter(lst))

# answer = lambda  lst :  evenFilter(lst)
# print(answer(lst))
#enumerate()

#when we use for loop, there are two ways
#first, using for loop combined with index
#second, using for loop combined with container name

# lst = ["John", "Rob", "Sam", "Smith"]

#for index in range(0,len(lst)):
#   #print(index)
#   print(lst[index])

# for vals in lst:
#   print(vals)

#enumerate() assign index to each values
#combine index, values together in tuple, so we can use both separately
#
# for enum in enumerate(lst):
#     print(enum)

#for index,


#Using enumerate, create a function "evenFilter2" that prints out numbers that are even AND have even index
#Save those numbers in a newLst and return that list
#
# lst = [2,4,3,6,8,10]
# #      0 1 2 3 4 5
# #output
# #2, 8
#
# def evenFilter2(lst):
#     #code
#     newLst = []
#     for index, vals in enumerate(lst):
#         if index % 2 == 0 and vals % 2 == 0:
#             newlst.append(vals)
#
#     return newlst
#
# print(evenFilter2(lst))

#try and except blocks

#try and except  blocks are used to take care of the errors

#in try block, we write codes that could "possibly" work
#if any errors happen, code moves to except block

#print(5/0) #Zero Dvision Error

try:
    a = 5/1
    print(a)

except:
    print("You divided number by zero!")

lst = [1,2,3,4,5]
for ele in lst:
    try:
        if ele % 2 == 0:
            a = ele/0 #Zero Division Error
        else:
            a = ele/1
    except:
        print("Zero Division Error!")
        print(ele)

#Common Errors include type conversion errors

# value = "a"
# print(int(value))

#In class Assignment
#For the given list, convert elements to integer and add it to the newlist
#if you can't do int type casting, add 0 to the newLst

lst = ["1", "3", "a", "b", "9"]
newlst = []

#output:
#[1,3,0,0,9]

#Hint
#Use for loop to check each elements and use int()
#Use try and except block inside for loop
#if error happens write your code inside the except block (adding 0 to the new list)

for ele in list:
    try:
        new_ele = int(ele) #converted element into an integer
        newlst.append(new_ele)
    except:
        newlst.append(0)

print(newlst)

from tkinter import *

#1. Create number input part
#2. Create different number buttons
#3. Create operator button
#4. Create backend part and connect each buttons

disValue = 0
#Backend

#Frontend
win = Tk()
win.title('Calculator')

#fg allows us to change the color of our font
#justiry allows us to place number on specific location

str_value = StringVar()
str_value.set("Hello")
dis = Entry(win, textvariable = "Hello", bg='white', fg='red', justify='right')

#grid() -> method allows us to pick specific location to place our entry or buttons
#ipadx, ipady allows us to increase the size of the x and y
#columnspan allows us to increase the size of the columns
dis.grid(column=0, row=0, ipadx=80, ipady=30)

calItem = [['1', '2', '3', '4'],
           ['5','6','7','8'],
           ['9','0','+','-'],
           ['/','*','C','=']]

item1 = calItem[0]
for enum in enumerate(item1):
    print(enum)

bt = Button(win, text ='1', width=10, height=5,bg='black',fg='white')
bt.grid()

bt2 = Button(win, text='2',width=10,height=5,bg='black',fg='white')
bt2.grid(column=1, row=1)

bt3 = Button(win, text='2',width=10,height=5,bg='black',fg='white')
bt3.grid(column=2, row=1)

bt4 = Button(win, text='2',width=10,height=5,bg='black',fg='white')
bt4.grid(column=3, row=1)

bt5 = Button(win, text='2',width=10,height=5,bg='black',fg='white')
bt5.grid(column=0, row=2)

bt6 = Button(win, text='2',width=10,height=5,bg='black',fg='white')
bt6.grid(column=1, row=2)

bt7 = Button(win, text='2',width=10,height=5,bg='black',fg='white')
bt7.grid(column=2, row=2)

bt8 = Button(win, text='2',width=10,height=5,bg='black',fg='white')
bt8.grid(column=3, row=12

win.mainloop()
