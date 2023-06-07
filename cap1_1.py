import numpy as np
# from simpy import Symbol, solve
import sympy


def dec2bin(target):
    amari = []
    
    while target != 0:
        amari.append(target % 2)
        target = target // 2
        
    amari.reverse()
    return amari

def dec2hex(target):
    amari = []

    while target != 0:
        amari.append(target % 16)
        target = target // 16
        
    for i in range(len(amari)):
        if amari[i] == 10: amari[i] = "A"
        elif amari[i] == 11: amari[i] = "B"
        elif amari[i] == 12: amari[i] = "C"
        elif amari[i] == 13: amari[i] = "D"
        elif amari[i] == 14: amari[i] = "E"
        elif amari[i] == 15: amari[i] = "F"
    amari.reverse()
    return amari

def any2Dec(target, m):
    n = len(target) - 1
    sum = 0
    
    for i in range(n + 1):
        if target[i] == "A": num = 10
        elif target[i] == "B" : num = 11
        elif target[i] == "C" : num = 12
        elif target[i] == "D" : num = 13
        elif target[i] == "E" : num = 14
        elif target[i] == "F" : num = 15
        else:
            num = int(target[i])
            print(num)
        sum += (m ** n) * num
        n -= 1
    return sum

def dec2bin_ex(target):
    i = int(target)
    f = target - i
    
    a = []

    while i != 0:
        a.append(i % 2)
        i = i // 2
        
    a.reverse()
    
    b = []
    n = 0
    while f != 0:
        temp = f * 2
        b.append(int(temp))
        f = temp - int(temp)
        n+=1
        # 実数誤差に対応するため
        if n >= 10:
            break
    return a, b

def get_pexel_color(color):
    r = color >> 16 & 0xff
    g = color >> 8 & 0xff
    b = color & 0xff
    
    return r, g, b

def fibo(n):
    if n == 0:
        print("n == 0")
        return 0
    return n + fibo(n - 1)


def solveRenritu():
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    ex1 = -3/2*x + 6 - y
    ex2 = 1/2*x + 2 - y
    print(sympy.solve((ex1, ex2)))

solveRenritu()

# x = np.arange(1, 10)
# y = x * 2
# print(x)
# print(y)

# color = 4287090426
# r, g, b = get_pexel_color(color)
# print(r)
# print(g)
# print(b)
# result = fibo(10)
# print(result)
# print(any2Dec("1A", 16))

# a, b = dec2bin_ex(10.625)
# print(a)
# print(b)

# num = 26
# print(hex(num))
# print(dec2hex(num))
# print(bin(num))
# print(dec2bin(num))