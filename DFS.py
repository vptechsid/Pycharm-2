g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}
visited = [0] * 6
def dfs(g, n, s):
	visited[n] = 1
	if n == s:
		return True
	else:
		for ii in g[n]:
			if not visited[ii]:
				t = dfs(g, ii, s)
				if t:
					return t
		return False
a=list(map(int,input().split()))
m=input()
print(dfs(g, 2, 5))
