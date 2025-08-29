a = True
while a:
    print('*'*(a))
    a += 1
    if a == 15:
        print('ni hao fineshyt')
        break

print('\n')

def pyramid(n):
    for i in range(n):
        print(' '*(n-i-1) + '*'*(2*i+1))

pyramid(5)

print('\n')
# while pyramid

a = 1
while a <= 5:
    print(' '*(5-a) + '*'*(2*a-1))
    a += 1

print('\n')

a = 1
while a <= 5:
    print(' '*(5-a) + '*'*a)
    a += 1