
N,M=map(int,input().split())
a=[('.|.'*i).center(M,'-') for i in range(1,N,2)]
for e in a+['WELCOME'.center(M,'-')]+list(reversed(a)):print(e)


n, m = map(int,input().split())
pattern=[]
#pattern=[('*|*'*(2*i + 1)).center(m, '-') for i in range(n//2)]
for i in range(n//2):
    pattern.insert(i,('*|*'*(2*i + 1)).center(m, '-'))
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

r,c=map(int,input().split())
pattern=[(('*|*'*i).center(c,'-')) for i in range(1,r,2)]
print('\n'.join(pattern+['WELCOME'.center(c,'-')]+pattern[::-1]))