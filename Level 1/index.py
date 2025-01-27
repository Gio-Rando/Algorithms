def task1(a,b,c):
    if a > b:
        a,b = b,a
    return b // c - ( a- 1) // c 
print(task1(6,6,8))


def task2(a):
    binary = ""
    while a > 0:
        binary = str(a % 2) + binary
        a //= 2
    return binary
print(task2(10))

def task3(a):
    
    