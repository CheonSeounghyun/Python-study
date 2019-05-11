'''
Mirko works in a sugar factory as a delivery boy. He has just received an order: he has to deliver exactly N kilograms of sugar to a candy store on the Adriatic coast. Mirko can use two types of packages, the ones that contain 3 kilograms, and the ones with 5 kilograms of sugar.

Mirko would like to take as few packages as possible. For example, if he has to deliver 18 kilograms of sugar, he could use six 3-kilogram packages. But, it would be better to use three 5-kilogram packages, and one 3-kilogram package, resulting in the total of four packages.

Help Mirko by finding the minimum number of packages required to transport exactly N kilograms of sugar.
'''

N = int(input())
C = 0  # count

while N > 0:
    if N % 5 == 0:
        N -= 5
        C = C + 1
    elif N % 3 == 0:
        N -= 3
        C = C + 1
    elif N > 5:
        N -= 5
        C = C + 1
    else:
        C = -1
        break
print(C)
