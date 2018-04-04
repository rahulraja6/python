def shortestPath(longpath):
    we=0
    ns=0
    ns=sum([ns+1 if i is 'N' else ns-1 if i is 'S' else ns+0 for i in longpath])
    we=sum([we+1 if i is 'W' else we-1 if i is 'E' else we+0 for i in longpath])
#    shortpath='S'*abs(ns) if ns<0 else 'N'*abs(ns)
    shortpath=''.join(sorted(['S'*abs(ns) if ns<0 else 'N'*abs(ns),'E'*abs(we)])) if we<0 else ''.join(sorted(['S'*abs(ns) if ns<0 else 'N'*abs(ns),'W'*abs(we)]))
    return shortpath

print(shortestPath('NWESSSWWENNSW'))
    