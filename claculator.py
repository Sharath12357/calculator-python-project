def get_input():
    a=int(input('eneter value 1'))
    b=int(input('enter value 2'))
    print('')
    return a,b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def true_div(a,b):
    return a/b
def floor_div(a,b):
    return a//b
def mod(a,b):
    return a%b
def square(a,b):
    return a**b
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def squareroot(n):
    a=n**0.5
    return a
while True:
    print('_'*100)
    print('enter 1: addition')
    print('enter 2: subtraction')
    print('enter 3: multiplication')
    print('enter 4: true division')
    print('enter 5: floor division')
    print('enter 6: modulus')
    print('enter 7: power')
    print('eneter 8 : fact')
    print('enter 9:square root')
    print('enetr 10 :to exit')
    print('-'*100)
    print(' ')
    ch=int(input('enter your choice:'))
    if ch==1:
        m,n=get_input()
        print('the sum is :',add(m,n))
    elif ch==2:
        m,n=get_input()
        print('the difference is:',sub(m,n))
    elif ch==3:
        m,n=get_input()
        print('the product is :',mul(m,n))
    elif ch==4:
        m,n=get_input()
        print('the true divison is :',true_div(m,n))
    elif ch==5:
        m,n=get_input()
        print('the floor divison is :',floor_div(m,n))
    elif ch==6:
        m,n=get_input()
        print('the module is :',mod(m,n))
    elif ch==7:
        m,n=get_input()
        print('the power is :',square(m,n))
    elif ch==8:
        print('the factorial is:',fact(int(input('enetr the value:'))))
    elif ch==9:
        print('the square root is  ',squareroot(int(input('enter the value:'))))
    elif ch==10:
        print('thank you')
        break
    else:
        print('invalid input')
    a=input('do you want to use(y/n)')
    if a.lower()=='y':
        continue
    else:
        print('thank you')
        break