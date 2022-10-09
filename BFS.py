g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}
visited = [0] * 6

def bfs(g,n,s):
	dist={n:[n]}
	dq=[n]
	while len(dq):
		t=dq.pop()
		for ii in g[t]:
			if ii not in dist:
				dist[ii]=[*dist[t],ii]
				dq.append(ii)
	return dist[s]

print(bfs(g,0,2))
