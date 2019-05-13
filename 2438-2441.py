#별찍기 

#2438
N = int(input())

for a in range(0, N):
    for b in range(0, a+1):
        print('*', end='')
    print('')

#2439
N = int(input())

for i in range(N):
    print(' '* (N-1), end='')
    print('*'*(i+1))
    N = N - 1
    
#2440
N = int(input())
for i in range(N):
    print('*'*N)
    N = N - 1

#2441
N = int(input())

for i in range(N):
    print(' ' * i,end='')
    print('*' * N)
    N -= 1
