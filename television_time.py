intervals = [( 0, 4), (6, 8), (2, 4), (7, 9)]
a=set()
[ [a.add(i) for i in range(tup[0],tup[1])] for tup in intervals]
print(a)
