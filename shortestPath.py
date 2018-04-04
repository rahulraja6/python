def shortestPath(longpath):
    we=0
    ns=0
    ns=sum([ns+1 if i is 'N' else ns-1 if i is 'S' else ns+0 for i in longpath])
    we=sum([we+1 if i is 'W' else we-1 if i is 'E' else we+0 for i in longpath])
    shortpath=''.join(['S'*abs(ns) if ns<0 else 'N'*abs(ns)])
    shortpath=''.join([''.join(sorted([shortpath,'E'*abs(we)])) if we<0 else ''.join(sorted([shortpath,'W'*abs(we)]))])
#    if we<0:
#        shortpath=''.join(sorted([shortpath,'E'*abs(we)]))
#    else:
#        shortpath=''.join(sorted([shortpath,'W'*abs(we)]))
    return shortpath

print(shortestPath('WWWWNN'))
    