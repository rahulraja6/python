# -*- coding: utf-8 -*-
import itertools
bowl=list(range(1,10))*2
length=len(bowl)
#for index, i in enumerate(itertools.cycle(bowl)):
#    if index>length-1:
#        print(i)
#        break
#    else:
#            bowl.pop(0)
            
[ i   if index>length-1  else  bowl.pop(0) for index, i in enumerate(itertools.cycle(bowl))]