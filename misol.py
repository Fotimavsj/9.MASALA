
# # 9.1 while
#
# n = int(input('n = '))
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i)
#     i = i + 1

# # 9.1 for
# 
# n = int(input('n= '))
# for i in range(1, n + 1, 1):
#     if n % i == 0:
#         print(i)

# # 9.2 while
#
# n = int(input('n= '))
# i = 1
# s = 0
# while i <= n:
#     if n % i == 0:
#         s = s + i
#     i = i + 1
# print(s)

# # 9.2 for
# 
# n = int(input('n= '))
# 
# s = 0
# for i in range(1, n + 1, 1):
#     if n % i == 0:
#         s = s + i
# print(s)

# # 9.3 while
#
# n = int(input('n= '))
# i = 1
# s = 0
# while i < n:
#     if n % i == 0:
#         s = s + i
#     i = i + 1
# if s == n:
#     print('mukammal son')
# else:
#     print('mukammal son emas')

# # 9.3 for
# 
# n = int(input('n= '))
# s = 0
# for i in range(1, n, 1):
#     if n % i == 0:
#         s = s + i
# if s == n:
#     print('mukammal son')
# else:
#     print('mukammal son emas')

# # 9.4 for
#
# n = int(input('n= '))
# for i in range(1, n, 1):
#     s = 0
#     j = 1
#     for j in range(j, i, 1):
#         if i % j == 0:
#             s = s + j
#     if s == i:
#         print(i)

# # 9.5 while
# 
# n = int(input('n= '))
# i = 1
# while i <= n:
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)
#     i = i + 1

# # 9.5 for
# 
# n = int(input('n= '))
# for i in range(1, n + 1, 1):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)

# # 9.6 while
#
# n = int(input('n= '))
# s = 0
# i = 1
# while i <= n:
#     if n % i == 0:
#         s = s + 1
#     i = i + 1
# if s == 2:
#     print('tub son')
# else:
#     print('tub son emas')

# # 9.6 for
# 
# n = int(input('n= '))
# s = 0
# for i in range(1, n + 1, 1):
#     if n % i == 0:
#         s = s + 1
# if s == 2:
#     print('tub son')
# else:
#     print('tub son emas')

# # 9.7 while
# 
# n = int(input('n= '))
# i = 1
# while i <= n:
#     j = 1
#     s = 0
#     while j <= i:
#         if i % j == 0:
#             s = s + 1
#         j = j + 1
#     if s == 2:
#         print(i)
#     i = i + 1

# # 9.7 for
#
# n = int(input('n= '))
# for i in range(1, n + 1, 1):
#     j = 1
#     s = 0
#     for j in range(j, i + 1, 1):
#         if i % j == 0:
#             s = s + 1
#         j = j + 1
#     if s == 2:
#         print(i)

# 9.10

# # a
#
# n = int(input('n= '))
# s = 0
# for i in range(1, n + 1, 1):
#     s = 2  n
# print(s)

# # b
#
# n = int(input('n= '))
# s = 1
# for i in range(1, n + 1, 1):
#     s = s * i
# print(s)

# # c
#
# n = int(input('n= '))
# i = 1
# s = 0
# p = 1
# while i <= n:
#     s = 1 + (1 / 1  2)
#     i = i + 1
#     p = p * s
# print(p)

# # d
#
# from math import *
# n = int(input('n= '))
# i = 2
# s = sqrt(2)
# while i <= n:
#     s = sqrt(s + 2)
#     i = i + 1
# print(s)

# # e
#
# from math import *
# n = int(input('n= '))
# i = 0
# s = 0
# p = 0
# while i < n:
#     s = (3 *(n - i))
#     p = sqrt(s + p)
#     i = i + 1
# print(p)

# # f
#
# from math import *
# n = int(input('n= '))
# i = 1
# a = sin(1)
# s = 1 / sin(1)
# while i <= n:
#     a = a + sin(i)
#     s = s + 1 / a
#     i = i + 1
# print(s)

# # g
# 
# from math import *
# n = int(input('n= '))
# i = 1
# s1 = cos(1)
# s2 = sin(1)
# s = cos(1) / sin(1)
# while i <= n:
#     s1 = s1 + cos(i)
#     s2 = s2 + sin(i)
#     s = s + (s1 / s2)
#     i = i + 1
# print(s)

# 9.11

# # a
#
# n = int(input('n= '))
# s = 0
# p = 1
# for i in range(1, n + 1, 1):
#     s = 1 / i  2
#     p = p + s
# print(p)

# # b
#
# n = int(input('n= '))
# s = 0
# p = 1
# for i in range(1, n + 1, 1):
#     s = 1 / i  3
#     p = p + s
# print(p)
# # c
#
# n = int(input('n= '))
# s1 = 1
# p = 1
# for i in range(1, n + 1, 1):
#     s = 0
#     j = 1
#     for j in range(j, i + 1, 1):
#         s1 = s1 + j
#     s = 1 / s1
#     p = p + s
# print(p)

# # d
#
# n = int(input('n= '))
# s = 0
# p = 0
# for i in range(1, n + 1, 1):
#     s = 1 / (2 * i)  2
#     p = p + s
# print(p)

# # e
#
# n = int(input('n= '))
# s = 0
# p = 1
# for i in range(2, n + 1, 1):
#     s = (i + 1) / (i + 2)
#     p = p * s
# print(p)

# # f
# 
# n = int(input('n= '))
# s1 = 1
# p = 1
# for i in range(2, n + 1, 1):
#     s = 0
#     j = 1
#     for j in range(j, i + 1, 1):
#         s1 = s1 * j
#     s = (1 + (1 / s1))  2
#     p = p * s
# print(p)

# 9.12

# # a
#
# a = float(input('a= '))
# n = int(input('n= '))
# s = 0
# for i in range(1, n):
#     s = a  n
# print(s)

# # b
#
# a = float(input('a= '))
# n = int(input('n= '))
# s = 0
# p = 1
# for i in range(1, n, 1):
#     s = a + i
#     p = p + s
# print(p * a)

# # c
#
# a = float(input('a= '))
# n = int(input('n= '))
# s = 0
# s1 = 0
# p = 1 / a
# p1 = 1
# for i in range(1, n + 1, 1):
#     s1 = a + i
#     p1 = p1 * s1
#     s = 1 / (a * p1)
#     p = p + s
# print(p)

# # d
# 
# a = float(input('a= '))
# n = int(input('n= '))
# s = 0
# p = 1
# for i in range(1, n + 1, 1):
#     s = a + n - i * n
#     p = p * s
# print(p)

# # 9.13
# 
# from math import *
# n = int(input('n= '))
# s = 0
# p = 0
# for i in range(1, n + 1, 1):
#     s = 1 + sin(i)
#     p = p + s
# print(p)

# # 9.14
# 
# x = float(input('x= '))
# a = float(input('a= '))
# n = int(input('n= '))
# s = x + a
# for i in range(1, n + 1, 1):
#     s = (s  2) + a
# print(s)

# # 9.15
# 
# n = int(input('n= '))
# s = 0
# p = 1
# for i in range(1, n + 1, 1):
#     for j in range(0, i + 1, 1):
#         p = p * (i + j)
#     s = s + p
#     p = 1
# print(s)
print("Fotima")
print("Feruza")
print("Dunyo")
print("Salom")