# -*- coding: utf-8 -*-

# 1, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41, 48, 49, 56, 57, 64, 65, 72, 73, 80, 
#81, 88, 89, 96, 97, 104, 105, 112, 113, 120, 122, 125, 129, 134, 140, 147 

#In Snooker there are 15 reds (1pt each), a yellow (2pts), green (3pts), brown (4pts), 
#blue (5pts), pink (6pts) and a black ball (7pts).

a=[1,2,3,4,5,6,7]
sum=0
for i in range(0,30):
    if i%2!=0:
        sum=sum+a[-1]
    else:
        sum=sum+a[0]
    print(sum)
inc=2
for j in range(1,7):
    sum=sum+inc
    print(sum)
    inc=inc+1

        
    
    