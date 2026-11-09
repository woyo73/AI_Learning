# from player import Player
# player = Player("knight", 100)
# player.show_info()

# import calculator as cal
# print(cal.add(10, 20))

# from math import sqrt, pi
# import math as m

# print(sqrt(25))
# print(pi)
# print(m.sqrt(16))

# import random

# items = ["검", "방패", "활", "지팡이", "포션"]

# print("랜덤 아이템:", random.choice(items))
# print("랜덤 아이템 3개:", random.sample(items, 3))

# import random

# numbers = [1, 2, 3, 4, 5]

# random.shuffle(numbers)
# print(numbers)


# selected = random.sample(numbers, 3)
# print(selected)


# import sys

# print(sys.version)
# print(sys.getwindowsversion())
# a = int(sys.argv[1])
# b = int(sys.argv[2])

# print(a+b)


# import os
# print(os.name)
# print(os.getcwd())
# print(os.listdir())


# os.makedirs("test_folder")
# os.rmdir("test_folder")


# from urllib import request

# with request.urlopen("https://example.com") as response:
#     data = response.read()

# print(type(data))
# print(data[:100])






# from bs4 import BeautifulSoup

# html = """
#   <html>
#     <body>
#       <h1>파이썬 공부</h1>
#       <p>외부 모듈 테스트</p>
#     </body>
#   </html>
# """

# soup = BeautifulSoup(html, "html.parser")

# print(soup.h1.text)
# print(soup.p.text)




# from functools import wraps

# def decorator(func):
#   @wraps(func)
#   def wrapper():
#     print("시작")
#     func()
#     print("종료")

#   return wrapper


# @decorator
# def hello():
#   print("hello")



# hello()
# print(hello.__name__)




# from functools import wraps

# def deco(func):

#     @wraps(func)
#     def wrapper():
#         return func()

#     return wrapper


# @deco
# def hello():
#     """인사하는 함수"""
#     print("안녕하세요")


# print(hello.__name__)
# print(hello.__doc__)


import calculator

print(__name__)




















