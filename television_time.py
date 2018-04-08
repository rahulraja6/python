# -*- coding: utf-8 -*-

intervals_list = [( 1, 4), (6, 8), (2, 4), (7, 9)]
a=set([  [i for i in range(tup[0],tup[1],1)] for tup in intervals_list])
#char=[[ch for ch in word] for word in ("apple", "banana", "pear", "the", "hello")]
tup=( 1, 4)
arr=[i for i in range(tup[0],tup[1],1)]