import io
import sys

_INPUT = """\
6
6 5
2 3
3 4
3 5
5 6
2 6
7
1 1
2 2
2 0
2 3
4 1
6 0
4 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from copy import deepcopy
  N,M=map(int,input().split())
  G=[set([i]) for i in range(N)]
  for _ in range(M):
    a,b=map(int,input().split())
    a-=1; b-=1
    G[a].add(b)
    G[b].add(a)
  G2=deepcopy(G)
  for i in range(N):
    for v in G[i]:
      for u in G[v]:
        G2[i].add(u)
  G3=deepcopy(G)
  for i in range(N):
    for v in G2[i]:
      for u in G[v]:
        G3[i].add(u)
  ans1,ans2,ans3=[sum([v+1 for v in G[i]]) for i in range(N)],[sum([v+1 for v in G2[i]]) for i in range(N)],[sum([v+1 for v in G3[i]]) for i in range(N)]
  Q=int(input())
  for _ in range(Q):
    x,k=map(int,input().split())
    x-=1
    if k==0: print(x+1)
    elif k==1: print(ans1[x])
    elif k==2: print(ans2[x])
    else: print(ans3[x])